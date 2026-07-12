"""
Transforms the FR app HTML into a polyglot merged shell.

Reads: ../../App francês/francais/index.html  (already PT UI)
Writes: index.html  (this dir)

Adds:
  - Language chooser modal shown on first launch
  - Runtime LANG toggle in top bar (DE / FR)
  - Loads both data-de and data-fr, exposes DATA() based on LANG
  - Headword-keyed `mastered` store (never breaks on verb reorder)
  - Migration hook: reads verben_v1 / deutsch_app_v2 / francais_app_v1 → polyglot_v1
  - Per-lang article widget (der/die/das for DE, le/la for FR)
  - Per-lang level themes and translation targets

Does NOT yet add:
  - Conjugation game (waiting on data)
"""
from pathlib import Path
import re

SRC = Path(__file__).parent.parent.parent / "App francês" / "francais" / "index.html"
DST = Path(__file__).parent / "index.html"

html = SRC.read_text(encoding="utf-8")

# ── 1. Swap the single verb-data + noun-data script tags for the six namespaced ones ──
html = html.replace(
    '<script src="verb-data.js"></script>\n<script src="noun-data.js"></script>',
    '<script src="verb-data-de.js"></script>\n'
    '<script src="verb-data-fr.js"></script>\n'
    '<script src="noun-data-de.js"></script>\n'
    '<script src="noun-data-fr.js"></script>\n'
    '<script src="conjugations-de.js"></script>\n'
    '<script src="conjugations-fr.js"></script>',
)

# ── 2. Replace DATA constants block with polyglot version ──
html = re.sub(
    r'const VERBS = \(window\.VERBS_DATA \|\| \[\]\)\.slice\(\);\s*'
    r'/\* NOUNS[^*]*\*/\s*'
    r'const NOUNS = \(window\.NOUNS_DATA \|\| \[\]\)\.slice\(\);\s*'
    r'const NOUN_LEVEL_STARTS = \(window\.NOUN_LEVELS && window\.NOUN_LEVELS\.starts\) \|\| null;',
    '''/* Polyglot: two languages, chosen at runtime */
const LANG_PACKS = {
  de: {
    verbs: (window.VERBS_DATA_DE || []).slice(),
    nouns: (window.NOUNS_DATA_DE || []).slice(),
    nounLevelStarts: (window.NOUN_LEVELS_DE && window.NOUN_LEVELS_DE.starts) || null,
    nounLevelNames: (window.NOUN_LEVELS_DE && window.NOUN_LEVELS_DE.names) || [],
    articles: ["der","die","das"],
    persons: {verbs:["ich","du","er","wir","ihr","sie"]},
    // in DE content, translation targets are: en, fr, pt
    targets: ["en","fr","pt"],
    label: "Deutsch",
    brand: "Deu<em>tsch</em>",
    eyebrow: "Deu<em>tsch</em>",
    langWordPt: "alemão",
    homeSub: "Do dia a dia à filosofia — o vocabulário essencial do pensamento alemão.",
    learnVerbsDesc: "Vira as cartas — alemão na frente, três traduções atrás.",
    learnNounsDesc: "Cartas com artigo (der/die/das), plural e traduções.",
    aboutH2: "Deutsch — verbos &amp; substantivos",
    aboutPara2: "<b>Os substantivos pendem para as humanidades:</b> níveis 1–12 são vocabulário do cotidiano; níveis 13–25 constroem o vocabulário filosófico alemão — ser, espírito, ética, política, estética, saber, linguagem, cultura, religião, natureza, fenomenologia, teoria crítica, economia, direito.",
    conj: (window.CONJUGATIONS_DE || {}),
    tenses: [
      {key:"prasens",       pt:"Presente",       persons:["ich","du","er","wir","ihr","sie"]},
      {key:"prateritum",    pt:"Pretérito",      persons:["ich","du","er","wir","ihr","sie"]},
      {key:"konjunktiv_ii", pt:"Konjunktiv II",  persons:["ich","du","er","wir","ihr","sie"]},
      {key:"imperativ",     pt:"Imperativo",     persons:["du","ihr","sie"]},
    ],
    // "aux + past participle" is a compound tense we quiz differently (ask for ptcp).
    compoundTense: {key:"perfekt_ptcp", pt:"Particípio (Perfekt)"},
  },
  fr: {
    verbs: (window.VERBS_DATA_FR || []).slice(),
    nouns: (window.NOUNS_DATA_FR || []).slice(),
    nounLevelStarts: (window.NOUN_LEVELS_FR && window.NOUN_LEVELS_FR.starts) || null,
    nounLevelNames: (window.NOUN_LEVELS_FR && window.NOUN_LEVELS_FR.names) || [],
    articles: ["le","la"],
    persons: {verbs:["je","tu","il","nous","vous","ils"]},
    targets: ["en","de","pt"],
    label: "Français",
    brand: "Fran<em>çais</em>",
    eyebrow: "Fran<em>çais</em>",
    langWordPt: "francês",
    homeSub: "Do cotidiano a Derrida — o vocabulário que carrega o pensamento francês.",
    learnVerbsDesc: "Vira as cartas — francês na frente, três traduções atrás.",
    learnNounsDesc: "Cartas com artigo (le/la), plural e traduções.",
    aboutH2: "Français — verbos &amp; substantivos",
    aboutPara2: "<b>Os substantivos pendem para as humanidades:</b> níveis 1–10 são vocabulário do cotidiano; níveis 11–25 constroem o vocabulário filosófico francês — ser, mente, ética, política, estética, saber, linguagem, cultura, religião, natureza, fenomenologia, teoria crítica, economia, direito.",
    conj: (window.CONJUGATIONS_FR || {}),
    tenses: [
      {key:"present",      pt:"Presente",         persons:["je","tu","il","nous","vous","ils"]},
      {key:"imparfait",    pt:"Imperfeito",       persons:["je","tu","il","nous","vous","ils"]},
      {key:"futur_simple", pt:"Futuro simples",   persons:["je","tu","il","nous","vous","ils"]},
      {key:"subjonctif",   pt:"Subjuntivo",       persons:["je","tu","il","nous","vous","ils"]},
      {key:"imperatif",    pt:"Imperativo",       persons:["tu","nous","vous"]},
    ],
    compoundTense: {key:"passe_compose_ptcp", pt:"Particípio (Passé)"},
  }
};
let LANG = "de";  // set from store or chooser on load
function LP(){ return LANG_PACKS[LANG]; }
function VERBS(){ return LP().verbs; }
function NOUNS(){ return LP().nouns; }
function NOUN_LEVEL_STARTS(){ return LP().nounLevelStarts; }
// primary headword accessor: v[LANG] holds the headword (v.de for DE verbs/nouns, v.fr for FR)
function head(v){ return v[LANG]; }''',
    html, count=1, flags=re.DOTALL,
)

# ── 3. Storage key & shape — polyglot_v1, headword-keyed ──
html = html.replace(
    'const KEY = "francais_app_v1";',
    'const KEY = "polyglot_v1";',
)

# Rewrite ensureStore + load with headword-keyed shape and 3-way migration
html = re.sub(
    r'let store = load\(\);.*?ensureStore\(\);',
    '''let store = load();
function load(){ try{return JSON.parse(localStorage.getItem(KEY))||{}}catch(e){return {}} }
function save(){ try{localStorage.setItem(KEY, JSON.stringify(store))}catch(e){} }
function emptyPack(){ return {
  verbs:{mastered:{},conjMastered:{},bestStreak:0,ultimate:null},
  nouns:{mastered:{},bestStreak:0,ultimate:null,articleBest:0}
};}
function ensureStore(){
  if(!store._schema) store._schema = 1;
  store.langs = store.langs || {};
  if(!store.langs.de) store.langs.de = emptyPack();
  if(!store.langs.fr) store.langs.fr = emptyPack();
  store.rank = store.rank || 0;
  store._migrations = store._migrations || {};
  runMigrations();
}
function migrateFromLegacy(rawKey, targetLang, mflag){
  if(store._migrations[mflag]) return;
  const raw = localStorage.getItem(rawKey);
  if(!raw){ store._migrations[mflag]=1; return; }
  let old; try{ old = JSON.parse(raw)||{}; }catch(e){ store._migrations[mflag]=1; return; }
  const pack = store.langs[targetLang];
  // verbs
  const vArr = LANG_PACKS[targetLang].verbs;
  const vOld = old.verbs || old;  // verben_v1 was verbs-only at root
  if(vOld && vOld.mastered){
    for(const idx in vOld.mastered){
      const v = vArr[+idx];
      if(v){ pack.verbs.mastered[v[targetLang]] = 1; }
    }
    if(vOld.bestStreak) pack.verbs.bestStreak = Math.max(pack.verbs.bestStreak, vOld.bestStreak);
    if(vOld.ultimate) pack.verbs.ultimate = pack.verbs.ultimate || vOld.ultimate;
  }
  // nouns
  const nArr = LANG_PACKS[targetLang].nouns;
  if(old.nouns){
    for(const idx in (old.nouns.mastered||{})){
      const n = nArr[+idx];
      if(n){ pack.nouns.mastered[n[targetLang]] = 1; }
    }
    if(old.nouns.bestStreak) pack.nouns.bestStreak = Math.max(pack.nouns.bestStreak, old.nouns.bestStreak);
    if(old.nouns.ultimate) pack.nouns.ultimate = pack.nouns.ultimate || old.nouns.ultimate;
    if(old.nouns.articleBest) pack.nouns.articleBest = Math.max(pack.nouns.articleBest, old.nouns.articleBest);
  }
  if(old.rank) store.rank = Math.max(store.rank, old.rank);
  store._migrations[mflag] = 1;
}
function runMigrations(){
  migrateFromLegacy("verben_v1",     "de", "from_verben_v1");
  migrateFromLegacy("deutsch_app_v2","de", "from_deutsch_app_v2");
  migrateFromLegacy("francais_app_v1","fr","from_francais_app_v1");
  save();
}
ensureStore();
// pick active language: stored choice, else chooser modal on first paint
LANG = store.active_lang || null;''',
    html, count=1, flags=re.DOTALL,
)

