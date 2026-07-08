# Deduplicates NOUNS from _build_nouns.py, pads each level back to 40
# with curated theme-appropriate fresh nouns, then writes noun-data.js.

import json, os, sys

from _build_nouns import NOUNS as RAW

LEVEL_SIZE = 40
LEVEL_COUNT = 25

LEVEL_NAMES = [
    "Time & sequence",
    "People & relations",
    "Body & senses",
    "Home, food & drink",
    "Places & travel",
    "Work, money & tools",
    "Nature & weather",
    "Actions & events",
    "Number, shape & measure",
    "Feelings & states",
    "Being & metaphysics",
    "Mind & consciousness",
    "Ethics & value",
    "Politics & society",
    "Knowledge & truth",
    "Language & meaning",
    "Art & aesthetics",
    "History & culture",
    "Religion & myth",
    "World & science",
    "Phenomenology & hermeneutics",
    "Critical theory & modernity",
    "Psychology & inner life",
    "Economy, law & justice",
    "Metaphysical & theological",
]

# Fresh pool per level index (0-based). Each entry is a full tuple
# (de, art, pl, en_list, fr_list, pt_list). More than enough per level.
POOL = {
    0: [  # Time & sequence
        ("Ära",         "die","Ären",       ["era"],                       ["ère"],                    ["era"]),
        ("Frist",       "die","Fristen",    ["deadline"],                  ["délai"],                  ["prazo"]),
        ("Verzögerung", "die","Verzögerungen",["delay"],                   ["retard"],                 ["atraso"]),
        ("Ewigkeitswert","der","—",         ["eternal value"],             ["valeur éternelle"],       ["valor eterno"]),
    ],
    1: [  # People & relations
        ("Sportler",    "der","Sportler",   ["athlete"],                   ["athlète"],                ["atleta"]),
        ("Verwandte",   "die","Verwandten", ["relative"],                  ["parent"],                 ["parente"]),
        ("Gast",        "der","Gäste",      ["guest"],                     ["invité"],                 ["convidado"]),
        ("Mitbewohner", "der","Mitbewohner",["roommate"],                  ["colocataire"],            ["colega de quarto"]),
    ],
    2: [  # Body & senses
        ("Wimper",      "die","Wimpern",    ["eyelash"],                   ["cil"],                    ["cílio"]),
        ("Knochen",     "der","Knochen",    ["bone"],                      ["os"],                     ["osso"]),
        ("Gelenk",      "das","Gelenke",    ["joint"],                     ["articulation"],           ["articulação"]),
        ("Nerv",        "der","Nerven",     ["nerve"],                     ["nerf"],                   ["nervo"]),
    ],
    3: [  # Home, food & drink
        ("Serviette",   "die","Servietten", ["napkin"],                    ["serviette"],              ["guardanapo"]),
        ("Nudel",       "die","Nudeln",     ["noodle","pasta"],            ["nouille","pâtes"],        ["macarrão"]),
        ("Rezept",      "das","Rezepte",    ["recipe"],                    ["recette"],                ["receita"]),
        ("Speisekammer","die","Speisekammern",["pantry"],                  ["garde-manger"],           ["despensa"]),
    ],
    4: [  # Places & travel
        ("Vorort",      "der","Vororte",    ["suburb"],                    ["banlieue"],               ["subúrbio"]),
        ("Sackgasse",   "die","Sackgassen", ["dead end"],                  ["impasse"],                ["beco sem saída"]),
        ("Passagier",   "der","Passagiere", ["passenger"],                 ["passager"],               ["passageiro"]),
        ("Ankunft",     "die","Ankünfte",   ["arrival"],                   ["arrivée"],                ["chegada"]),
    ],
    5: [  # Work, money & tools
        ("Bezahlung",   "die","Bezahlungen",["payment"],                   ["paiement"],               ["pagamento"]),
        ("Schraubendreher","der","Schraubendreher",["screwdriver"],        ["tournevis"],              ["chave de fenda"]),
        ("Bohrer",      "der","Bohrer",     ["drill"],                     ["perceuse"],               ["furadeira"]),
        ("Lohnzettel",  "der","Lohnzettel", ["payslip"],                   ["fiche de paie"],          ["contracheque"]),
    ],
    6: [  # Nature & weather (need 1)
        ("Küste",       "die","Küsten",     ["coast"],                     ["côte"],                   ["costa"]),
        ("Schlucht",    "die","Schluchten", ["canyon"],                    ["gorge"],                  ["desfiladeiro"]),
        ("Gipfel",      "der","Gipfel",     ["summit"],                    ["sommet"],                 ["cume"]),
        ("Nebelbank",   "die","Nebelbänke", ["fog bank"],                  ["banc de brouillard"],     ["banco de neblina"]),
    ],
    7: [  # Actions & events
        ("Zusammenstoß","der","Zusammenstöße",["collision"],               ["collision"],              ["colisão"]),
        ("Ausbruch",    "der","Ausbrüche",  ["outbreak","eruption"],       ["éruption"],               ["eclosão"]),
        ("Verhandlung", "die","Verhandlungen",["negotiation"],             ["négociation"],            ["negociação"]),
        ("Wandel",      "der","—",          ["transformation","change"],   ["mutation"],               ["transformação"]),
    ],
    8: [  # Number, shape & measure (need 1)
        ("Pyramide",    "die","Pyramiden",  ["pyramid"],                   ["pyramide"],               ["pirâmide"]),
        ("Prozentsatz", "der","Prozentsätze",["percentage"],               ["pourcentage"],            ["porcentagem"]),
        ("Bruchteil",   "der","Bruchteile", ["fraction"],                  ["fraction"],               ["fração"]),
        ("Diagramm",    "das","Diagramme",  ["diagram"],                   ["diagramme"],              ["diagrama"]),
    ],
    9: [  # Feelings & states
        ("Nostalgie",   "die","—",          ["nostalgia"],                 ["nostalgie"],              ["nostalgia"]),
        ("Gelassenheit","die","—",          ["serenity","composure"],      ["sérénité"],               ["serenidade"]),
        ("Erregung",    "die","Erregungen", ["arousal","excitement"],      ["excitation"],             ["excitação"]),
        ("Schwermut",   "die","—",          ["melancholy"],                ["mélancolie"],             ["melancolia"]),
    ],
    10: [  # Being & metaphysics (need 6)
        ("Akzidenz",    "die","Akzidenzien",["accident"],                  ["accident"],               ["acidente"]),
        ("Attribut",    "das","Attribute",  ["attribute"],                 ["attribut"],               ["atributo"]),
        ("Entität",     "die","Entitäten",  ["entity"],                    ["entité"],                 ["entidade"]),
        ("Instanz",     "die","Instanzen",  ["instance"],                  ["instance"],               ["instância"]),
        ("Modus",       "der","Modi",       ["mode"],                      ["mode"],                   ["modo"]),
        ("Kausalität",  "die","—",          ["causality"],                 ["causalité"],              ["causalidade"]),
        ("Weltgrund",   "der","—",          ["ground of being"],           ["fondement du monde"],     ["fundamento do mundo"]),
        ("Urgrund",     "der","—",          ["primal ground"],             ["fond originel"],          ["fundamento primordial"]),
    ],
    11: [  # Mind & consciousness (need 1)
        ("Introspektion","die","—",         ["introspection"],             ["introspection"],          ["introspecção"]),
        ("Reflexivität","die","—",          ["reflexivity"],               ["réflexivité"],            ["reflexividade"]),
        ("Selbstbezug", "der","—",          ["self-reference"],            ["auto-référence"],         ["autorreferência"]),
        ("Assoziation", "die","Assoziationen",["association"],             ["association"],            ["associação"]),
    ],
    12: [  # Ethics & value (need 1)
        ("Norm",        "die","Normen",     ["norm"],                      ["norme"],                  ["norma"]),
        ("Pflichtgefühl","das","—",         ["sense of duty"],             ["sens du devoir"],         ["senso de dever"]),
        ("Wohlwollen",  "das","—",          ["benevolence"],               ["bienveillance"],          ["benevolência"]),
        ("Barmherzigkeit","die","—",        ["mercy"],                     ["miséricorde"],            ["misericórdia"]),
    ],
    13: [  # Politics & society (need 4)
        ("Bürgerrecht", "das","Bürgerrechte",["civil right"],              ["droit civique"],          ["direito civil"]),
        ("Legitimität", "die","—",          ["legitimacy"],                ["légitimité"],             ["legitimidade"]),
        ("Parlament",   "das","Parlamente", ["parliament"],                ["parlement"],              ["parlamento"]),
        ("Regierung",   "die","Regierungen",["government"],                ["gouvernement"],           ["governo"]),
        ("Opposition",  "die","Oppositionen",["opposition"],               ["opposition"],             ["oposição"]),
        ("Bündnis",     "das","Bündnisse",  ["alliance"],                  ["alliance"],               ["aliança"]),
        ("Verwaltung",  "die","Verwaltungen",["administration"],           ["administration"],         ["administração"]),
    ],
    14: [  # Knowledge & truth (need 5)
        ("Doxa",        "die","—",          ["opinion","doxa"],            ["opinion","doxa"],         ["doxa"]),
        ("Evidenz",     "die","—",          ["evidence"],                  ["évidence"],               ["evidência"]),
        ("Inferenz",    "die","Inferenzen", ["inference"],                 ["inférence"],              ["inferência"]),
        ("Widerlegung", "die","Widerlegungen",["refutation"],              ["réfutation"],             ["refutação"]),
        ("Behauptung",  "die","Behauptungen",["assertion","claim"],        ["affirmation"],            ["afirmação"]),
        ("Falsifikation","die","Falsifikationen",["falsification"],        ["falsification"],          ["falseamento"]),
        ("Verifikation","die","Verifikationen",["verification"],           ["vérification"],           ["verificação"]),
        ("Erkenntnis",  "die","Erkenntnisse",["cognition","insight"],      ["connaissance"],           ["cognição"]),
    ],
    15: [  # Language & meaning (need 3)
        ("Grammatik",   "die","Grammatiken",["grammar"],                   ["grammaire"],              ["gramática"]),
        ("Silbe",       "die","Silben",     ["syllable"],                  ["syllabe"],                ["sílaba"]),
        ("Ausdruck",    "der","Ausdrücke",  ["expression"],                ["expression"],             ["expressão"]),
        ("Semiotik",    "die","—",          ["semiotics"],                 ["sémiotique"],             ["semiótica"]),
        ("Konnotation", "die","Konnotationen",["connotation"],             ["connotation"],            ["conotação"]),
    ],
    16: [  # Art & aesthetics (need 4)
        ("Ornament",    "das","Ornamente",  ["ornament"],                  ["ornement"],               ["ornamento"]),
        ("Ballade",     "die","Balladen",   ["ballad"],                    ["ballade"],                ["balada"]),
        ("Sonate",      "die","Sonaten",    ["sonata"],                    ["sonate"],                 ["sonata"]),
        ("Palette",     "die","Paletten",   ["palette"],                   ["palette"],                ["paleta"]),
        ("Perspektive", "die","Perspektiven",["perspective"],              ["perspective"],            ["perspectiva"]),
        ("Ästhetik",    "die","Ästhetiken", ["aesthetics"],                ["esthétique"],             ["estética"]),
        ("Choreografie","die","Choreografien",["choreography"],            ["chorégraphie"],           ["coreografia"]),
    ],
    17: [  # History & culture (need 8)
        ("Aufstand",    "der","Aufstände",  ["uprising"],                  ["soulèvement"],            ["revolta"]),
        ("Chronik",     "die","Chroniken",  ["chronicle"],                 ["chronique"],              ["crônica"]),
        ("Dynastie",    "die","Dynastien",  ["dynasty"],                   ["dynastie"],               ["dinastia"]),
        ("Feudalismus", "der","—",          ["feudalism"],                 ["féodalisme"],             ["feudalismo"]),
        ("Kolonie",     "die","Kolonien",   ["colony"],                    ["colonie"],                ["colônia"]),
        ("Bündnisvertrag","der","Bündnisverträge",["treaty"],              ["traité"],                 ["tratado"]),
        ("Reich",       "das","Reiche",     ["empire","realm"],            ["empire"],                 ["império"]),
        ("Kaiser",      "der","Kaiser",     ["emperor"],                   ["empereur"],               ["imperador"]),
        ("König",       "der","Könige",     ["king"],                      ["roi"],                    ["rei"]),
        ("Sitte",       "die","Sitten",     ["custom","mores"],            ["moeurs"],                 ["costume"]),
        ("Brauchtum",   "das","—",          ["folk custom"],               ["coutume"],                ["tradições"]),
        ("Zeugnis",     "das","Zeugnisse",  ["testimony"],                 ["témoignage"],             ["testemunho"]),
    ],
    18: [  # Religion & myth (need 4)
        ("Mönch",       "der","Mönche",     ["monk"],                      ["moine"],                  ["monge"]),
        ("Nonne",       "die","Nonnen",     ["nun"],                       ["nonne"],                  ["freira"]),
        ("Pilger",      "der","Pilger",     ["pilgrim"],                   ["pèlerin"],                ["peregrino"]),
        ("Wunder",      "das","Wunder",     ["miracle"],                   ["miracle"],                ["milagre"]),
        ("Legende",     "die","Legenden",   ["legend"],                    ["légende"],                ["lenda"]),
        ("Heiliger",    "der","Heilige",    ["saint"],                     ["saint"],                  ["santo"]),
        ("Reliquie",    "die","Reliquien",  ["relic"],                     ["relique"],                ["relíquia"]),
        ("Segen",       "der","Segen",      ["blessing"],                  ["bénédiction"],            ["bênção"]),
    ],
    19: [  # World & science (need 4)
        ("Genom",       "das","Genome",     ["genome"],                    ["génome"],                 ["genoma"]),
        ("Teilchen",    "das","Teilchen",   ["particle"],                  ["particule"],              ["partícula"]),
        ("Gravitation", "die","—",          ["gravity"],                   ["gravitation"],            ["gravidade"]),
        ("Formel",      "die","Formeln",    ["formula"],                   ["formule"],                ["fórmula"]),
        ("Isotop",      "das","Isotope",    ["isotope"],                   ["isotope"],                ["isótopo"]),
    ],
    20: [  # Phenomenology & hermeneutics (need 7)
        ("Intention",   "die","Intentionen",["intention"],                 ["intention"],              ["intenção"]),
        ("Gestalt",     "die","Gestalten",  ["gestalt","shape"],           ["gestalt","forme"],        ["gestalt","forma"]),
        ("Reduktion",   "die","Reduktionen",["reduction"],                 ["réduction"],              ["redução"]),
        ("Intersubjektivität","die","—",    ["intersubjectivity"],         ["intersubjectivité"],      ["intersubjetividade"]),
        ("Präreflexivität","die","—",       ["pre-reflexivity"],           ["pré-réflexivité"],        ["pré-reflexividade"]),
        ("Leiblichkeit","die","—",          ["embodiment"],                ["corporéité"],             ["corporeidade"]),
        ("Vorverständnis","das","—",        ["pre-understanding"],         ["pré-compréhension"],      ["pré-compreensão"]),
        ("Hermeneutik", "die","—",          ["hermeneutics"],              ["herméneutique"],          ["hermenêutica"]),
        ("Verweisung",  "die","Verweisungen",["reference","referral"],     ["renvoi"],                 ["remissão"]),
        ("Zuhandenheit","die","—",          ["readiness-to-hand"],         ["être-sous-la-main"],      ["ser-à-mão"]),
        ("Vorhandenheit","die","—",         ["presence-at-hand"],          ["être-là"],                ["ser-em-presença"]),
        ("Verstehen",   "das","—",          ["understanding"],             ["compréhension"],          ["compreensão"]),
        ("Wirkungsgeschichte","die","—",    ["effective history"],         ["histoire des effets"],    ["história efetual"]),
        ("Horizontverschmelzung","die","—", ["fusion of horizons"],        ["fusion des horizons"],    ["fusão de horizontes"]),
        ("Applikation", "die","Applikationen",["application"],             ["application"],            ["aplicação"]),
        ("Intentionalitätsakt","der","Intentionalitätsakte",["intentional act"],["acte intentionnel"], ["ato intencional"]),
        ("Erscheinungsweise","die","Erscheinungsweisen",["mode of appearance"],["mode d'apparition"], ["modo de aparição"]),
    ],
    21: [  # Critical theory & modernity (need 11)
        ("Massenkultur","die","—",          ["mass culture"],              ["culture de masse"],       ["cultura de massa"]),
        ("Basis",       "die","Basen",      ["base"],                      ["base"],                   ["base"]),
        ("Überbau",     "der","—",          ["superstructure"],            ["superstructure"],         ["superestrutura"]),
        ("Reifizierung","die","—",          ["reification"],               ["réification"],            ["reificação"]),
        ("Gouvernementalität","die","—",    ["governmentality"],           ["gouvernementalité"],      ["governamentalidade"]),
        ("Panoptismus", "der","—",          ["panopticism"],               ["panoptisme"],             ["panoptismo"]),
        ("Simulakrum",  "das","Simulakra",  ["simulacrum"],                ["simulacre"],              ["simulacro"]),
        ("Kulturindustrie","die","—",       ["culture industry"],          ["industrie culturelle"],   ["indústria cultural"]),
        ("Verwaltete Welt","die","—",       ["administered world"],        ["monde administré"],       ["mundo administrado"]),
        ("Instrumentelle Vernunft","die","—",["instrumental reason"],      ["raison instrumentale"],   ["razão instrumental"]),
        ("Spektakel",   "das","—",          ["spectacle"],                 ["spectacle"],              ["espetáculo"]),
        ("Simulation",  "die","Simulationen",["simulation"],               ["simulation"],             ["simulação"]),
        ("Hyperrealität","die","—",         ["hyperreality"],              ["hyperréalité"],           ["hiperrealidade"]),
        ("Rhizom",      "das","Rhizome",    ["rhizome"],                   ["rhizome"],                ["rizoma"]),
    ],
    22: [  # Psychology & inner life (need 4)
        ("Traumdeutung","die","—",          ["dream interpretation"],      ["interprétation des rêves"],["interpretação dos sonhos"]),
        ("Projektion",  "die","Projektionen",["projection"],               ["projection"],             ["projeção"]),
        ("Sublimierung","die","Sublimierungen",["sublimation"],            ["sublimation"],            ["sublimação"]),
        ("Ich",         "das","—",          ["ego","I"],                   ["moi","ego"],              ["ego","eu"]),
        ("Über-Ich",    "das","—",          ["super-ego"],                 ["surmoi"],                 ["superego"]),
        ("Es",          "das","—",          ["id"],                        ["ça"],                     ["id"]),
        ("Libido",      "die","—",          ["libido"],                    ["libido"],                 ["libido"]),
        ("Katharsis",   "die","—",          ["catharsis"],                 ["catharsis"],              ["catarse"]),
    ],
    23: [  # Economy, law & justice (need 11)
        ("Bilanz",      "die","Bilanzen",   ["balance sheet"],             ["bilan"],                  ["balanço"]),
        ("Aktie",       "die","Aktien",     ["share","stock"],             ["action"],                 ["ação"]),
        ("Konjunktur",  "die","Konjunkturen",["economic cycle"],           ["conjoncture"],            ["conjuntura"]),
        ("Berufung",    "die","Berufungen", ["appeal","calling"],          ["appel","vocation"],       ["apelação","vocação"]),
        ("Rechtsprechung","die","—",        ["jurisdiction","case law"],   ["jurisprudence"],          ["jurisprudência"]),
        ("Angebot",     "das","Angebote",   ["supply","offer"],            ["offre"],                  ["oferta"]),
        ("Nachfrage",   "die","—",          ["demand"],                    ["demande"],                ["procura"]),
        ("Wettbewerb",  "der","Wettbewerbe",["competition"],               ["concurrence"],            ["concorrência"]),
        ("Monopol",     "das","Monopole",   ["monopoly"],                  ["monopole"],               ["monopólio"]),
        ("Handel",      "der","—",          ["trade"],                     ["commerce"],               ["comércio"]),
        ("Vermögen",    "das","Vermögen",   ["wealth","assets"],           ["fortune","patrimoine"],   ["patrimônio"]),
        ("Erbschaft",   "die","Erbschaften",["inheritance"],               ["héritage"],               ["herança"]),
        ("Steuersatz",  "der","Steuersätze",["tax rate"],                  ["taux d'imposition"],      ["alíquota"]),
        ("Zoll",        "der","Zölle",      ["tariff","customs"],          ["douane"],                 ["taxa alfandegária"]),
        ("Ertrag",      "der","Erträge",    ["yield","proceeds"],          ["rendement"],              ["rendimento"]),
        ("Verlust",     "der","Verluste",   ["loss"],                      ["perte"],                  ["perda"]),
        ("Gewinn",      "der","Gewinne",    ["profit"],                    ["bénéfice"],               ["lucro"]),
        ("Schadensersatz","der","—",        ["damages","compensation"],    ["dommages-intérêts"],      ["indenização"]),
    ],
    24: [  # Metaphysical & theological (need 4)
        ("Essenz",      "die","Essenzen",   ["essence"],                   ["essence"],                ["essência"]),
        ("Monade",      "die","Monaden",    ["monad"],                     ["monade"],                 ["mônada"]),
        ("Vorsehung",   "die","—",          ["providence"],                ["providence"],             ["providência"]),
        ("Erschaffung", "die","—",          ["creation"],                  ["création"],               ["criação"]),
        ("Vollkommenheit","die","—",        ["perfection"],                ["perfection"],             ["perfeição"]),
        ("Allmacht",    "die","—",          ["omnipotence"],               ["omnipotence"],            ["onipotência"]),
    ],
}


