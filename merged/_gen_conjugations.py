"""
Generate conjugation tables for 150 DE + 150 FR verbs using DeepSeek.
- Batches 10 verbs per API call
- Writes incrementally to data/conjugations-de.json and data/conjugations-fr.json
- Skips verbs already cached; fully resumable
"""

import sys
import json
import time
from pathlib import Path

# ── paths ───────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent
DATA = ROOT / "data"

EXISTING_DE = DATA / "existing_de_verbs.txt"
EXISTING_FR = DATA / "existing_fr_verbs.txt"
NEW_DE      = DATA / "new_de_verbs.json"
NEW_FR      = DATA / "new_fr_verbs.json"
CACHE_DE    = DATA / "conjugations-de.json"
CACHE_FR    = DATA / "conjugations-fr.json"

sys.path.insert(0, str(ROOT))
from _deepseek import ask_json

BATCH = 10   # verbs per DeepSeek call

# ── helpers ──────────────────────────────────────────────────────────────────
def load_cache(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"[warn] {path.name} corrupt – starting fresh")
    return {}


def save_cache(path: Path, data: dict):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_verb_list(txt_path: Path) -> list[str]:
    return [l.strip() for l in txt_path.read_text(encoding="utf-8").splitlines() if l.strip()]


def load_new_verbs(json_path: Path, key: str) -> list[str]:
    items = json.loads(json_path.read_text(encoding="utf-8"))
    return [item[key] for item in items]


# ── DE prompt ────────────────────────────────────────────────────────────────
DE_SCHEMA = """{
  "VERB": {
    "aux": "haben|sein",
    "prasens":      {"ich":"","du":"","er":"","wir":"","ihr":"","sie":""},
    "prateritum":   {"ich":"","du":"","er":"","wir":"","ihr":"","sie":""},
    "konjunktiv_ii":{"ich":"","du":"","er":"","wir":"","ihr":"","sie":""},
    "perfekt_ptcp": "string",
    "imperativ":    {"du":"","ihr":"","sie":""}
  }
}"""

def build_de_prompt(verbs: list[str]) -> str:
    verb_list = ", ".join(f'"{v}"' for v in verbs)
    return f"""Return ONLY valid JSON (no markdown, no explanation) with conjugation tables for these German verbs: {verb_list}

Use exactly this schema for each verb (replace VERB with the infinitive):
{DE_SCHEMA}

Rules:
- Use standard/dictionary forms only.
- Preserve umlauts: ä ö ü ß
- "aux" must be either "haben" or "sein"
- "perfekt_ptcp" is the past participle only (e.g. "gegessen", "gegangen")
- "imperativ.sie" always uses the full polite form (e.g. "essen Sie", "gehen Sie")
- For separable verbs keep the prefix attached in conjugated forms
- Return ALL {len(verbs)} verbs in one JSON object, keys are the infinitives"""


# ── FR prompt ────────────────────────────────────────────────────────────────
FR_SCHEMA = """{
  "VERB": {
    "aux": "avoir|être",
    "present":            {"je":"","tu":"","il":"","nous":"","vous":"","ils":""},
    "imparfait":          {"je":"","tu":"","il":"","nous":"","vous":"","ils":""},
    "futur_simple":       {"je":"","tu":"","il":"","nous":"","vous":"","ils":""},
    "subjonctif":         {"je":"","tu":"","il":"","nous":"","vous":"","ils":""},
    "passe_compose_ptcp": "string",
    "imperatif":          {"tu":"","nous":"","vous":""}
  }
}"""

def build_fr_prompt(verbs: list[str]) -> str:
    verb_list = ", ".join(f'"{v}"' for v in verbs)
    return f"""Return ONLY valid JSON (no markdown, no explanation) with conjugation tables for these French verbs: {verb_list}

Use exactly this schema for each verb (replace VERB with the infinitive):
{FR_SCHEMA}

Rules:
- Use standard/dictionary forms only.
- Preserve accents: à è é ê ç î ô û ù
- "aux" must be either "avoir" or "être"
- "passe_compose_ptcp" is the past participle only (e.g. "mangé", "allé")
- Subjonctif uses present subjunctive (que je/tu/il/nous/vous/ils)
- For reflexive verbs (e.g. "se souvenir") include the reflexive pronoun in each conjugated form
- Return ALL {len(verbs)} verbs in one JSON object, keys are the infinitives"""