# ── 4. tstore() and helpers: headword-keyed ──
html = html.replace(
    'function tstore(){ return store[TRACK]; }',
    'function tstore(){ return store.langs[LANG][TRACK]; }',
)
html = html.replace(
    'function totalMastered(){\n'
    '  return Object.keys(store.verbs.mastered).length + Object.keys(store.nouns.mastered).length;\n'
    '}',
    'function totalMastered(){\n'
    '  const p = store.langs[LANG];\n'
    '  return Object.keys(p.verbs.mastered).length + Object.keys(p.nouns.mastered).length;\n'
    '}',
)

# ── 5. DATA(), N() to use headword collections ──
html = html.replace(
    'const DATA = () => TRACK==="verbs" ? VERBS : NOUNS;',
    'const DATA = () => TRACK==="verbs" ? VERBS() : NOUNS();',
)

# ── 6. markMastered: use headword as key ──
html = re.sub(
    r'function markMastered\(vi\)\{[^}]*if\(!s\.mastered\[vi\]\)\{[^}]*s\.mastered\[vi\]=1;[^}]*save\(\);[^}]*checkRankUp\(\);[^}]*\}[^}]*\}',
    '''function markMastered(vi){
    const s = tstore();
    const k = head(DATA()[vi]);
    if(!s.mastered[k]){
      s.mastered[k]=1; save();
      checkRankUp();
    }
  }''',
    html, count=1, flags=re.DOTALL,
)

# ── 7. levelMasteredCount + buildLevelChips: use headword lookup ──
html = html.replace(
    'function levelMasteredCount(l){\n'
    '  const idxs = levelIndices(l);\n'
    '  const m = tstore().mastered;\n'
    '  return idxs.filter(i=>m[i]).length;\n'
    '}',
    'function levelMasteredCount(l){\n'
    '  const idxs = levelIndices(l);\n'
    '  const m = tstore().mastered;\n'
    '  return idxs.filter(i=>m[head(DATA()[i])]).length;\n'
    '}',
)

# Catalogue rendering — headword-keyed mastered check
html = re.sub(
    r'(row\.className="vrow"\+\(mastered\[)vi(\]\?" mastered":""\);)',
    r'\1head(v)\2',
    html,
)

# ── 8. Add language chooser modal + top-bar toggle ──
CHOOSER = '''<div class="levelup" id="lang-chooser"><div class="card">
  <h2 style="font-size:1.6rem;margin-bottom:14px">Escolha o idioma</h2>
  <p style="color:var(--muted);margin-bottom:18px;font-size:14px;line-height:1.55">Você vai treinar vocabulário e conjugação. Você pode alternar depois no cabeçalho.</p>
  <div style="display:flex;flex-direction:column;gap:10px">
    <button class="btn btn-primary" data-lang-pick="de">Deutsch — Alemão</button>
    <button class="btn btn-primary" data-lang-pick="fr">Français — Francês</button>
  </div>
</div></div>
'''
# Inject chooser right after <body> opening
html = re.sub(
    r'(<body[^>]*>)',
    r'\1\n' + CHOOSER,
    html, count=1,
)

# Persistent language switcher: fixed pill in the top-right, always visible.
TOGGLE = '''<div id="lang-switch" role="radiogroup" aria-label="Idioma">
  <button class="chip" id="lang-btn-de" role="radio" aria-checked="false" onclick="chooseLang('de')">DE</button>
  <button class="chip" id="lang-btn-fr" role="radio" aria-checked="false" onclick="chooseLang('fr')">FR</button>
</div>'''
html = re.sub(
    r'(<body[^>]*>)',
    r'\1\n' + TOGGLE,
    html, count=1,
)

# ── 9. Init JS: language chooser handling ──
INIT_JS = '''
// ── Language chooser + toggle (chooseLang avoids collision with source pickLang) ──
function chooseLang(lg){
  LANG = lg;
  store.active_lang = lg;
  save();
  document.getElementById("lang-chooser").classList.remove("show");
  document.body.classList.toggle("lang-de", lg==="de");
  document.body.classList.toggle("lang-fr", lg==="fr");
  const de=document.getElementById("lang-btn-de"), fr=document.getElementById("lang-btn-fr");
  if(de){ de.classList.toggle("on", lg==="de"); de.setAttribute("aria-checked", lg==="de" ? "true" : "false"); }
  if(fr){ fr.classList.toggle("on", lg==="fr"); fr.setAttribute("aria-checked", lg==="fr" ? "true" : "false"); }
  renderArtChoices();
  renderHome();
}
document.querySelectorAll("[data-lang-pick]").forEach(b=>{
  b.addEventListener("click", ()=>chooseLang(b.dataset.langPick));
});
if(!LANG){
  document.getElementById("lang-chooser").classList.add("show");
}else{
  chooseLang(LANG);
}
'''
# Append init JS just before the closing </script> tag (before service worker block)
html = html.replace(
    'if("serviceWorker" in navigator){',
    INIT_JS + '\nif("serviceWorker" in navigator){',
)

# ── 9b. Per-language color identity: Prussian for DE, Bleu-de-France Imperial for FR ──
LANG_THEME_CSS = '''
/* ── Language identities ───────────────────────────────────
   DE = Prussian:  deep Prussian-blue field, cold gold trim
   FR = Imperial:  bleu-de-France royal, fleur-d'or trim
   Applied to <body class="lang-de"> / <body class="lang-fr">.
   Boss/noun accents still override for those specific screens.
   ────────────────────────────────────────────────────────── */
body.lang-de{
  --prussian:#0d2a45;
  --prussian-2:#12395e;
  --prussian-deep:#061a2c;
  --iron:#8a94a8;
  --gold-cold:#c8a24a;
  --gold-cold-deep:#a5822f;
  --accent:var(--gold-cold);
  --accent-deep:var(--gold-cold-deep);
  background:var(--prussian-deep);
  background-image:
    radial-gradient(1100px 620px at 82% -12%, rgba(200,162,74,.10), transparent 60%),
    radial-gradient(900px 560px at -10% 108%, rgba(18,57,94,.55), transparent 62%),
    linear-gradient(180deg, var(--prussian-deep), #030a13 100%);
}
body.lang-de .brand h1 em{color:var(--gold-cold);text-shadow:0 0 22px rgba(200,162,74,.25)}
body.lang-de .dot{background:var(--gold-cold);color:var(--gold-cold)}
body.lang-de.nouns{ --accent:#7fb2e0; --accent-deep:#5088c3; }  /* Prussian steel-blue for nouns */
body.lang-de.boss{ --accent:#a374ff; --accent-deep:#7c4dff; }

body.lang-fr{
  --imperial:#002395;
  --imperial-2:#0055a4;
  --imperial-deep:#001a70;
  --fleur:#ffd700;
  --fleur-deep:#d4af37;
  --accent:var(--fleur);
  --accent-deep:var(--fleur-deep);
  background:var(--imperial-deep);
  background-image:
    radial-gradient(1100px 620px at 82% -12%, rgba(255,215,0,.10), transparent 60%),
    radial-gradient(900px 560px at -10% 108%, rgba(0,85,164,.55), transparent 62%),
    linear-gradient(180deg, var(--imperial-deep), #030a13 100%);
}
body.lang-fr .brand h1 em{color:var(--fleur);text-shadow:0 0 22px rgba(255,215,0,.25)}
body.lang-fr .dot{background:var(--fleur);color:var(--fleur)}
body.lang-fr.nouns{ --accent:#4d94ff; --accent-deep:#0055a4; }  /* Imperial blue for nouns */
body.lang-fr.boss{ --accent:#a374ff; --accent-deep:#7c4dff; }
'''
html = html.replace('</style>', LANG_THEME_CSS + '</style>', 1)

# ── 10. Manifest name + brand strings ──
html = re.sub(
    r'<title>[^<]*</title>',
    '<title>Polyglot — Deutsch & Français</title>',
    html, count=1,
)