def level_of(pos):
    return min(pos // LEVEL_SIZE, LEVEL_COUNT - 1)


def build():
    # Split RAW into levels using original positions.
    levels = [[] for _ in range(LEVEL_COUNT)]
    for i, row in enumerate(RAW):
        levels[level_of(i)].append(row)

    # Deduplicate globally (first-seen wins), preserving level of first hit.
    seen = set()
    clean_levels = [[] for _ in range(LEVEL_COUNT)]
    for li, lvl in enumerate(levels):
        for row in lvl:
            de = row[0]
            if de in seen:
                continue
            seen.add(de)
            clean_levels[li].append(row)

    # Pad each level back to LEVEL_SIZE from its pool.
    for li in range(LEVEL_COUNT):
        need = LEVEL_SIZE - len(clean_levels[li])
        if need <= 0:
            continue
        pool = POOL.get(li, [])
        added = 0
        for row in pool:
            if added >= need:
                break
            de = row[0]
            if de in seen:
                continue
            clean_levels[li].append(row)
            seen.add(de)
            added += 1
        if added < need:
            print(f"WARN level {li+1} ({LEVEL_NAMES[li]}): need {need}, only added {added}", file=sys.stderr)

    # Flatten and audit.
    out = []
    for lvl in clean_levels:
        out.extend(lvl)
    return out, clean_levels


def esc(s):
    return json.dumps(s, ensure_ascii=False)


def to_js(rows, clean_levels):
    lines = ["// generated by _finalize_nouns.py — do not edit"]
    lines.append("window.NOUNS_DATA = [")
    for row in rows:
        de, art, pl, en, fr, pt = row
        en_s = "[" + ",".join(esc(w) for w in en) + "]"
        fr_s = "[" + ",".join(esc(w) for w in fr) + "]"
        pt_s = "[" + ",".join(esc(w) for w in pt) + "]"
        lines.append(f'  {{de:{esc(de)},art:{esc(art)},pl:{esc(pl)},en:{en_s},fr:{fr_s},pt:{pt_s}}},')
    lines.append("];")
    # level index for the UI (start position of each level in the flat list)
    starts = []
    running = 0
    for lvl in clean_levels:
        starts.append(running)
        running += len(lvl)
    starts.append(running)  # sentinel end
    names = [esc(n) for n in LEVEL_NAMES]
    lines.append("window.NOUN_LEVELS = {")
    lines.append(f"  starts: [{','.join(str(s) for s in starts)}],")
    lines.append(f"  names: [{','.join(names)}]")
    lines.append("};")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    rows, clean_levels = build()
    # audit
    seen = {}
    dupes = []
    for i, r in enumerate(rows):
        if r[0] in seen:
            dupes.append((r[0], seen[r[0]], i))
        else:
            seen[r[0]] = i
    print(f"total nouns: {len(rows)}")
    print(f"unique headwords: {len(seen)}")
    print(f"duplicates: {len(dupes)}")
    for li, lvl in enumerate(clean_levels):
        print(f"  L{li+1:>2} {LEVEL_NAMES[li]:<32} = {len(lvl)}")
    # validate fields
    bad = []
    for r in rows:
        de, art, pl, en, fr, pt = r
        if art not in ("der", "die", "das"):
            bad.append(("bad art", de, art))
        if not en or not fr or not pt:
            bad.append(("empty translation", de))
        if not de or not pl:
            bad.append(("empty de/pl", de))
    if bad:
        print("VALIDATION ISSUES:")
        for b in bad:
            print(" ", b)
    else:
        print("validation: OK")
    here = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(here, "noun-data.js")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(to_js(rows, clean_levels))
    print(f"wrote {out_path}")