# ── batch processor ──────────────────────────────────────────────────────────
def process_language(
    lang: str,
    all_verbs: list[str],
    cache_path: Path,
    prompt_fn,
) -> list[str]:
    cache = load_cache(cache_path)
    pending = [v for v in all_verbs if v not in cache]
    failed  = []

    total   = len(all_verbs)
    cached  = total - len(pending)
    print(f"\n[{lang}] {total} verbs total | {cached} already cached | {len(pending)} to fetch")

    batches = [pending[i:i+BATCH] for i in range(0, len(pending), BATCH)]

    for bi, batch in enumerate(batches, 1):
        print(f"  [{lang}] Batch {bi}/{len(batches)}: {batch}")
        t0 = time.time()
        try:
            result = ask_json(prompt_fn(batch))
            elapsed = time.time() - t0

            # accept responses where keys match (DeepSeek may normalise keys)
            inserted = []
            for verb in batch:
                if verb in result:
                    cache[verb] = result[verb]
                    inserted.append(verb)
                else:
                    # try case-insensitive match
                    lv = verb.lower()
                    match = next((k for k in result if k.lower() == lv), None)
                    if match:
                        cache[verb] = result[match]
                        inserted.append(verb)
                    else:
                        print(f"    [warn] '{verb}' not found in response keys: {list(result.keys())}")
                        failed.append(verb)

            save_cache(cache_path, cache)
            print(f"    -> saved {len(inserted)} verbs in {elapsed:.1f}s  (cache now {len(cache)})")

        except Exception as exc:
            print(f"    [ERROR] batch {bi} failed: {exc}")
            for verb in batch:
                failed.append(verb)
            # save whatever we have so far
            save_cache(cache_path, cache)

        # small pause between batches to be polite to the API
        if bi < len(batches):
            time.sleep(1)

    return failed


# ── main ─────────────────────────────────────────────────────────────────────
def main():
    # Build DE verb list (existing 120 + new 30 = 150)
    de_existing = load_verb_list(EXISTING_DE)
    de_new      = load_new_verbs(NEW_DE, "de")
    de_all      = de_existing + [v for v in de_new if v not in de_existing]
    assert len(de_all) == 150, f"DE list has {len(de_all)} verbs, expected 150"

    # Build FR verb list (existing 120 + new 30 = 150)
    fr_existing = load_verb_list(EXISTING_FR)
    fr_new      = load_new_verbs(NEW_FR, "fr")
    fr_all      = fr_existing + [v for v in fr_new if v not in fr_existing]
    assert len(fr_all) == 150, f"FR list has {len(fr_all)} verbs, expected 150"

    print("=" * 60)
    print(f"DE verbs: {len(de_all)}  |  FR verbs: {len(fr_all)}")
    print("=" * 60)

    t_start = time.time()

    failed_de = process_language("DE", de_all, CACHE_DE, build_de_prompt)
    failed_fr = process_language("FR", fr_all, CACHE_FR, build_fr_prompt)

    elapsed = time.time() - t_start

    # ── final verification ───────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)

    cache_de = load_cache(CACHE_DE)
    cache_fr = load_cache(CACHE_FR)

    print(f"conjugations-de.json  keys: {len(cache_de)}  (expected 150)")
    print(f"conjugations-fr.json  keys: {len(cache_fr)}  (expected 150)")

    # spot-check structure
    def check_structure(cache, lang):
        problems = []
        if lang == "DE":
            required = {"aux","prasens","prateritum","konjunktiv_ii","perfekt_ptcp","imperativ"}
            persons  = {"ich","du","er","wir","ihr","sie"}
            tenses   = {"prasens","prateritum","konjunktiv_ii"}
        else:
            required = {"aux","present","imparfait","futur_simple","subjonctif",
                        "passe_compose_ptcp","imperatif"}
            persons  = {"je","tu","il","nous","vous","ils"}
            tenses   = {"present","imparfait","futur_simple","subjonctif"}

        for verb, data in cache.items():
            missing = required - set(data.keys())
            if missing:
                problems.append(f"  {verb}: missing fields {missing}")
            for t in tenses:
                if t in data:
                    mp = persons - set(data[t].keys())
                    if mp:
                        problems.append(f"  {verb}.{t}: missing persons {mp}")
        return problems

    prob_de = check_structure(cache_de, "DE")
    prob_fr = check_structure(cache_fr, "FR")

    if prob_de:
        print(f"\n[DE] {len(prob_de)} structural issues:")
        for p in prob_de[:20]:
            print(p)
    else:
        print("\n[DE] structure OK for all cached verbs")

    if prob_fr:
        print(f"\n[FR] {len(prob_fr)} structural issues:")
        for p in prob_fr[:20]:
            print(p)
    else:
        print("\n[FR] structure OK for all cached verbs")

    if failed_de:
        print(f"\n[DE] {len(failed_de)} verbs FAILED: {failed_de}")
    else:
        print("\n[DE] no failures")

    if failed_fr:
        print(f"\n[FR] {len(failed_fr)} verbs FAILED: {failed_fr}")
    else:
        print("\n[FR] no failures")

    print(f"\nTotal time: {elapsed/60:.1f} minutes")
    print("Done.")


if __name__ == "__main__":
    main()