# ── 11. Fix VERBS/NOUNS array uses (they became functions in polyglot) ──
# These are inside the JS body, after the DATA constants block.
for pat, rep in [
    (r'\bNOUNS\.length\b',   'NOUNS().length'),
    (r'\bVERBS\.length\b',   'VERBS().length'),
    (r'\bNOUNS\.map\(',      'NOUNS().map('),
    (r'\bVERBS\.map\(',      'VERBS().map('),
    (r'\bNOUNS\[',           'NOUNS()['),
    (r'\bVERBS\[',           'VERBS()['),
]:
    # Only substitute inside <script> — safe because CSS/HTML doesn't use these names
    html = re.sub(pat, rep, html)

# ── 12. store.verbs / store.nouns → store.langs[LANG].verbs / .nouns ──
html = html.replace('store.verbs', 'store.langs[LANG].verbs')
html = html.replace('store.nouns', 'store.langs[LANG].nouns')

# ── 13. v.fr / n.fr in render-layer JS → head(v) / head(n) ──
# CSS classes .fr are unaffected (they never appear as v.fr in stylesheet)
html = re.sub(r'\bv\.fr\b', 'head(v)', html)
html = re.sub(r'\bn\.fr\b', 'head(n)', html)

# ── 14. Hard-coded translation-target labels → dynamic trList helper ──
# Insert helper after head() definition
HELPER = '''
function trList(v){
  // Render translation targets for current LANG as pill spans.
  return LP().targets.map(t => {
    const arr = v[t] || [];
    const rest = arr.length>1 ? ", "+arr.slice(1).join(", ") : "";
    return `<span><i>${t.toUpperCase()}</i><b>${arr[0]||""}</b>${rest}</span>`;
  }).join("");
}
function trInline(v){
  // Compact "en · de · pt" style for feedback.
  return LP().targets.map(t => (v[t]||[])[0] || "").join(" · ");
}'''
html = html.replace(
    'function head(v){ return v[LANG]; }',
    'function head(v){ return v[LANG]; }' + HELPER,
    1,
)

# Replace the three-line `<span><i>EN|DE|PT</i>...` blocks in the catalogue render with `${trList(v)}`
html = re.sub(
    r'<span><i>EN</i><b>\$\{v\.en\[0\]\}</b>\$\{v\.en\.length>1\?", "\+v\.en\.slice\(1\)\.join\(", "\):""\}</span>\s*'
    r'<span><i>DE</i><b>\$\{v\.de\[0\]\}</b>\$\{v\.de\.length>1\?", "\+v\.de\.slice\(1\)\.join\(", "\):""\}</span>\s*'
    r'<span><i>PT</i><b>\$\{v\.pt\[0\]\}</b>\$\{v\.pt\.length>1\?", "\+v\.pt\.slice\(1\)\.join\(", "\):""\}</span>',
    '${trList(v)}',
    html,
)

# Replace the inline `${v.en[0]} · ${v.de[0]} · ${v.pt[0]}` in art-feedback with trInline
html = html.replace('${v.en[0]} · ${v.de[0]} · ${v.pt[0]}', '${trInline(v)}')

# ── 14b. Fix vocab learn renderCard: hardcoded ["en","de","pt"] crashes in DE mode ──
# Root cause: in DE data, v.de is the headword STRING; calling .slice(1).join throws.
# Also: front card tag and plural article are hard-coded — must be per-LANG.
html = html.replace(
    '<span class="tag">DE</span><span class="badge" id="learn-badge">',
    '<span class="tag" id="learn-tag">DE</span><span class="badge" id="learn-badge">',
)
html = html.replace(
    '''  front.className = "verb" + (TRACK==="nouns" ? " "+v.art : "");
  if(TRACK==="nouns"){
    front.innerHTML = `<span class="art">${v.art}</span>${head(v)}`;
    plural.textContent = v.pl && v.pl!=="—" ? "pl. les "+v.pl : "(sem plural)";
  } else {
    front.textContent = head(v);
    plural.textContent = "";
  }
  const isMastered = tstore().mastered[vi];
  $("#learn-badge").textContent = isMastered ? "✓ dominado" : "";
  const t=$("#learn-trans"); t.innerHTML="";
  ["en","de","pt"].forEach(lg=>{
    const row=document.createElement("div"); row.className="trow";
    const alt = v[lg].length>1 ? ` <span class="alt">· ${v[lg].slice(1).join(", ")}</span>` : "";
    row.innerHTML=`<span class="lg">${lg.toUpperCase()}</span><span class="w">${v[lg][0]}${alt}</span>`;
    t.appendChild(row);
  });
  if(TRACK==="nouns" && v.pl && v.pl!=="—"){
    const row=document.createElement("div"); row.className="trow pl";
    row.innerHTML=`<span class="lg">PL</span><span class="w">die ${v.pl}</span>`;
    t.appendChild(row);
  }''',
    '''  front.className = "verb" + (TRACK==="nouns" ? " "+v.art : "");
  const plArt = LANG==="de" ? "die" : "les";
  if(TRACK==="nouns"){
    front.innerHTML = `<span class="art">${v.art}</span>${head(v)}`;
    plural.textContent = v.pl && v.pl!=="—" ? "pl. "+plArt+" "+v.pl : "(sem plural)";
  } else {
    front.textContent = head(v);
    plural.textContent = "";
  }
  const tagEl = document.getElementById("learn-tag");
  if(tagEl) tagEl.textContent = LANG.toUpperCase();
  const isMastered = tstore().mastered[vi];
  $("#learn-badge").textContent = isMastered ? "✓ dominado" : "";
  const t=$("#learn-trans"); t.innerHTML="";
  LP().targets.forEach(lg=>{
    const arr = v[lg] || [];
    const row=document.createElement("div"); row.className="trow";
    const alt = arr.length>1 ? ` <span class="alt">· ${arr.slice(1).join(", ")}</span>` : "";
    row.innerHTML=`<span class="lg">${lg.toUpperCase()}</span><span class="w">${arr[0]||""}${alt}</span>`;
    t.appendChild(row);
  });
  if(TRACK==="nouns" && v.pl && v.pl!=="—"){
    const row=document.createElement("div"); row.className="trow pl";
    row.innerHTML=`<span class="lg">PL</span><span class="w">${plArt} ${v.pl}</span>`;
    t.appendChild(row);
  }''',
)

# ── 15. Article widget: dynamic button set per LANG ──
# Empty out the hard-coded le/la buttons; we'll fill them in JS.
html = html.replace(
    '<div class="art-choice" id="art-choices"><button class="le" data-a="le">le</button><button class="la" data-a="la">la</button></div>',
    '<div class="art-choice" id="art-choices"></div>',
)

# Insert renderArtChoices() + delegated click binding.
# Replace `$$("#art-choices button").forEach(b=>b.addEventListener("click", ()=>{` with delegated click
# Then call renderArtChoices() from startArticle & pickLang.
ART_HELPER = '''
function renderArtChoices(){
  const box = document.getElementById("art-choices");
  if(!box) return;
  box.innerHTML = LP().articles.map(a =>
    `<button class="${a}" data-a="${a}">${a}</button>`
  ).join("");
}
// delegated click for article buttons
document.getElementById("art-choices")?.addEventListener("click", (ev)=>{
  const b = ev.target.closest("button[data-a]");
  if(!b) return;
  if(asession.checked) return;
  asession.checked=true; asession.attempts++;
  const vi=asession.queue[asession.idx]; const v=NOUNS()[vi];
  const pick = b.dataset.a; const ok = pick===v.art;
  document.querySelectorAll("#art-choices button").forEach(x=>{
    x.disabled=true;
    if(x.dataset.a===v.art) x.classList.add("correct");
    else if(x===b) x.classList.add("wrong");
  });
  if(ok){
    asession.correct++; asession.streak++; asession.best=Math.max(asession.best,asession.streak);
    const s = store.langs[LANG].nouns;
    if(asession.streak>(s.articleBest||0)){ s.articleBest=asession.streak; save(); }
    document.getElementById("art-feedback").innerHTML = `<span class="r-ok">✓ ${v.art} ${head(v)}</span><span class="allt">${trInline(v)}</span>`;
  } else {
    asession.streak=0;
    document.getElementById("art-feedback").innerHTML = `<span class="r-bad">✗ It's ${v.art} ${head(v)}</span><span class="allt">${trInline(v)}</span>`;
  }
  document.getElementById("art-next").style.display="block";
  document.getElementById("art-next").focus();
});
'''
# Kill the old single-time listener block (three lines starting with $$("#art-choices button").forEach(b=>b.addEventListener)...
html = re.sub(
    r'\$\$\("#art-choices button"\)\.forEach\(b=>b\.addEventListener\("click", \(\)=>\{[\s\S]*?\}\)\);\n',
    '',
    html, count=1,
)
# Inject the new helper before "$('#art-next').addEventListener(\"click\""
html = html.replace(
    '$("#art-next").addEventListener("click"',
    ART_HELPER + '\n$("#art-next").addEventListener("click"',
    1,
)

# Call renderArtChoices at start of article round and on pickLang.
html = html.replace(
    'function renderArt(){',
    'function renderArt(){\n  renderArtChoices();',
    1,
)
html = html.replace(
    '  renderHome();\n}\ndocument.querySelectorAll("[data-lang-pick]")',
    '  renderArtChoices();\n  renderHome();\n}\ndocument.querySelectorAll("[data-lang-pick]")',
    1,
)

# ── 16. Home copy: swap "Français" / "120 verbos" hard-codes for dynamic ──
# Reactive brand & eyebrow: set them at renderHome() time via LP().
# Insert a small updater into renderHome start.
HOME_UPDATE = '''function updateStaticCopy(){
  if(!LANG) return;  // chooser modal still up
  const lp = LP();
  // ── HOME ─────────────────────────────────────────────
  const eb = document.getElementById("home-eyebrow");
  if(eb) eb.innerHTML = lp.eyebrow + " · Verbos &amp; Substantivos";
  const h1 = document.querySelector("#screen-home h1");
  if(h1) h1.innerHTML = lp.brand + ".";
  const sub = document.querySelector("#screen-home .brand p");
  if(sub){
    sub.innerHTML = `Domine <b style="color:var(--text)">${VERBS().length} verbos</b> e <b style="color:var(--text)">${NOUNS().length} substantivos</b>. ${lp.homeSub}`;
  }
  // track chips
  document.querySelectorAll('.tracks button[data-track="verbs"] .cnt').forEach(el => el.textContent = VERBS().length);
  document.querySelectorAll('.tracks button[data-track="nouns"] .cnt').forEach(el => el.textContent = NOUNS().length);
  // Mode-card descriptions per container
  const verbsAprender = document.querySelector('#modes-verbs .mode:not(.ultimate) .d');
  if(verbsAprender) verbsAprender.textContent = lp.learnVerbsDesc;
  const nounsAprender = document.querySelectorAll('#modes-nouns .mode .d')[0];
  if(nounsAprender) nounsAprender.textContent = lp.learnNounsDesc;
  const nounsArt = document.querySelectorAll('#modes-nouns .mode .d')[1];
  if(nounsArt) nounsArt.textContent = lp.articles.join(" · ") + " — escolhe o gênero certo.";
  // Ultimate/boss mode-card counts
  const verbsUlt = document.querySelector('#modes-verbs .mode.ultimate .d');
  if(verbsUlt) verbsUlt.textContent = `Todos os ${VERBS().length}, sem dicas. Errou volta pra pilha. Vence o jogo.`;
  const nounsUlt = document.querySelector('#modes-nouns .mode.ultimate .d');
  if(nounsUlt) nounsUlt.textContent = `Todos os ${NOUNS().length}, sem dicas. Errou volta pra pilha.`;
  // ── ABOUT ─────────────────────────────────────────────
  const aH2 = document.querySelector("#screen-about h2");
  if(aH2) aH2.innerHTML = lp.aboutH2;
  const aParas = document.querySelectorAll("#screen-about > p");
  const total = VERBS().length + NOUNS().length;
  if(aParas[0]) aParas[0].innerHTML = `<b>Objetivo:</b> dominar as <b>${total} palavras</b> — ${VERBS().length} verbos e ${NOUNS().length} substantivos — pra traduzir qualquer uma de bate-pronto. Cada resposta certa marca a palavra como dominada.`;
  if(aParas[1]) aParas[1].innerHTML = lp.aboutPara2;
  if(aParas[2]) aParas[2].innerHTML = `<b>Os ranks</b> marcam o caminho de Iniciante (0) a Filósofo (${totalWords()} XP: ${VERBS().length} verbos + ${NOUNS().length} substantivos + ${totalConjCells()} conjugações).`;
  // ── DRILL / ARTICLE sub-labels ────────────────────────
  const qsub = document.getElementById("q-sub");
  if(qsub) qsub.textContent = lp.langWordPt;
  const artSub = document.getElementById("art-sub");
  if(artSub) artSub.textContent = "substantivo " + lp.langWordPt;
}
// Alias for compatibility with older call site
function updateHomeCopy(){ updateStaticCopy(); }
'''
html = html.replace(
    'function renderHome(){',
    HOME_UPDATE + 'function renderHome(){\n  if(!LANG) return;\n  updateHomeCopy();',
    1,
)

# Kill the hardcoded FR eyebrow override in renderHome (updateHomeCopy handles it).
html = re.sub(
    r'\$\("#home-eyebrow"\)\.textContent = TRACK==="verbs" \? "Français · 120 verbos" : "Français · " \+ N\(\) \+ " substantivos";\s*',
    '',
    html,
)

# ── 16b. Fix the dynamic q-sub label in drill so it says "alemão verbo" for DE ──
html = html.replace(
    '$("#q-sub").textContent = "francês "+(session.track==="verbs"?"verbo":"substantivo")+" · "+(session.mode==="ultimate"?"boss":"treino");',
    '$("#q-sub").textContent = LP().langWordPt+" "+(session.track==="verbs"?"verbo":"substantivo")+" · "+(session.mode==="ultimate"?"boss":"treino");',
)

# ── 16c. Catalogue crumb ──
html = html.replace(
    '$("#cat-crumb").textContent = "Catalogue · "+(TRACK==="verbs"?"120 verbs":"1000 nouns");',
    '$("#cat-crumb").textContent = "Catálogo · "+(TRACK==="verbs"?VERBS().length+" verbos":NOUNS().length+" substantivos");',
)

# ── 16c-fix. LEVEL_THEMES.verbs: extend from 12 to 15 entries (150 verbs / 10 per level) ──
html = html.replace(
    ' verbs:[\n'
    '  "Ser · Ter · Fazer","Modais & movimento","Cognição","Fala & vida","Trabalho & aprendizado",\n'
    '  "Percepção & crescimento","Tempo & prova","Existência & escolha","Emoção & perda","Mudança & luta",\n'
    '  "Formação","Descoberta"\n'
    ' ],',
    ' verbs:[\n'
    '  "Ser · Ter · Fazer","Modais & movimento","Cognição","Fala & vida","Trabalho & aprendizado",\n'
    '  "Percepção & crescimento","Tempo & prova","Existência & escolha","Emoção & perda","Mudança & luta",\n'
    '  "Formação","Descoberta","Sentimento & desejo","Ofício & criação","Rito & partida"\n'
    ' ],',
)

# ── 16c-fix2. RANKS ladder: everything scales with total XP (verbs + nouns + conj cells) ──
# Global rank counts translation mastered AND conjugation mastered.
# Ranks rescale proportionally per-LANG on pickLang.
html = html.replace(
    'function totalMastered(){\n'
    '  const p = store.langs[LANG];\n'
    '  return Object.keys(p.verbs.mastered).length + Object.keys(p.nouns.mastered).length;\n'
    '}',
    'function totalMastered(){\n'
    '  const p = store.langs[LANG];\n'
    '  return Object.keys(p.verbs.mastered).length\n'
    '       + Object.keys(p.nouns.mastered).length\n'
    '       + Object.keys(p.verbs.conjMastered||{}).length;\n'
    '}\n'
    'function totalConjCells(){\n'
    '  const conj = LP().conj || {}, tenses = LP().tenses, cmp = LP().compoundTense;\n'
    '  let n = 0;\n'
    '  for(const v in conj){\n'
    '    for(const t of tenses){\n'
    '      const cells = conj[v][t.key]; if(!cells) continue;\n'
    '      for(const p of t.persons){ if(cells[p]) n++; }\n'
    '    }\n'
    '    if(cmp && conj[v][cmp.key]) n++;\n'
    '  }\n'
    '  return n;\n'
    '}\n'
    'function totalWords(){ return VERBS().length + NOUNS().length + totalConjCells(); }\n'
    '// Rescale ranks proportionally to total XP so ladder makes sense per LANG.\n'
    '// Fractions of the total, in the same order as RANKS array.\n'
    'const _RANK_FRAC = [0, 0.02, 0.08, 0.18, 0.33, 0.50, 0.75, 1.00];\n'
    'function rescaleRanks(){\n'
    '  if(!LANG) return;\n'
    '  const T = totalWords();\n'
    '  for(let i=0;i<RANKS.length;i++) RANKS[i].min = Math.round(T * _RANK_FRAC[i]);\n'
    '}',
)

# Percentage + bar: use totalWords() instead of 1120
html = html.replace(
    '$("#rank-pct").textContent = Math.round(100*xp/1120)+"%";',
    '$("#rank-pct").textContent = Math.round(100*xp/totalWords())+"%";',
)
html = html.replace(
    '$("#rank-bar").style.width = (100*xp/1120)+"%";',
    '$("#rank-bar").style.width = Math.min(100, 100*xp/totalWords())+"%";',
)
# Final "Filósofo" message: use totalWords()
html = html.replace(
    '$("#rank-next").innerHTML = "🏆 <b>Todos os 1120 dominados. Você é Filósofo.</b>";',
    '$("#rank-next").innerHTML = `🏆 <b>Todos os ${totalWords()} dominados. Você é Filósofo.</b>`;',
)
# Drill summary promo message
html = html.replace(
    'promo.innerHTML = `+ <b>${nm}</b> recém-dominados — ${xp}/1120 rumo a Filósofo.`;',
    'promo.innerHTML = `+ <b>${nm}</b> recém-dominados — ${xp}/${totalWords()} rumo a Filósofo.`;',
)

# Rank widget static "/1120" text: wrap in span so we can update it per-lang
html = html.replace(
    '<div class="xp"><b id="rank-xp">0</b>/1120<br><span id="rank-pct">0%</span></div>',
    '<div class="xp"><b id="rank-xp">0</b>/<span id="rank-total">1120</span><br><span id="rank-pct">0%</span></div>',
)

# Update the static objetivo/ranks copy in Sobre so the placeholder 1120 doesn't briefly flash.
# (updateStaticCopy already rewrites these — this just makes the untouched source cleaner.)
# Also update rank-total inside updateStaticCopy.
html = html.replace(
    '  const artSub = document.getElementById("art-sub");\n'
    '  if(artSub) artSub.textContent = "substantivo " + lp.langWordPt;\n'
    '}',
    '  const artSub = document.getElementById("art-sub");\n'
    '  if(artSub) artSub.textContent = "substantivo " + lp.langWordPt;\n'
    '  // Rank widget total (uses XP = verbs + nouns + conj cells)\n'
    '  rescaleRanks();\n'
    '  const rt = document.getElementById("rank-total");\n'
    '  if(rt) rt.textContent = totalWords();\n'
    '}',
)

# ── 16d. Insert Conjugação mode-card BEFORE Ultimate; make Ultimate the last card ──
# Source has verbs Ultimate with idx 03. Prepend Conjugação (idx 03) and bump Ultimate to idx 04.
html = html.replace(
    '<button class="mode ultimate" data-go="ult-setup">\n'
    '        <span class="idx">03</span>\n'
    '        <span class="body"><span class="t">Ultimate <span class="medal">◆ boss</span></span><span class="d">Todos os 120, sem dicas. Errou volta pra pilha. Vence o jogo.</span></span>',
    '<button class="mode conjugation" data-go="conj-setup">\n'
    '        <span class="idx">03</span>\n'
    '        <span class="body"><span class="t">Conjugação</span><span class="d">Flashcards das tabelas ou treino digitando — todos os tempos.</span></span>\n'
    '        <span class="arw">→</span>\n'
    '      </button>\n'
    '      <button class="mode ultimate" data-go="ult-setup">\n'
    '        <span class="idx">04</span>\n'
    '        <span class="body"><span class="t">Ultimate <span class="medal">◆ boss</span></span><span class="d">Todos os 150 verbos + conjugações completas. Sem dicas. Errou volta pra pilha.</span></span>',
    1,
)

# ── 16d-fix. Conjugation drill marks conjMastered AND triggers rank promo ──
html = html.replace(
    '    store.langs[LANG].verbs.conjMastered[key] = 1;\n'
    '    save();',
    '    const _newConj = !store.langs[LANG].verbs.conjMastered[key];\n'
    '    store.langs[LANG].verbs.conjMastered[key] = 1;\n'
    '    save();\n'
    '    if(_newConj) checkRankUp();',
)

# ── 16d-fix2. Ultimate on verbs adds a conjugation phase after translations clear. ──
# We hijack finishUltimate: if track is verbs, chain into conjugation ultimate.
ULT_CONJ_PHASE = '''
/* Ultimate → conjugation phase (verbs only) */
let ultConjSess = null;
function buildUltConjQueue(){
  const conj = LP().conj || {}, tenses = LP().tenses, cmp = LP().compoundTense;
  const cells = [];
  for(const v in conj){
    for(const t of tenses){
      const row = conj[v][t.key]; if(!row) continue;
      for(const p of t.persons){
        if(row[p]) cells.push({verb:v, tense:t.key, tensePt:t.pt, person:p, answer:row[p]});
      }
    }
    if(cmp && conj[v][cmp.key]) cells.push({verb:v, tense:cmp.key, tensePt:cmp.pt, person:"—", answer:conj[v][cmp.key]});
  }
  // shuffle
  for(let i=cells.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [cells[i],cells[j]]=[cells[j],cells[i]]; }
  return cells;
}
function startUltConjPhase(){
  const queue = buildUltConjQueue();
  ultConjSess = {queue, idx:0, total:queue.length, correct:0, attempts:0,
                 streak:0, best:0, cleared:0, mistakes:0, start:Date.now(), checked:false};
  document.getElementById("conj-crumb").textContent = "Ultimate · fase 2/2 · conjugação";
  document.getElementById("conj-quit").textContent = "← Sair";
  // reuse conjugation play screen
  conjSess = ultConjSess;                       // let renderConjCard read it
  conjSess.isUltimate = true;
  show("conj-play");
  renderConjCard();
}
'''
# We inject ULT_CONJ_PHASE later (after CONJ_JS block lands in html — see 16f-post).

# finishUltimate: user picks phases via the ult-setup screen, so no auto-chain.

# In nextConj — when in Ultimate conjugation phase, wrong answers go back into queue.
html = html.replace(
    'function nextConj(){\n'
    '  if(!conjSess) return;\n'
    '  conjSess.idx++;\n'
    '  if(conjSess.idx >= conjSess.queue.length){',
    'function nextConj(){\n'
    '  if(!conjSess) return;\n'
    '  if(conjSess.isUltimate){\n'
    '    // wrong cells go to back of queue; correct ones drop out\n'
    '    const c = conjSess.queue.shift();\n'
    '    if(conjSess.lastOk){ conjSess.cleared++; }\n'
    '    else { conjSess.queue.push(c); conjSess.mistakes = (conjSess.mistakes||0)+1; }\n'
    '    if(conjSess.queue.length===0){\n'
    '      // victory: use victory screen\n'
    '      const secs=Math.round((Date.now()-conjSess.start)/1000);\n'
    '      const mm=Math.floor(secs/60), ss=String(secs%60).padStart(2,"0");\n'
    '      const total=conjSess.total;\n'
    '      const acc=Math.round(100*total/(total+(conjSess.mistakes||0)));\n'
    '      document.getElementById("vic-acc").textContent=acc+"%";\n'
    '      document.getElementById("vic-time").textContent=mm+":"+ss;\n'
    '      document.getElementById("vic-streak").textContent=conjSess.best;\n'
    '      document.getElementById("vic-sub").textContent = `Todas as ${total} conjugações dominadas — Ultimate zerado.`;\n'
    '      const s = store.langs[LANG].verbs;\n'
    '      if(!s.ultimate || acc>s.ultimate.acc) s.ultimate = {acc, time:mm+":"+ss};\n'
    '      save();\n'
    '      show("victory");\n'
    '      return;\n'
    '    }\n'
    '    renderConjCard();\n'
    '    return;\n'
    '  }\n'
    '  conjSess.idx++;\n'
    '  if(conjSess.idx >= conjSess.queue.length){',
)

# checkConj: in ultimate phase, track lastOk so nextConj can requeue on wrong.
html = html.replace(
    '  const ok = conjNorm(guess) === conjNorm(c.answer) ||\n'
    '             (accentFold(guess) === accentFold(c.answer) && guess.length>0);\n'
    '  if(ok){',
    '  const ok = conjNorm(guess) === conjNorm(c.answer) ||\n'
    '             (accentFold(guess) === accentFold(c.answer) && guess.length>0);\n'
    '  conjSess.lastOk = ok;\n'
    '  if(ok){',
)

# renderConjCard needs to read current cell from either sess type (uses conjSess.queue[idx] normally,
# for ultimate we use conjSess.queue[0])
# Find renderConjCard body:
html = html.replace(
    'function renderConjCard(){\n'
    '  if(!conjSess) return;\n'
    '  const c = conjSess.queue[conjSess.idx];',
    'function renderConjCard(){\n'
    '  if(!conjSess) return;\n'
    '  const c = conjSess.isUltimate ? conjSess.queue[0] : conjSess.queue[conjSess.idx];',
)

# updatePlayMeta for conj: existing card updates use idx — for ultimate, show cleared/total.
html = html.replace(
    '  document.getElementById("conj-count").textContent = (conjSess.idx+1) + " / " + conjSess.queue.length;\n'
    '  document.getElementById("conj-bar").style.width = (100*conjSess.idx/conjSess.queue.length)+"%";',
    '  if(conjSess.isUltimate){\n'
    '    document.getElementById("conj-count").textContent = conjSess.cleared + " / " + conjSess.total + " cleared";\n'
    '    document.getElementById("conj-bar").style.width = (100*conjSess.cleared/conjSess.total)+"%";\n'
    '  } else {\n'
    '    document.getElementById("conj-count").textContent = (conjSess.idx+1) + " / " + conjSess.queue.length;\n'
    '    document.getElementById("conj-bar").style.width = (100*conjSess.idx/conjSess.queue.length)+"%";\n'
    '  }',
)

# ── 16d-fix3. Ultimate phase picker: user chooses which phase to run. ──
# Inject a phase picker into the ult-setup screen (verbs → per-phase; nouns → hidden).
# Anchor must be unique to the ult-setup screen — use the ult-lang seg that follows.
html = html.replace(
    '<div class="field-label">Responder em</div>\n    <div class="seg" id="ult-lang">',
    '<div class="field-label" id="ult-phase-label">Escolha uma fase</div>\n'
    '    <div class="seg" id="ult-phase" style="flex-wrap:wrap;gap:6px"></div>\n'
    '    <div class="field-label" id="ult-lang-label">Responder em</div>\n'
    '    <div class="seg" id="ult-lang">',
    1,
)

ULT_PHASE_JS = '''
let ultPhase = "verbs";  // "verbs" | "nouns" | tense-key (prasens, prateritum, ...) | "conj_all"
function renderUltPhaseChoices(){
  const box = document.getElementById("ult-phase");
  const label = document.getElementById("ult-phase-label");
  if(!box || !label) return;
  const isVerbs = TRACK==="verbs";
  if(!isVerbs){
    // Nouns Ultimate stays as single phase (translate all nouns).
    ultPhase = "nouns";
    box.style.display = "none";
    label.style.display = "none";
    return;
  }
  box.style.display = "";
  label.style.display = "";
  const tenses = LP().tenses, cmp = LP().compoundTense;
  const opts = [
    {key:"verbs", label:"Tradução · "+VERBS().length+" verbos"},
    ...tenses.map(t => ({key:t.key, label:"Conjugação · "+t.pt})),
    ...(cmp ? [{key:cmp.key, label:"Conjugação · "+cmp.pt}] : []),
  ];
  ultPhase = "verbs";
  box.innerHTML = opts.map(o => `<button data-phase="${o.key}" class="${o.key==='verbs'?'on':''}">${o.label}</button>`).join("");
  box.onclick = (e) => {
    const b = e.target.closest("button[data-phase]"); if(!b) return;
    box.querySelectorAll("button").forEach(x => x.classList.remove("on"));
    b.classList.add("on");
    ultPhase = b.dataset.phase;
    // Update the count in rule 01
    updateUltCount();
    // Language chooser only relevant for translation phase
    const langBox = document.getElementById("ult-lang");
    if(langBox) langBox.style.display = ultPhase==="verbs" ? "" : "none";
    const langLabel = document.querySelector('#screen-ult-setup .field-label:not(#ult-phase-label)');
    if(langLabel) langLabel.style.display = ultPhase==="verbs" ? "" : "none";
  };
  updateUltCount();
}
function updateUltCount(){
  const el = document.getElementById("ult-count"); if(!el) return;
  if(ultPhase==="verbs") el.textContent = VERBS().length;
  else if(ultPhase==="nouns") el.textContent = NOUNS().length;
  else {
    // count conjugation cells for this tense
    const conj = LP().conj || {};
    const tense = LP().tenses.find(t => t.key===ultPhase) || (LP().compoundTense && LP().compoundTense.key===ultPhase ? LP().compoundTense : null);
    if(!tense){ el.textContent = "?"; return; }
    let n = 0;
    for(const v in conj){
      const cells = conj[v][ultPhase]; if(!cells) continue;
      if(tense.persons){ for(const p of tense.persons){ if(cells[p]) n++; } }
      else { n++; }
    }
    el.textContent = n;
  }
}
// Route ult-start to the correct starter based on ultPhase.
function startUltimatePhase(){
  if(ultPhase==="verbs" || ultPhase==="nouns"){ startUltimate(); return; }
  // Conjugation phase — build cell queue.
  const conj = LP().conj || {};
  const tense = LP().tenses.find(t => t.key===ultPhase) || (LP().compoundTense && LP().compoundTense.key===ultPhase ? LP().compoundTense : null);
  if(!tense){ alert("Fase indisponível."); return; }
  const cells = [];
  for(const v in conj){
    const row = conj[v][tense.key]; if(!row) continue;
    if(tense.persons){ for(const p of tense.persons){ if(row[p]) cells.push({verb:v, tense:tense.key, tensePt:tense.pt, person:p, answer:row[p]}); } }
    else if(row){ cells.push({verb:v, tense:tense.key, tensePt:tense.pt, person:"—", answer:row}); }
  }
  for(let i=cells.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [cells[i],cells[j]]=[cells[j],cells[i]]; }
  conjSess = {queue:cells, idx:0, total:cells.length, correct:0, attempts:0,
              streak:0, best:0, cleared:0, mistakes:0, start:Date.now(), checked:false, isUltimate:true};
  document.getElementById("conj-crumb").textContent = "Ultimate · " + tense.pt;
  document.getElementById("conj-quit").textContent = "← Sair";
  show("conj-play");
  renderConjCard();
}
'''
# Inject ULT_PHASE_JS near end (before setTrack("verbs")).
html = html.replace(
    'setTrack("verbs");\nrenderHome();',
    ULT_PHASE_JS + '\nsetTrack("verbs");\nrenderHome();',
    1,
)

# Route the Ultimate start button through startUltimatePhase.
html = html.replace(
    '$("#ult-start").addEventListener("click",startUltimate);',
    '$("#ult-start").addEventListener("click",startUltimatePhase);',
)

# Ensure the phase picker is (re)rendered whenever ult-setup is shown.
# The source likely uses show("ult-setup") — hook renderUltSetup which the source already calls.
html = html.replace(
    'function renderUltSetup(){',
    'function renderUltSetup(){\n  renderUltPhaseChoices();',
    1,
)

# Ultimate translation phase crumb: use plain "Ultimate · verbos/nouns" (no forced fase 1/2 since user picks).
html = html.replace(
    '$("#play-crumb").textContent="Ultimate · "+(TRACK==="verbs"?"verbs":"nouns");',
    '$("#play-crumb").textContent = "Ultimate · "+(TRACK==="verbs"?"tradução de verbos":"substantivos");',
)

# ── 16e. Add conjugation setup + play + summary screens ──
CONJ_SCREENS = '''
<!-- ============ CONJUGATION SETUP ============ -->
<section class="screen" id="screen-conj-setup">
  <div class="topbar"><button class="back" data-go="home">← Início</button><span class="spacer"></span><span class="crumb">Conjugação</span></div>
  <div class="panel-intro">
    <h2 style="font-size:1.4rem;font-weight:800;letter-spacing:-.01em;margin-bottom:8px">Conjugação</h2>
    <p style="color:var(--muted);font-size:14px;line-height:1.55;margin-bottom:14px" id="conj-setup-sub">Aprenda com flashcards ou treine digitando. Escolha um tempo verbal, ou todos.</p>
    <div id="conj-mode-choices" class="seg" style="gap:8px;margin-bottom:12px">
      <button data-mode="learn">Aprender · flashcards</button>
      <button data-mode="drill" class="on">Treinar · digitar</button>
    </div>
    <div id="conj-tense-choices" class="seg" style="flex-wrap:wrap;gap:8px;margin-bottom:10px"></div>
    <div id="conj-scope-choices" class="seg" style="gap:8px;margin-bottom:16px">
      <button data-scope="all" class="on">Todos os 150 verbos</button>
      <button data-scope="mastered">Dominados (revisão)</button>
      <button data-scope="unmastered">Só não dominados</button>
    </div>
    <button class="btn btn-primary" id="conj-start">Começar →</button>
  </div>
</section>

<!-- ============ CONJUGATION LEARN (flashcards) ============ -->
<section class="screen" id="screen-conj-learn">
  <div class="topbar"><button class="back" id="conj-learn-quit">← Sair</button><span class="spacer"></span><span class="crumb" id="conj-learn-crumb">Aprender conjugação</span></div>
  <div class="deckbar" style="margin-top:12px">
    <span class="counter"><b id="conj-learn-pos">1</b> / <span id="conj-learn-total">1</span></span>
    <button class="btn btn-ghost btn-sm" id="conj-learn-shuffle">⇄ Embaralhar</button>
  </div>
  <div class="flip" id="conj-flip">
    <div class="flip-inner">
      <div class="face front">
        <span class="tag" id="conj-learn-tag">DE</span><span class="badge" id="conj-learn-badge"></span>
        <div class="verb" id="conj-learn-verb">—</div>
        <div class="plural" id="conj-learn-tensename"></div>
        <div class="hint">toque para revelar a tabela</div>
      </div>
      <div class="face back">
        <span class="tag" id="conj-learn-backtag">Conjugação</span>
        <div class="trans" id="conj-learn-table" style="text-align:left;font-family:var(--mono);font-size:15px;line-height:1.75"></div>
      </div>
    </div>
  </div>
  <div class="flip-ctrls">
    <button class="btn btn-ghost nav-ic" id="conj-learn-prev">←</button>
    <button class="btn btn-primary" id="conj-learn-flip">Virar</button>
    <button class="btn btn-ghost nav-ic" id="conj-learn-next">→</button>
  </div>
</section>

<!-- ============ CONJUGATION PLAY ============ -->
<section class="screen" id="screen-conj-play">
  <div class="topbar"><button class="back" id="conj-quit">← Sair</button><span class="spacer"></span><span class="crumb" id="conj-crumb">Conjugação</span></div>
  <div class="playmeta">
    <span class="counter"><b id="conj-count">0 / 0</b></span>
    <span class="streak" id="conj-streak">streak 0</span>
  </div>
  <div class="progress"><div class="bar" id="conj-bar" style="width:0"></div></div>
  <div class="q-ask" style="margin-top:20px;text-align:center">
    <div class="q-word" id="conj-verb" style="font-size:1.8rem;font-weight:800;letter-spacing:-.02em"></div>
    <div class="q-sub" id="conj-tense" style="color:var(--muted);margin-top:6px;font-size:13px;letter-spacing:.05em;text-transform:uppercase"></div>
    <div style="margin-top:18px;font-family:var(--mono);font-size:22px;color:var(--accent)"><span id="conj-person"></span> <span style="color:var(--muted2)">___</span></div>
  </div>
  <input type="text" class="answer" id="conj-input" placeholder="digite a flexão…" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="margin-top:18px">
  <div class="feedback" id="conj-feedback" style="min-height:44px;margin-top:12px;text-align:center;font-size:14px"></div>
  <div style="display:flex;gap:10px;margin-top:14px">
    <button class="btn btn-primary" id="conj-check" style="flex:1">Verificar</button>
    <button class="btn btn-ghost" id="conj-skip">Pular</button>
  </div>
</section>
'''
# Inject before the catalogue screen
html = html.replace(
    '<!-- ============ CATALOGUE ============ -->',
    CONJ_SCREENS + '\n<!-- ============ CATALOGUE ============ -->',
    1,
)

# ── 16f. Conjugation JS logic ──
CONJ_JS = '''

/* ============================================================
   CONJUGATION GAME
   ============================================================ */
let conjCfg = {tense:"all", scope:"all", mode:"drill"};
let conjSess = null;
let conjLearnSess = null;
function accentFold(s){ return (s||"").toString().toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g,"").trim(); }
function conjNorm(s){ return (s||"").toString().toLowerCase().normalize("NFC").trim(); }
function renderConjSetup(){
  const box = document.getElementById("conj-tense-choices");
  if(!box) return;
  const tenses = LP().tenses;
  box.innerHTML = `<button data-tense="all" class="on">Todos</button>` +
    tenses.map(t => `<button data-tense="${t.key}">${t.pt}</button>`).join("") +
    (LP().compoundTense ? `<button data-tense="${LP().compoundTense.key}">${LP().compoundTense.pt}</button>` : "");
  conjCfg.tense = "all"; conjCfg.scope = "all"; conjCfg.mode = "drill";
  document.querySelectorAll("#conj-scope-choices button").forEach(b => b.classList.toggle("on", b.dataset.scope==="all"));
  document.querySelectorAll("#conj-mode-choices button").forEach(b => b.classList.toggle("on", b.dataset.mode==="drill"));
  const mc = document.getElementById("conj-mode-choices");
  if(mc && !mc.dataset.wired){
    mc.dataset.wired = "1";
    mc.addEventListener("click", (e) => {
      const b = e.target.closest("button[data-mode]"); if(!b) return;
      mc.querySelectorAll("button").forEach(x => x.classList.remove("on"));
      b.classList.add("on");
      conjCfg.mode = b.dataset.mode;
      const sc = document.getElementById("conj-scope-choices");
      const sub = document.getElementById("conj-setup-sub");
      const btn = document.getElementById("conj-start");
      if(conjCfg.mode === "learn"){
        if(sc) sc.style.display = "none";
        if(sub) sub.textContent = "Flashcards: verbo + tempo na frente, tabela completa atrás. Percorra com ← →.";
        if(btn) btn.textContent = "Abrir flashcards →";
      } else {
        if(sc) sc.style.display = "";
        if(sub) sub.textContent = "Digite a flexão para a pessoa pedida. Certas viram cartas dominadas.";
        if(btn) btn.textContent = "Começar treino →";
      }
    });
  }
  // event delegation
  box.onclick = (e) => {
    const b = e.target.closest("button[data-tense]"); if(!b) return;
    box.querySelectorAll("button").forEach(x => x.classList.remove("on"));
    b.classList.add("on");
    conjCfg.tense = b.dataset.tense;
  };
  const sc = document.getElementById("conj-scope-choices");
  sc.onclick = (e) => {
    const b = e.target.closest("button[data-scope]"); if(!b) return;
    sc.querySelectorAll("button").forEach(x => x.classList.remove("on"));
    b.classList.add("on");
    conjCfg.scope = b.dataset.scope;
  };
  // count in verb-count
  const total = VERBS().length;
  const allBtn = sc.querySelector('[data-scope="all"]');
  if(allBtn) allBtn.textContent = `Todos os ${total} verbos`;
}
function buildConjQueue(){
  // Build list of {verb, tense, person, answer} cells based on conjCfg.
  // Scope now filters by conj-cell mastery (revisão vs pendentes), not verb-translation mastery.
  const conj = LP().conj || {};
  const verbs = VERBS().map(v => v[LANG]).filter(v => conj[v]);
  const conjMastered = store.langs[LANG].verbs.conjMastered || {};
  const compound = LP().compoundTense;
  const cellKey = (v, t, p) => v + "|" + t + "|" + p;
  const scopeAccept = (v, t, p) => {
    const k = cellKey(v, t, p);
    if(conjCfg.scope === "mastered")   return !!conjMastered[k];
    if(conjCfg.scope === "unmastered") return !conjMastered[k];
    return true;
  };
  let cells = [];
  for(const v of verbs){
    const table = conj[v]; if(!table) continue;
    if(conjCfg.tense === compound?.key){
      const ans = table[compound.key];
      if(ans && scopeAccept(v, compound.key, "—")){
        cells.push({verb:v, tense:compound.key, tensePt:compound.pt, person:"—", answer:ans});
      }
    } else if(conjCfg.tense === "all"){
      for(const t of LP().tenses){
        const cells_t = table[t.key];
        if(!cells_t) continue;
        for(const p of t.persons){
          if(cells_t[p] && scopeAccept(v, t.key, p)){
            cells.push({verb:v, tense:t.key, tensePt:t.pt, person:p, answer:cells_t[p]});
          }
        }
      }
      if(compound && table[compound.key] && scopeAccept(v, compound.key, "—")){
        cells.push({verb:v, tense:compound.key, tensePt:compound.pt, person:"—", answer:table[compound.key]});
      }
    } else {
      const t = LP().tenses.find(x => x.key===conjCfg.tense);
      if(!t) continue;
      const cells_t = table[t.key]; if(!cells_t) continue;
      for(const p of t.persons){
        if(cells_t[p] && scopeAccept(v, t.key, p)){
          cells.push({verb:v, tense:t.key, tensePt:t.pt, person:p, answer:cells_t[p]});
        }
      }
    }
  }
  // Shuffle
  for(let i=cells.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [cells[i],cells[j]]=[cells[j],cells[i]]; }
  // Cap round size for sanity
  const cap = conjCfg.tense==="all" ? 60 : 40;
  return cells.slice(0, cap);
}
function startConj(){
  if(conjCfg.mode === "learn"){ startConjLearn(); return; }
  const queue = buildConjQueue();
  if(!queue.length){
    alert("Nada para treinar aqui. Escolha outro escopo.");
    return;
  }
  conjSess = {queue, idx:0, correct:0, attempts:0, streak:0, best:0, checked:false};
  document.getElementById("conj-crumb").textContent = "Conjugação · " + (conjCfg.tense==="all" ? "todos" : (LP().tenses.find(t=>t.key===conjCfg.tense)?.pt || LP().compoundTense?.pt || ""));
  show("conj-play"); renderConjCard();
}
function buildConjLearnQueue(){
  // One card per (verb, tense). Simple-tense card = full table; compound-tense card = single form.
  const conj = LP().conj || {};
  const verbs = VERBS().map(v => v[LANG]).filter(v => conj[v]);
  const compound = LP().compoundTense;
  const cards = [];
  for(const v of verbs){
    const table = conj[v]; if(!table) continue;
    const wantTense = conjCfg.tense;
    if(wantTense === "all"){
      for(const t of LP().tenses){
        if(table[t.key]) cards.push({verb:v, tenseKey:t.key, tensePt:t.pt, persons:t.persons, cells:table[t.key], compound:false});
      }
      if(compound && table[compound.key]) cards.push({verb:v, tenseKey:compound.key, tensePt:compound.pt, persons:["—"], cells:{"—":table[compound.key]}, compound:true});
    } else if(compound && wantTense === compound.key){
      if(table[compound.key]) cards.push({verb:v, tenseKey:compound.key, tensePt:compound.pt, persons:["—"], cells:{"—":table[compound.key]}, compound:true});
    } else {
      const t = LP().tenses.find(x => x.key === wantTense);
      if(t && table[t.key]) cards.push({verb:v, tenseKey:t.key, tensePt:t.pt, persons:t.persons, cells:table[t.key], compound:false});
    }
  }
  return cards;
}
function shuffleInPlace(a){ for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; }
function startConjLearn(){
  const cards = buildConjLearnQueue();
  if(!cards.length){ alert("Sem tabelas para mostrar. Escolha outro tempo."); return; }
  conjLearnSess = {cards, idx:0};
  document.getElementById("conj-learn-crumb").textContent = "Aprender · " + (conjCfg.tense==="all" ? "todos os tempos" : (LP().tenses.find(t=>t.key===conjCfg.tense)?.pt || LP().compoundTense?.pt || ""));
  document.getElementById("conj-learn-tag").textContent = LANG.toUpperCase();
  document.getElementById("conj-learn-backtag").textContent = "Conjugação";
  document.getElementById("conj-learn-total").textContent = cards.length;
  show("conj-learn"); renderConjLearnCard();
}
function renderConjLearnCard(){
  if(!conjLearnSess) return;
  const flip = document.getElementById("conj-flip");
  flip.classList.remove("flipped");
  const c = conjLearnSess.cards[conjLearnSess.idx];
  document.getElementById("conj-learn-verb").textContent = c.verb;
  document.getElementById("conj-learn-tensename").textContent = c.tensePt;
  document.getElementById("conj-learn-pos").textContent = conjLearnSess.idx + 1;
  // Build table
  const rows = c.persons.map(p => {
    const val = c.cells[p] || "—";
    const label = p === "—" ? "particípio" : p;
    return `<div style="display:flex;justify-content:space-between;gap:14px;padding:4px 0;border-bottom:1px dashed rgba(255,255,255,.06)"><span style="color:var(--muted);min-width:70px">${label}</span><span style="color:var(--text);font-weight:600">${val}</span></div>`;
  }).join("");
  document.getElementById("conj-learn-table").innerHTML = rows;
}
function nextConjLearn(step){
  if(!conjLearnSess) return;
  const n = conjLearnSess.cards.length;
  conjLearnSess.idx = (conjLearnSess.idx + step + n) % n;
  renderConjLearnCard();
}
function renderConjCard(){
  if(!conjSess) return;
  const c = conjSess.queue[conjSess.idx];
  document.getElementById("conj-verb").textContent = c.verb;
  document.getElementById("conj-tense").textContent = c.tensePt;
  document.getElementById("conj-person").textContent = c.person==="—" ? "particípio" : c.person;
  document.getElementById("conj-count").textContent = (conjSess.idx+1) + " / " + conjSess.queue.length;
  const s = document.getElementById("conj-streak"); s.textContent = "streak " + conjSess.streak; s.classList.toggle("zero", conjSess.streak===0);
  document.getElementById("conj-bar").style.width = (conjSess.idx / conjSess.queue.length * 100) + "%";
  const inp = document.getElementById("conj-input");
  inp.value = ""; inp.disabled = false; inp.focus();
  document.getElementById("conj-feedback").innerHTML = "";
  document.getElementById("conj-check").textContent = "Verificar";
  conjSess.checked = false;
}
function checkConj(){
  if(!conjSess) return;
  const c = conjSess.queue[conjSess.idx];
  const inp = document.getElementById("conj-input");
  const guess = inp.value.trim();
  if(conjSess.checked){ nextConj(); return; }
  conjSess.checked = true; conjSess.attempts++;
  const fb = document.getElementById("conj-feedback");
  const ok = conjNorm(guess) === conjNorm(c.answer) ||
             (accentFold(guess) === accentFold(c.answer) && guess.length>0);
  if(ok){
    conjSess.correct++; conjSess.streak++;
    if(conjSess.streak > conjSess.best) conjSess.best = conjSess.streak;
    fb.innerHTML = `<span class="correct">✓ <b>${c.answer}</b></span>`;
    const key = c.verb + "|" + c.tense + "|" + c.person;
    store.langs[LANG].verbs.conjMastered[key] = 1;
    save();
  } else {
    conjSess.streak = 0;
    fb.innerHTML = `<span class="bad">✗ resposta: <b>${c.answer}</b></span>`;
  }
  inp.disabled = true;
  document.getElementById("conj-check").textContent = "Próxima →";
}
function nextConj(){
  if(!conjSess) return;
  conjSess.idx++;
  if(conjSess.idx >= conjSess.queue.length){
    const acc = conjSess.attempts ? Math.round(100*conjSess.correct/conjSess.attempts) : 0;
    document.getElementById("sum-acc").textContent = acc + "%";
    document.getElementById("sum-correct").textContent = conjSess.correct + "/" + conjSess.queue.length;
    document.getElementById("sum-streak").textContent = conjSess.best;
    document.getElementById("sum-title").textContent = acc===100 ? "Conjugação impecável." : acc>=80 ? "Forte." : acc>=50 ? "No caminho." : "Continua.";
    document.getElementById("sum-sub").textContent = `${conjSess.correct} de ${conjSess.queue.length} corretas · maior streak ${conjSess.best}`;
    document.getElementById("sum-promo").style.display = "none";
    document.getElementById("sum-crumb").textContent = "Conjugação · fim";
    show("summary");
    return;
  }
  renderConjCard();
}
// wire buttons
document.addEventListener("click", (e) => {
  const t = e.target.closest("[data-go='conj-setup']");
  if(t){ renderConjSetup(); show("conj-setup"); }
});
document.getElementById("conj-start")?.addEventListener("click", startConj);
document.getElementById("conj-check")?.addEventListener("click", checkConj);
document.getElementById("conj-skip")?.addEventListener("click", nextConj);
document.getElementById("conj-quit")?.addEventListener("click", () => { if(confirm("Sair da rodada?")) show("home"); });
document.getElementById("conj-input")?.addEventListener("keydown", (e) => { if(e.key==="Enter"){ e.preventDefault(); checkConj(); } });
document.getElementById("conj-flip")?.addEventListener("click", () => document.getElementById("conj-flip").classList.toggle("flipped"));
document.getElementById("conj-learn-flip")?.addEventListener("click", (e) => { e.stopPropagation(); document.getElementById("conj-flip").classList.toggle("flipped"); });
document.getElementById("conj-learn-prev")?.addEventListener("click", (e) => { e.stopPropagation(); nextConjLearn(-1); });
document.getElementById("conj-learn-next")?.addEventListener("click", (e) => { e.stopPropagation(); nextConjLearn(1); });
document.getElementById("conj-learn-shuffle")?.addEventListener("click", () => {
  if(!conjLearnSess) return;
  shuffleInPlace(conjLearnSess.cards); conjLearnSess.idx = 0; renderConjLearnCard();
});
document.getElementById("conj-learn-quit")?.addEventListener("click", () => show("home"));
'''
# Insert conjugation JS just before the init block (before setTrack("verbs"); renderHome();)
html = html.replace(
    'setTrack("verbs");\nrenderHome();',
    CONJ_JS + '\nsetTrack("verbs");\nrenderHome();',
    1,
)

# 16f-post: inject ULT_CONJ_PHASE now that '// wire buttons' anchor exists in html.
assert '// wire buttons' in html, "wire buttons anchor missing after CONJ_JS insertion"
html = html.replace('// wire buttons', ULT_CONJ_PHASE + '\n// wire buttons', 1)

# ── 16g. Style hooks for conjugation mode-card + feedback ──
CONJ_CSS = '''
.mode.conjugation{background:linear-gradient(120deg,rgba(90,169,255,.12),rgba(90,169,255,.03));border-color:rgba(90,169,255,.35)}
body.lang-de .mode.conjugation{background:linear-gradient(120deg,rgba(200,162,74,.14),rgba(200,162,74,.03));border-color:rgba(200,162,74,.45)}
body.lang-fr .mode.conjugation{background:linear-gradient(120deg,rgba(255,215,0,.12),rgba(0,85,164,.05));border-color:rgba(255,215,0,.4)}
.feedback .bad{color:var(--bad)}
.feedback .bad b{color:var(--text);font-weight:700}
/* Persistent language switcher — fixed top-right on every screen */
#lang-switch{position:fixed;top:calc(env(safe-area-inset-top, 0px) + 10px);right:calc(env(safe-area-inset-right, 0px) + 10px);z-index:9500;display:flex;gap:0;background:rgba(12,14,18,.85);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.12);border-radius:999px;padding:3px;box-shadow:0 6px 20px rgba(0,0,0,.35)}
#lang-switch .chip{border:0;background:transparent;color:var(--muted);font:600 12px/1 var(--mono, ui-monospace, monospace);letter-spacing:.08em;padding:6px 12px;border-radius:999px;cursor:pointer;transition:background .18s, color .18s}
#lang-switch .chip:hover{color:var(--text)}
#lang-switch .chip.on{background:var(--accent);color:#0a0a0a}
body.lang-de #lang-switch .chip.on{background:var(--accent, #c8a24a);color:#0a0a0a}
body.lang-fr #lang-switch .chip.on{background:#ffd700;color:#003a7a}
/* Nudge home eyebrow away from the switcher */
#screen-home .brand{padding-right:88px}
'''
html = html.replace('</style>', CONJ_CSS + '</style>', 1)

# ── 17. Bump service worker cache name ──
try:
    sw_path = Path(__file__).parent / "sw.js"
    if sw_path.exists():
        sw = sw_path.read_text(encoding="utf-8")
        sw = re.sub(r'const CACHE = "[^"]+";', 'const CACHE = "polyglot-v1";', sw)
        sw_path.write_text(sw, encoding="utf-8")
except Exception as e:
    print(f"[warn] sw.js update skipped: {e}")

DST.write_text(html, encoding="utf-8")
print(f"wrote {DST} ({len(html)} chars)")
