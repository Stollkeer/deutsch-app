# Builds noun-data.js from a curated list of 1000 German nouns.
# Fields per noun: (de, art, pl, en_list, fr_list, pt_list)
# - de:    German singular (capitalised)
# - art:   der | die | das
# - pl:    plural form (bare, without "die"), or "—" for singularia tantum
# - en/fr/pt: primary translation first; alternatives after; kept short

# 25 levels x 40 nouns = 1000.
# Levels 1–10: everyday high-frequency vocabulary.
# Levels 11–25: humanities/philosophy — being, mind, ethics, politics,
#               knowledge, language, art, history, religion, science,
#               phenomenology, critical theory, psychology, economy/law,
#               metaphysical & theological.

NOUNS = [

# ============================================================
# LEVEL 1 — Time & sequence
# ============================================================
("Zeit",         "die","Zeiten",       ["time"],                     ["temps"],                 ["tempo"]),
("Jahr",         "das","Jahre",        ["year"],                     ["année","an"],            ["ano"]),
("Tag",          "der","Tage",         ["day"],                      ["jour"],                  ["dia"]),
("Stunde",       "die","Stunden",      ["hour"],                     ["heure"],                 ["hora"]),
("Woche",        "die","Wochen",       ["week"],                     ["semaine"],               ["semana"]),
("Monat",        "der","Monate",       ["month"],                    ["mois"],                  ["mês"]),
("Minute",       "die","Minuten",      ["minute"],                   ["minute"],                ["minuto"]),
("Sekunde",      "die","Sekunden",     ["second"],                   ["seconde"],               ["segundo"]),
("Moment",       "der","Momente",      ["moment"],                   ["moment","instant"],      ["momento"]),
("Augenblick",   "der","Augenblicke",  ["instant","moment"],         ["instant"],               ["instante"]),
("Anfang",       "der","Anfänge",      ["beginning","start"],        ["début","commencement"],  ["começo","início"]),
("Ende",         "das","Enden",        ["end"],                      ["fin"],                   ["fim"]),
("Zukunft",      "die","—",            ["future"],                   ["avenir","futur"],        ["futuro"]),
("Vergangenheit","die","—",            ["past"],                     ["passé"],                 ["passado"]),
("Gegenwart",    "die","—",            ["present"],                  ["présent"],               ["presente"]),
("Alter",        "das","—",            ["age"],                      ["âge"],                   ["idade"]),
("Nacht",        "die","Nächte",       ["night"],                    ["nuit"],                  ["noite"]),
("Morgen",       "der","Morgen",       ["morning"],                  ["matin"],                 ["manhã"]),
("Abend",        "der","Abende",       ["evening"],                  ["soir"],                  ["noite","tarde"]),
("Mittag",       "der","Mittage",      ["noon","midday"],            ["midi"],                  ["meio-dia"]),
("Zeitpunkt",    "der","Zeitpunkte",   ["point in time"],            ["moment","instant"],      ["momento","instante"]),
("Dauer",        "die","—",            ["duration"],                 ["durée"],                 ["duração"]),
("Ewigkeit",     "die","Ewigkeiten",   ["eternity"],                 ["éternité"],              ["eternidade"]),
("Epoche",       "die","Epochen",      ["epoch","era"],              ["époque"],                ["época"]),
("Ära",          "die","Ären",         ["era","age"],                ["ère"],                   ["era"]),
("Frist",        "die","Fristen",      ["deadline","time limit"],    ["délai","échéance"],      ["prazo"]),
("Termin",       "der","Termine",      ["appointment","date"],       ["rendez-vous"],           ["compromisso","hora marcada"]),
("Uhr",          "die","Uhren",        ["clock","watch"],            ["horloge","montre"],      ["relógio"]),
("Datum",        "das","Daten",        ["date"],                     ["date"],                  ["data"]),
("Kalender",     "der","Kalender",     ["calendar"],                 ["calendrier"],            ["calendário"]),
("Jahrhundert",  "das","Jahrhunderte", ["century"],                  ["siècle"],                ["século"]),
("Jahrzehnt",    "das","Jahrzehnte",   ["decade"],                   ["décennie"],              ["década"]),
("Sommer",       "der","Sommer",       ["summer"],                   ["été"],                   ["verão"]),
("Winter",       "der","Winter",       ["winter"],                   ["hiver"],                 ["inverno"]),
("Frühling",     "der","Frühlinge",    ["spring"],                   ["printemps"],             ["primavera"]),
("Herbst",       "der","Herbste",      ["autumn","fall"],            ["automne"],               ["outono"]),
("Wochenende",   "das","Wochenenden",  ["weekend"],                  ["week-end"],              ["fim de semana"]),
("Rhythmus",     "der","Rhythmen",     ["rhythm"],                   ["rythme"],                ["ritmo"]),
("Zeitalter",    "das","Zeitalter",    ["age","era"],                ["âge","ère"],             ["era","idade"]),
("Weile",        "die","Weilen",       ["while","little time"],      ["moment","temps"],        ["momento","tempo"]),

# ============================================================
# LEVEL 2 — People & relations
# ============================================================
("Mensch",       "der","Menschen",     ["human","person"],           ["être humain","homme"],   ["ser humano","pessoa"]),
("Frau",         "die","Frauen",       ["woman"],                    ["femme"],                 ["mulher"]),
("Mann",         "der","Männer",       ["man","husband"],            ["homme","mari"],          ["homem","marido"]),
("Kind",         "das","Kinder",       ["child"],                    ["enfant"],                ["criança"]),
("Junge",        "der","Jungen",       ["boy"],                      ["garçon"],                ["menino"]),
("Mädchen",      "das","Mädchen",      ["girl"],                     ["fille"],                 ["menina"]),
("Familie",      "die","Familien",     ["family"],                   ["famille"],               ["família"]),
("Vater",        "der","Väter",        ["father"],                   ["père"],                  ["pai"]),
("Mutter",       "die","Mütter",       ["mother"],                   ["mère"],                  ["mãe"]),
("Sohn",         "der","Söhne",        ["son"],                      ["fils"],                  ["filho"]),
("Tochter",      "die","Töchter",      ["daughter"],                 ["fille"],                 ["filha"]),
("Bruder",       "der","Brüder",       ["brother"],                  ["frère"],                 ["irmão"]),
("Schwester",    "die","Schwestern",   ["sister"],                   ["sœur"],                  ["irmã"]),
("Eltern",       "die","—",            ["parents"],                  ["parents"],               ["pais"]),
("Freund",       "der","Freunde",      ["friend","boyfriend"],       ["ami","copain"],          ["amigo","namorado"]),
("Freundin",     "die","Freundinnen",  ["friend","girlfriend"],      ["amie","copine"],         ["amiga","namorada"]),
("Nachbar",      "der","Nachbarn",     ["neighbor"],                 ["voisin"],                ["vizinho"]),
("Kollege",      "der","Kollegen",     ["colleague"],                ["collègue"],              ["colega"]),
("Person",       "die","Personen",     ["person"],                   ["personne"],              ["pessoa"]),
("Leute",        "die","—",            ["people"],                   ["gens","personnes"],      ["pessoas","gente"]),
("Gruppe",       "die","Gruppen",      ["group"],                    ["groupe"],                ["grupo"]),
("Paar",         "das","Paare",        ["couple","pair"],            ["couple","paire"],        ["casal","par"]),
("Nachbarschaft","die","Nachbarschaften",["neighborhood"],           ["voisinage","quartier"],  ["vizinhança","bairro"]),
("Bekannte",     "der","Bekannten",    ["acquaintance"],             ["connaissance"],          ["conhecido"]),
("Fremde",       "der","Fremden",      ["stranger","foreigner"],     ["étranger","inconnu"],    ["estranho","estrangeiro"]),
("Verwandte",    "der","Verwandten",   ["relative"],                 ["parent","proche"],       ["parente"]),
("Gast",         "der","Gäste",        ["guest"],                    ["invité","hôte"],         ["convidado","hóspede"]),
("Gastgeber",    "der","Gastgeber",    ["host"],                     ["hôte"],                  ["anfitrião"]),
("Chef",         "der","Chefs",        ["boss"],                     ["chef","patron"],         ["chefe"]),
("Team",         "das","Teams",        ["team"],                     ["équipe"],                ["equipe","time"]),
("Gesellschaft", "die","Gesellschaften",["society","company"],       ["société"],               ["sociedade"]),
("Gemeinschaft", "die","Gemeinschaften",["community"],               ["communauté"],            ["comunidade"]),
("Ehe",          "die","Ehen",         ["marriage"],                 ["mariage"],               ["casamento"]),
("Hochzeit",     "die","Hochzeiten",   ["wedding"],                  ["mariage","noces"],       ["casamento","boda"]),
("Liebe",        "die","—",            ["love"],                     ["amour"],                 ["amor"]),
("Geburt",       "die","Geburten",     ["birth"],                    ["naissance"],             ["nascimento"]),
("Tod",          "der","Todesfälle",   ["death"],                    ["mort"],                  ["morte"]),
("Kindheit",     "die","—",            ["childhood"],                ["enfance"],               ["infância"]),
("Jugend",       "die","—",            ["youth"],                    ["jeunesse"],              ["juventude"]),
("Beziehung",    "die","Beziehungen",  ["relationship"],             ["relation"],              ["relação","relacionamento"]),

# ============================================================
# LEVEL 3 — Body & senses
# ============================================================
("Körper",       "der","Körper",       ["body"],                     ["corps"],                 ["corpo"]),
("Kopf",         "der","Köpfe",        ["head"],                     ["tête"],                  ["cabeça"]),
("Gesicht",      "das","Gesichter",    ["face"],                     ["visage","figure"],       ["rosto","cara"]),
("Auge",         "das","Augen",        ["eye"],                      ["œil"],                   ["olho"]),
("Ohr",          "das","Ohren",        ["ear"],                      ["oreille"],               ["orelha","ouvido"]),
("Nase",         "die","Nasen",        ["nose"],                     ["nez"],                   ["nariz"]),
("Mund",         "der","Münder",       ["mouth"],                    ["bouche"],                ["boca"]),
("Zahn",         "der","Zähne",        ["tooth"],                    ["dent"],                  ["dente"]),
("Zunge",        "die","Zungen",       ["tongue","language"],        ["langue"],                ["língua"]),
("Hals",         "der","Hälse",        ["neck","throat"],            ["cou","gorge"],           ["pescoço","garganta"]),
("Arm",          "der","Arme",         ["arm"],                      ["bras"],                  ["braço"]),
("Hand",         "die","Hände",        ["hand"],                     ["main"],                  ["mão"]),
("Finger",       "der","Finger",       ["finger"],                   ["doigt"],                 ["dedo"]),
("Bein",         "das","Beine",        ["leg"],                      ["jambe"],                 ["perna"]),
("Fuß",          "der","Füße",         ["foot"],                     ["pied"],                  ["pé"]),
("Rücken",       "der","Rücken",       ["back"],                     ["dos"],                   ["costas"]),
("Bauch",        "der","Bäuche",       ["belly","stomach"],          ["ventre","estomac"],      ["barriga","estômago"]),
("Herz",         "das","Herzen",       ["heart"],                    ["cœur"],                  ["coração"]),
("Blut",         "das","—",            ["blood"],                    ["sang"],                  ["sangue"]),
("Haut",         "die","Häute",        ["skin"],                     ["peau"],                  ["pele"]),
("Haar",         "das","Haare",        ["hair"],                     ["cheveu","poil"],         ["cabelo","pelo"]),
("Knochen",      "der","Knochen",      ["bone"],                     ["os"],                    ["osso"]),
("Muskel",       "der","Muskeln",      ["muscle"],                   ["muscle"],                ["músculo"]),
("Gehirn",       "das","Gehirne",      ["brain"],                    ["cerveau"],               ["cérebro"]),
("Nerv",         "der","Nerven",       ["nerve"],                    ["nerf"],                  ["nervo"]),
("Stimme",       "die","Stimmen",      ["voice"],                    ["voix"],                  ["voz"]),
("Blick",        "der","Blicke",       ["look","glance"],            ["regard"],                ["olhar"]),
("Gehör",        "das","—",            ["hearing"],                  ["ouïe"],                  ["audição"]),
("Geschmack",    "der","Geschmäcker",  ["taste"],                    ["goût"],                  ["gosto","sabor"]),
("Geruch",       "der","Gerüche",      ["smell","odor"],             ["odeur"],                 ["cheiro","odor"]),
("Berührung",    "die","Berührungen",  ["touch"],                    ["toucher","contact"],     ["toque","contato"]),
("Schmerz",      "der","Schmerzen",    ["pain"],                     ["douleur"],               ["dor"]),
("Hunger",       "der","—",            ["hunger"],                   ["faim"],                  ["fome"]),
("Durst",        "der","—",            ["thirst"],                   ["soif"],                  ["sede"]),
("Müdigkeit",    "die","—",            ["tiredness","fatigue"],      ["fatigue"],               ["cansaço"]),
("Atem",         "der","—",            ["breath"],                   ["souffle","haleine"],     ["respiração","fôlego"]),
("Schlaf",       "der","—",            ["sleep"],                    ["sommeil"],               ["sono"]),
("Traum",        "der","Träume",       ["dream"],                    ["rêve"],                  ["sonho"]),
("Wunde",        "die","Wunden",       ["wound"],                    ["blessure","plaie"],      ["ferida"]),
("Gesundheit",   "die","—",            ["health"],                   ["santé"],                 ["saúde"]),

# ============================================================
# LEVEL 4 — Home, food & drink
# ============================================================
("Haus",         "das","Häuser",       ["house"],                    ["maison"],                ["casa"]),
("Wohnung",      "die","Wohnungen",    ["apartment","flat"],         ["appartement"],           ["apartamento"]),
("Zimmer",       "das","Zimmer",       ["room"],                     ["chambre","pièce"],       ["quarto","cômodo"]),
("Küche",        "die","Küchen",       ["kitchen"],                  ["cuisine"],               ["cozinha"]),
("Bad",          "das","Bäder",        ["bathroom","bath"],          ["salle de bain","bain"],  ["banheiro","banho"]),
("Bett",         "das","Betten",       ["bed"],                      ["lit"],                   ["cama"]),
("Tisch",        "der","Tische",       ["table"],                    ["table"],                 ["mesa"]),
("Stuhl",        "der","Stühle",       ["chair"],                    ["chaise"],                ["cadeira"]),
("Tür",          "die","Türen",        ["door"],                     ["porte"],                 ["porta"]),
("Fenster",      "das","Fenster",      ["window"],                   ["fenêtre"],               ["janela"]),
("Wand",         "die","Wände",        ["wall"],                     ["mur"],                   ["parede"]),
("Boden",        "der","Böden",        ["floor","ground"],           ["sol","plancher"],        ["chão","piso"]),
("Dach",         "das","Dächer",       ["roof"],                     ["toit"],                  ["telhado"]),
("Licht",        "das","Lichter",      ["light"],                    ["lumière"],               ["luz"]),
("Lampe",        "die","Lampen",       ["lamp"],                     ["lampe"],                 ["lâmpada","luminária"]),
("Schlüssel",    "der","Schlüssel",    ["key"],                      ["clé","clef"],            ["chave"]),
("Bild",         "das","Bilder",       ["picture","image"],          ["image","tableau"],       ["imagem","quadro"]),
("Spiegel",      "der","Spiegel",      ["mirror"],                   ["miroir"],                ["espelho"]),
("Buch",         "das","Bücher",       ["book"],                     ["livre"],                 ["livro"]),
("Zeitung",      "die","Zeitungen",    ["newspaper"],                ["journal"],               ["jornal"]),
("Essen",        "das","—",            ["food","meal"],              ["nourriture","repas"],    ["comida","refeição"]),
("Brot",         "das","Brote",        ["bread"],                    ["pain"],                  ["pão"]),
("Fleisch",      "das","—",            ["meat"],                     ["viande"],                ["carne"]),
("Fisch",        "der","Fische",       ["fish"],                     ["poisson"],               ["peixe"]),
("Ei",           "das","Eier",         ["egg"],                      ["œuf"],                   ["ovo"]),
("Milch",        "die","—",            ["milk"],                     ["lait"],                  ["leite"]),
("Käse",         "der","Käse",         ["cheese"],                   ["fromage"],               ["queijo"]),
("Butter",       "die","—",            ["butter"],                   ["beurre"],                ["manteiga"]),
("Obst",         "das","—",            ["fruit"],                    ["fruits"],                ["fruta"]),
("Gemüse",       "das","—",            ["vegetables"],               ["légumes"],               ["verdura","legume"]),
("Wasser",       "das","Wässer",       ["water"],                    ["eau"],                   ["água"]),
("Kaffee",       "der","Kaffees",      ["coffee"],                   ["café"],                  ["café"]),
("Tee",          "der","Tees",         ["tea"],                      ["thé"],                   ["chá"]),
("Wein",         "der","Weine",        ["wine"],                     ["vin"],                   ["vinho"]),
("Bier",         "das","Biere",        ["beer"],                     ["bière"],                 ["cerveja"]),
("Zucker",       "der","—",            ["sugar"],                    ["sucre"],                 ["açúcar"]),
("Salz",         "das","Salze",        ["salt"],                     ["sel"],                   ["sal"]),
("Suppe",        "die","Suppen",       ["soup"],                     ["soupe"],                 ["sopa"]),
("Kuchen",       "der","Kuchen",       ["cake"],                     ["gâteau"],                ["bolo"]),
("Mahlzeit",     "die","Mahlzeiten",   ["meal"],                     ["repas"],                 ["refeição"]),

# ============================================================
# LEVEL 5 — Places & travel
# ============================================================
("Stadt",        "die","Städte",       ["city","town"],              ["ville"],                 ["cidade"]),
("Land",         "das","Länder",       ["country","land"],           ["pays","terre"],          ["país","terra"]),
("Dorf",         "das","Dörfer",       ["village"],                  ["village"],               ["vila","aldeia"]),
("Straße",       "die","Straßen",      ["street","road"],            ["rue","route"],           ["rua","estrada"]),
("Weg",          "der","Wege",         ["way","path"],               ["chemin","voie"],         ["caminho","via"]),
("Platz",        "der","Plätze",       ["place","square"],           ["place","espace"],        ["lugar","praça"]),
("Ort",          "der","Orte",         ["place","location"],         ["lieu","endroit"],        ["lugar","local"]),
("Region",       "die","Regionen",     ["region"],                   ["région"],                ["região"]),
("Welt",         "die","Welten",       ["world"],                    ["monde"],                 ["mundo"]),
("Erde",         "die","—",            ["earth"],                    ["terre"],                 ["terra"]),
("Himmel",       "der","Himmel",       ["sky","heaven"],             ["ciel"],                  ["céu"]),
("Meer",         "das","Meere",        ["sea"],                      ["mer"],                   ["mar"]),
("See",          "der","Seen",         ["lake"],                     ["lac"],                   ["lago"]),
("Fluss",        "der","Flüsse",       ["river"],                    ["fleuve","rivière"],      ["rio"]),
("Berg",         "der","Berge",        ["mountain"],                 ["montagne"],              ["montanha","monte"]),
("Wald",         "der","Wälder",       ["forest","woods"],           ["forêt","bois"],          ["floresta","mata"]),
("Feld",         "das","Felder",       ["field"],                    ["champ"],                 ["campo"]),
("Insel",        "die","Inseln",       ["island"],                   ["île"],                   ["ilha"]),
("Küste",        "die","Küsten",       ["coast"],                    ["côte"],                  ["costa","litoral"]),
("Park",         "der","Parks",        ["park"],                     ["parc"],                  ["parque"]),
("Garten",       "der","Gärten",       ["garden"],                   ["jardin"],                ["jardim"]),
("Reise",        "die","Reisen",       ["journey","trip"],           ["voyage"],                ["viagem"]),
("Zug",          "der","Züge",         ["train"],                    ["train"],                 ["trem","comboio"]),
("Auto",         "das","Autos",        ["car"],                      ["voiture","auto"],        ["carro"]),
("Bus",          "der","Busse",        ["bus"],                      ["bus"],                   ["ônibus"]),
("Flugzeug",     "das","Flugzeuge",    ["airplane"],                 ["avion"],                 ["avião"]),
("Schiff",       "das","Schiffe",      ["ship"],                     ["navire","bateau"],       ["navio","barco"]),
("Fahrrad",      "das","Fahrräder",    ["bicycle"],                  ["vélo","bicyclette"],     ["bicicleta"]),
("Bahnhof",      "der","Bahnhöfe",     ["train station"],            ["gare"],                  ["estação"]),
("Flughafen",    "der","Flughäfen",    ["airport"],                  ["aéroport"],              ["aeroporto"]),
("Hafen",        "der","Häfen",        ["port","harbor"],            ["port"],                  ["porto"]),
("Hotel",        "das","Hotels",       ["hotel"],                    ["hôtel"],                 ["hotel"]),
("Restaurant",   "das","Restaurants",  ["restaurant"],               ["restaurant"],            ["restaurante"]),
("Geschäft",     "das","Geschäfte",    ["shop","business"],          ["magasin","affaire"],     ["loja","negócio"]),
("Markt",        "der","Märkte",       ["market"],                   ["marché"],                ["mercado","feira"]),
("Schule",       "die","Schulen",      ["school"],                   ["école"],                 ["escola"]),
("Universität",  "die","Universitäten",["university"],               ["université"],            ["universidade"]),
("Kirche",       "die","Kirchen",      ["church"],                   ["église"],                ["igreja"]),
("Museum",       "das","Museen",       ["museum"],                   ["musée"],                 ["museu"]),
("Bibliothek",   "die","Bibliotheken", ["library"],                  ["bibliothèque"],          ["biblioteca"]),

# ============================================================
# LEVEL 6 — Work, money & tools
# ============================================================
("Arbeit",       "die","Arbeiten",     ["work","job"],               ["travail"],               ["trabalho"]),
("Beruf",        "der","Berufe",       ["profession"],               ["profession","métier"],   ["profissão","ofício"]),
("Job",          "der","Jobs",         ["job"],                      ["boulot","travail"],      ["emprego"]),
("Firma",        "die","Firmen",       ["firm","company"],           ["firme","entreprise"],    ["firma","empresa"]),
("Unternehmen",  "das","Unternehmen",  ["enterprise","company"],     ["entreprise"],            ["empresa"]),
("Büro",         "das","Büros",        ["office"],                   ["bureau"],                ["escritório"]),
("Fabrik",       "die","Fabriken",     ["factory"],                  ["usine"],                 ["fábrica"]),
("Werkstatt",    "die","Werkstätten",  ["workshop"],                 ["atelier"],               ["oficina"]),
("Gehalt",       "das","Gehälter",     ["salary"],                   ["salaire"],               ["salário"]),
("Lohn",         "der","Löhne",        ["wage","pay"],               ["salaire","paie"],        ["salário","paga"]),
("Geld",         "das","—",            ["money"],                    ["argent"],                ["dinheiro"]),
("Preis",        "der","Preise",       ["price","prize"],            ["prix"],                  ["preço","prêmio"]),
("Kosten",       "die","—",            ["costs"],                    ["coûts","frais"],         ["custos"]),
("Steuer",       "die","Steuern",      ["tax"],                      ["impôt","taxe"],          ["imposto"]),
("Rechnung",     "die","Rechnungen",   ["bill","invoice"],           ["facture"],               ["conta","fatura"]),
("Kunde",        "der","Kunden",       ["customer","client"],        ["client"],                ["cliente"]),
("Verkauf",      "der","Verkäufe",     ["sale"],                     ["vente"],                 ["venda"]),
("Handel",       "der","—",            ["trade","commerce"],         ["commerce","négoce"],     ["comércio"]),
("Bank",         "die","Banken",       ["bank"],                     ["banque"],                ["banco"]),
("Konto",        "das","Konten",       ["account"],                  ["compte"],                ["conta"]),
("Kredit",       "der","Kredite",      ["credit","loan"],            ["crédit","prêt"],         ["crédito","empréstimo"]),
("Vertrag",      "der","Verträge",     ["contract"],                 ["contrat"],               ["contrato"]),
("Projekt",      "das","Projekte",     ["project"],                  ["projet"],                ["projeto"]),
("Aufgabe",      "die","Aufgaben",     ["task","assignment"],        ["tâche","devoir"],        ["tarefa","dever"]),
("Ziel",         "das","Ziele",        ["goal","target"],            ["but","objectif"],        ["objetivo","alvo"]),
("Erfolg",       "der","Erfolge",      ["success"],                  ["succès","réussite"],     ["sucesso","êxito"]),
("Fehler",       "der","Fehler",       ["error","mistake"],          ["erreur","faute"],        ["erro","engano"]),
("Werkzeug",     "das","Werkzeuge",    ["tool"],                     ["outil"],                 ["ferramenta"]),
("Maschine",     "die","Maschinen",    ["machine"],                  ["machine"],               ["máquina"]),
("Computer",     "der","Computer",     ["computer"],                 ["ordinateur"],            ["computador"]),
("Handy",        "das","Handys",       ["mobile phone"],             ["portable","mobile"],     ["celular","telemóvel"]),
("Telefon",      "das","Telefone",     ["telephone"],                ["téléphone"],             ["telefone"]),
("Papier",       "das","Papiere",      ["paper"],                    ["papier"],                ["papel"]),
("Stift",        "der","Stifte",       ["pen","pencil"],             ["stylo","crayon"],        ["caneta","lápis"]),
("Brief",        "der","Briefe",       ["letter"],                   ["lettre"],                ["carta"]),
("Adresse",      "die","Adressen",     ["address"],                  ["adresse"],               ["endereço"]),
("Nummer",       "die","Nummern",      ["number"],                   ["numéro"],                ["número"]),
("Karte",        "die","Karten",       ["card","map"],               ["carte"],                 ["cartão","mapa"]),
("Post",         "die","—",            ["mail","post"],              ["poste","courrier"],      ["correio"]),
("Paket",        "das","Pakete",       ["package","parcel"],         ["colis","paquet"],        ["pacote","encomenda"]),

# ============================================================
# LEVEL 7 — Nature & weather
# ============================================================
("Natur",        "die","Naturen",      ["nature"],                   ["nature"],                ["natureza"]),
("Wetter",       "das","—",            ["weather"],                  ["temps","météo"],         ["tempo","clima"]),
("Sonne",        "die","Sonnen",       ["sun"],                      ["soleil"],                ["sol"]),
("Mond",         "der","Monde",        ["moon"],                     ["lune"],                  ["lua"]),
("Stern",        "der","Sterne",       ["star"],                     ["étoile"],                ["estrela"]),
("Wolke",        "die","Wolken",       ["cloud"],                    ["nuage"],                 ["nuvem"]),
("Regen",        "der","—",            ["rain"],                     ["pluie"],                 ["chuva"]),
("Schnee",       "der","—",            ["snow"],                     ["neige"],                 ["neve"]),
("Eis",          "das","—",            ["ice"],                      ["glace"],                 ["gelo"]),
("Wind",         "der","Winde",        ["wind"],                     ["vent"],                  ["vento"]),
("Sturm",        "der","Stürme",       ["storm"],                    ["tempête","orage"],       ["tempestade"]),
("Blitz",        "der","Blitze",       ["lightning"],                ["éclair","foudre"],       ["relâmpago","raio"]),
("Donner",       "der","Donner",       ["thunder"],                  ["tonnerre"],              ["trovão"]),
("Nebel",        "der","Nebel",        ["fog","mist"],               ["brouillard","brume"],    ["neblina","névoa"]),
("Kälte",        "die","—",            ["cold"],                     ["froid"],                 ["frio"]),
("Hitze",        "die","—",            ["heat"],                     ["chaleur"],               ["calor"]),
("Baum",         "der","Bäume",        ["tree"],                     ["arbre"],                 ["árvore"]),
("Blume",        "die","Blumen",       ["flower"],                   ["fleur"],                 ["flor"]),
("Blatt",        "das","Blätter",      ["leaf","sheet"],             ["feuille"],               ["folha"]),
("Gras",         "das","Gräser",       ["grass"],                    ["herbe"],                 ["grama"]),
("Pflanze",      "die","Pflanzen",     ["plant"],                    ["plante"],                ["planta"]),
("Tier",         "das","Tiere",        ["animal"],                   ["animal"],                ["animal"]),
("Hund",         "der","Hunde",        ["dog"],                      ["chien"],                 ["cachorro","cão"]),
("Katze",        "die","Katzen",       ["cat"],                      ["chat"],                  ["gato"]),
("Vogel",        "der","Vögel",        ["bird"],                     ["oiseau"],                ["pássaro","ave"]),
("Pferd",        "das","Pferde",       ["horse"],                    ["cheval"],                ["cavalo"]),
("Kuh",          "die","Kühe",         ["cow"],                      ["vache"],                 ["vaca"]),
("Schwein",      "das","Schweine",     ["pig"],                      ["cochon","porc"],         ["porco"]),
("Schaf",        "das","Schafe",       ["sheep"],                    ["mouton"],                ["ovelha"]),
("Wolf",         "der","Wölfe",        ["wolf"],                     ["loup"],                  ["lobo"]),
("Fluss",        "der","Flüsse",       ["river"],                    ["fleuve","rivière"],      ["rio"]),   # already, will dedupe
("Wüste",        "die","Wüsten",       ["desert"],                   ["désert"],                ["deserto"]),
("Tal",          "das","Täler",        ["valley"],                   ["vallée"],                ["vale"]),
("Hügel",        "der","Hügel",        ["hill"],                     ["colline"],               ["colina"]),
("Wiese",        "die","Wiesen",       ["meadow"],                   ["prairie","pré"],         ["prado","campina"]),
("Feuer",        "das","Feuer",        ["fire"],                     ["feu"],                   ["fogo"]),
("Rauch",        "der","—",            ["smoke"],                    ["fumée"],                 ["fumaça"]),
("Erdbeben",     "das","Erdbeben",     ["earthquake"],               ["tremblement de terre"],  ["terremoto"]),
("Klima",        "das","Klimata",      ["climate"],                  ["climat"],                ["clima"]),
("Umwelt",       "die","—",            ["environment"],              ["environnement"],         ["meio ambiente"]),

# ============================================================
# LEVEL 8 — Actions & events
# ============================================================
("Sache",        "die","Sachen",       ["thing","matter"],           ["chose","affaire"],       ["coisa","assunto"]),
("Ding",         "das","Dinge",        ["thing"],                    ["chose"],                 ["coisa"]),
("Frage",        "die","Fragen",       ["question"],                 ["question"],              ["pergunta","questão"]),
("Antwort",      "die","Antworten",    ["answer","reply"],           ["réponse"],               ["resposta"]),
("Problem",      "das","Probleme",     ["problem"],                  ["problème"],              ["problema"]),
("Lösung",       "die","Lösungen",     ["solution"],                 ["solution"],              ["solução"]),
("Idee",         "die","Ideen",        ["idea"],                     ["idée"],                  ["ideia"]),
("Plan",         "der","Pläne",        ["plan"],                     ["plan"],                  ["plano"]),
("Entscheidung", "die","Entscheidungen",["decision"],                ["décision"],              ["decisão"]),
("Wahl",         "die","Wahlen",       ["choice","election"],        ["choix","élection"],      ["escolha","eleição"]),
("Möglichkeit",  "die","Möglichkeiten",["possibility","opportunity"],["possibilité"],           ["possibilidade"]),
("Chance",       "die","Chancen",      ["chance"],                   ["chance"],                ["chance","oportunidade"]),
("Grund",        "der","Gründe",       ["reason","ground"],          ["raison","motif"],        ["razão","motivo"]),
("Ursache",      "die","Ursachen",     ["cause"],                    ["cause"],                 ["causa"]),
("Folge",        "die","Folgen",       ["consequence","sequel"],     ["conséquence","suite"],   ["consequência","sequência"]),
("Wirkung",      "die","Wirkungen",    ["effect","impact"],          ["effet","impact"],        ["efeito","impacto"]),
("Bedeutung",    "die","Bedeutungen",  ["meaning","importance"],     ["signification","sens"],  ["significado","importância"]),
("Zweck",        "der","Zwecke",       ["purpose"],                  ["but","fin"],             ["propósito","finalidade"]),
("Absicht",      "die","Absichten",    ["intention"],                ["intention"],             ["intenção"]),
("Sinn",         "der","Sinne",        ["sense","meaning"],          ["sens"],                  ["sentido"]),
("Regel",        "die","Regeln",       ["rule"],                     ["règle"],                 ["regra"]),
("Gesetz",       "das","Gesetze",      ["law"],                      ["loi"],                   ["lei"]),
("Ordnung",      "die","Ordnungen",    ["order","tidiness"],         ["ordre"],                 ["ordem"]),
("System",       "das","Systeme",      ["system"],                   ["système"],               ["sistema"]),
("Methode",      "die","Methoden",     ["method"],                   ["méthode"],               ["método"]),
("Weise",        "die","Weisen",       ["way","manner"],             ["façon","manière"],       ["maneira","modo"]),
("Art",          "die","Arten",        ["kind","type","manner"],     ["sorte","genre"],         ["tipo","espécie"]),
("Form",         "die","Formen",       ["form","shape"],             ["forme"],                 ["forma"]),
("Rolle",        "die","Rollen",       ["role"],                     ["rôle"],                  ["papel","função"]),
("Schritt",      "der","Schritte",     ["step"],                     ["pas","étape"],           ["passo","etapa"]),
("Versuch",      "der","Versuche",     ["attempt","experiment"],     ["essai","tentative"],     ["tentativa","experimento"]),
("Bewegung",     "die","Bewegungen",   ["movement"],                 ["mouvement"],             ["movimento"]),
("Reihe",        "die","Reihen",       ["row","series"],             ["rang","série"],          ["fileira","série"]),
("Fall",         "der","Fälle",        ["case","fall"],              ["cas","chute"],           ["caso","queda"]),
("Beispiel",     "das","Beispiele",    ["example"],                  ["exemple"],               ["exemplo"]),
("Ereignis",     "das","Ereignisse",   ["event"],                    ["événement"],             ["evento","acontecimento"]),
("Vorfall",      "der","Vorfälle",     ["incident"],                 ["incident"],              ["incidente"]),
("Situation",    "die","Situationen",  ["situation"],                ["situation"],             ["situação"]),
("Zustand",      "der","Zustände",     ["state","condition"],        ["état","condition"],      ["estado","condição"]),
("Veränderung",  "die","Veränderungen",["change","alteration"],      ["changement"],            ["mudança","alteração"]),

# ============================================================
# LEVEL 9 — Number, shape & measure
# ============================================================
("Zahl",         "die","Zahlen",       ["number"],                   ["nombre","chiffre"],      ["número","algarismo"]),
("Anzahl",       "die","—",            ["number","quantity"],        ["nombre","quantité"],     ["quantidade","número"]),
("Menge",        "die","Mengen",       ["quantity","amount","crowd"],["quantité","foule"],      ["quantidade","multidão"]),
("Hälfte",       "die","Hälften",      ["half"],                     ["moitié"],                ["metade"]),
("Drittel",      "das","Drittel",      ["third"],                    ["tiers"],                 ["terço"]),
("Viertel",      "das","Viertel",      ["quarter"],                  ["quart"],                 ["quarto","quarteirão"]),
("Prozent",      "das","Prozent",      ["percent"],                  ["pour cent"],             ["por cento"]),
("Summe",        "die","Summen",       ["sum","total"],              ["somme","total"],         ["soma","total"]),
("Rest",         "der","Reste",        ["rest","remainder"],         ["reste"],                 ["resto"]),
("Paar",         "das","Paare",        ["couple","pair"],            ["couple","paire"],        ["par","casal"]),  # dedupe
("Dutzend",      "das","Dutzende",     ["dozen"],                    ["douzaine"],              ["dúzia"]),
("Hundert",      "das","Hunderte",    ["hundred"],                  ["centaine"],              ["cem","centena"]),
("Tausend",      "das","Tausende",    ["thousand"],                 ["millier"],               ["mil","milhar"]),
("Million",      "die","Millionen",    ["million"],                  ["million"],               ["milhão"]),
("Länge",        "die","Längen",       ["length"],                   ["longueur"],              ["comprimento","extensão"]),
("Breite",       "die","Breiten",      ["width","breadth"],          ["largeur"],               ["largura"]),
("Höhe",         "die","Höhen",        ["height"],                   ["hauteur"],               ["altura"]),
("Tiefe",        "die","Tiefen",       ["depth"],                    ["profondeur"],            ["profundidade"]),
("Größe",        "die","Größen",       ["size","greatness"],         ["taille","grandeur"],     ["tamanho","grandeza"]),
("Gewicht",      "das","Gewichte",     ["weight"],                   ["poids"],                 ["peso"]),
("Maß",          "das","Maße",         ["measure"],                  ["mesure"],                ["medida"]),
("Meter",        "der","Meter",        ["meter"],                    ["mètre"],                 ["metro"]),
("Kilo",         "das","Kilos",        ["kilo","kilogram"],          ["kilo","kilogramme"],     ["quilo"]),
("Liter",        "der","Liter",        ["liter"],                    ["litre"],                 ["litro"]),
("Grad",         "der","Grade",        ["degree"],                   ["degré"],                 ["grau"]),
("Kreis",        "der","Kreise",       ["circle"],                   ["cercle"],                ["círculo"]),
("Linie",        "die","Linien",       ["line"],                     ["ligne"],                 ["linha"]),
("Punkt",        "der","Punkte",       ["point","dot"],              ["point"],                 ["ponto"]),
("Ecke",         "die","Ecken",        ["corner"],                   ["coin"],                  ["canto","esquina"]),
("Seite",        "die","Seiten",       ["side","page"],              ["côté","page"],           ["lado","página"]),
("Reihenfolge",  "die","Reihenfolgen", ["order","sequence"],         ["ordre","séquence"],      ["ordem","sequência"]),
("Struktur",     "die","Strukturen",   ["structure"],                ["structure"],             ["estrutura"]),
("Muster",       "das","Muster",       ["pattern"],                  ["motif","modèle"],        ["padrão","modelo"]),
("Zeichen",      "das","Zeichen",      ["sign","mark"],              ["signe"],                 ["sinal"]),
("Farbe",        "die","Farben",       ["color"],                    ["couleur"],               ["cor"]),
("Grenze",       "die","Grenzen",      ["border","limit"],           ["frontière","limite"],    ["fronteira","limite"]),
("Anteil",       "der","Anteile",      ["share","portion"],          ["part","portion"],        ["parte","cota"]),
("Vielfalt",     "die","Vielfalten",   ["diversity","variety"],      ["diversité","variété"],   ["diversidade","variedade"]),
("Einheit",      "die","Einheiten",    ["unit","unity"],             ["unité"],                 ["unidade"]),
("Ganze",        "das","—",            ["whole"],                    ["tout","entier"],         ["todo","inteiro"]),

# ============================================================
# LEVEL 10 — Feelings & states
# ============================================================
("Gefühl",       "das","Gefühle",      ["feeling","emotion"],        ["sentiment","émotion"],   ["sentimento","emoção"]),
("Freude",       "die","Freuden",      ["joy"],                      ["joie"],                  ["alegria"]),
("Glück",        "das","—",            ["luck","happiness"],         ["bonheur","chance"],      ["sorte","felicidade"]),
("Trauer",       "die","—",            ["mourning","grief"],         ["deuil","tristesse"],     ["luto","tristeza"]),
("Traurigkeit",  "die","—",            ["sadness"],                  ["tristesse"],             ["tristeza"]),
("Wut",          "die","—",            ["anger","rage"],             ["colère","rage"],         ["raiva","ira"]),
("Ärger",        "der","—",            ["annoyance","trouble"],      ["ennui","agacement"],     ["aborrecimento","chateação"]),
("Angst",        "die","Ängste",       ["fear","anxiety"],           ["peur","angoisse"],       ["medo","angústia"]),
("Furcht",       "die","—",            ["fear","dread"],             ["crainte","peur"],        ["temor","medo"]),
("Sorge",        "die","Sorgen",       ["worry","care"],             ["souci","inquiétude"],    ["preocupação","cuidado"]),
("Hoffnung",     "die","Hoffnungen",   ["hope"],                     ["espoir","espérance"],    ["esperança"]),
("Mut",          "der","—",            ["courage"],                  ["courage"],               ["coragem"]),
("Scham",        "die","—",            ["shame"],                    ["honte"],                 ["vergonha"]),
("Schuld",       "die","Schulden",     ["guilt","debt"],             ["culpabilité","dette"],   ["culpa","dívida"]),
("Reue",         "die","—",            ["remorse","regret"],         ["remords","repentir"],    ["arrependimento","remorso"]),
("Sehnsucht",    "die","Sehnsüchte",   ["longing","yearning"],       ["nostalgie","désir"],     ["saudade","anseio"]),
("Neugier",      "die","—",            ["curiosity"],                ["curiosité"],             ["curiosidade"]),
("Neid",         "der","—",            ["envy"],                     ["envie","jalousie"],      ["inveja"]),
("Eifersucht",   "die","—",            ["jealousy"],                 ["jalousie"],              ["ciúme"]),
("Stolz",        "der","—",            ["pride"],                    ["fierté","orgueil"],      ["orgulho"]),
("Demut",        "die","—",            ["humility"],                 ["humilité"],              ["humildade"]),
("Zufriedenheit","die","—",            ["contentment"],              ["satisfaction","contentement"],["satisfação","contentamento"]),
("Ruhe",         "die","—",            ["calm","rest","quiet"],      ["calme","repos"],         ["calma","descanso","silêncio"]),
("Frieden",      "der","—",            ["peace"],                    ["paix"],                  ["paz"]),
("Stille",       "die","—",            ["silence","stillness"],      ["silence"],               ["silêncio"]),
("Lärm",         "der","—",            ["noise"],                    ["bruit"],                 ["barulho","ruído"]),
("Stimmung",     "die","Stimmungen",   ["mood","atmosphere"],        ["humeur","ambiance"],     ["humor","clima"]),
("Laune",        "die","Launen",       ["mood","whim"],              ["humeur","caprice"],      ["humor","capricho"]),
("Interesse",    "das","Interessen",   ["interest"],                 ["intérêt"],               ["interesse"]),
("Langeweile",   "die","—",            ["boredom"],                  ["ennui"],                 ["tédio","chateação"]),
("Leidenschaft", "die","Leidenschaften",["passion"],                 ["passion"],               ["paixão"]),
("Zärtlichkeit", "die","—",            ["tenderness"],               ["tendresse"],             ["ternura"]),
("Zuneigung",    "die","—",            ["affection"],                ["affection"],             ["afeição","carinho"]),
("Zorn",         "der","—",            ["wrath","rage"],             ["colère","courroux"],    ["ira","fúria"]),
("Ekel",         "der","—",            ["disgust"],                  ["dégoût"],                ["nojo","asco"]),
("Überraschung", "die","Überraschungen",["surprise"],                ["surprise"],              ["surpresa"]),
("Enttäuschung", "die","Enttäuschungen",["disappointment"],          ["déception"],             ["decepção","desilusão"]),
("Erwartung",    "die","Erwartungen",  ["expectation"],              ["attente","espérance"],   ["expectativa","espera"]),
("Vertrauen",    "das","—",            ["trust","confidence"],       ["confiance"],             ["confiança"]),
("Misstrauen",   "das","—",            ["mistrust"],                 ["méfiance"],              ["desconfiança"]),

# ============================================================
# LEVEL 11 — Being & metaphysics
# ============================================================
("Sein",         "das","—",            ["being"],                    ["être","existence"],      ["ser","existência"]),
("Dasein",       "das","—",            ["existence","being-there"],  ["existence","Dasein"],    ["existência","Dasein"]),
("Wesen",        "das","Wesen",        ["essence","being"],          ["essence","être"],        ["essência","ser"]),
("Existenz",     "die","Existenzen",   ["existence"],                ["existence"],             ["existência"]),
("Wirklichkeit", "die","Wirklichkeiten",["reality"],                 ["réalité"],               ["realidade"]),
("Realität",     "die","Realitäten",   ["reality"],                  ["réalité"],               ["realidade"]),
("Substanz",     "die","Substanzen",   ["substance"],                ["substance"],             ["substância"]),
("Materie",      "die","Materien",     ["matter"],                   ["matière"],               ["matéria"]),
("Geist",        "der","Geister",      ["spirit","mind","ghost"],    ["esprit"],                ["espírito","mente"]),
("Seele",        "die","Seelen",       ["soul"],                     ["âme"],                   ["alma"]),
("Idee",         "die","Ideen",        ["idea","form"],              ["idée"],                  ["ideia"]),  # dedupe
("Begriff",      "der","Begriffe",     ["concept","notion"],         ["concept","notion"],      ["conceito","noção"]),
("Ding",         "das","Dinge",        ["thing"],                    ["chose"],                 ["coisa"]),  # dedupe
("Objekt",       "das","Objekte",      ["object"],                   ["objet"],                 ["objeto"]),
("Subjekt",      "das","Subjekte",     ["subject"],                  ["sujet"],                 ["sujeito"]),
("Eigenschaft",  "die","Eigenschaften",["property","quality"],       ["propriété","qualité"],   ["propriedade","qualidade"]),
("Qualität",     "die","Qualitäten",   ["quality"],                  ["qualité"],               ["qualidade"]),
("Quantität",    "die","Quantitäten",  ["quantity"],                 ["quantité"],              ["quantidade"]),
("Relation",     "die","Relationen",   ["relation"],                 ["relation"],              ["relação"]),
("Kausalität",   "die","—",            ["causality"],                ["causalité"],             ["causalidade"]),
("Ursprung",     "der","Ursprünge",    ["origin"],                   ["origine"],               ["origem"]),
("Grund",        "der","Gründe",       ["ground","reason"],          ["fondement","raison"],    ["fundamento","razão"]),  # dedupe
("Prinzip",      "das","Prinzipien",   ["principle"],                ["principe"],              ["princípio"]),
("Erscheinung",  "die","Erscheinungen",["appearance","phenomenon"],  ["apparition","phénomène"],["aparência","fenômeno"]),
("Phänomen",     "das","Phänomene",    ["phenomenon"],               ["phénomène"],             ["fenômeno"]),
("Wirklichkeit", "die","—",            ["actuality"],                ["actualité"],             ["atualidade"]),  # dedupe
("Möglichkeit",  "die","Möglichkeiten",["possibility"],              ["possibilité"],           ["possibilidade"]),  # dedupe
("Notwendigkeit","die","—",            ["necessity"],                ["nécessité"],             ["necessidade"]),
("Zufall",       "der","Zufälle",      ["chance","coincidence"],     ["hasard","coïncidence"],  ["acaso","coincidência"]),
("Unendlichkeit","die","—",            ["infinity"],                 ["infini","infinité"],     ["infinito","infinidade"]),
("Endlichkeit",  "die","—",            ["finitude"],                 ["finitude"],              ["finitude"]),
("Ganzheit",     "die","—",            ["wholeness","totality"],     ["totalité"],              ["totalidade","integridade"]),
("Vielheit",     "die","—",            ["multiplicity"],             ["multiplicité"],          ["multiplicidade"]),
("Bewegung",     "die","—",            ["motion"],                   ["mouvement"],             ["movimento"]),  # dedupe
("Kraft",        "die","Kräfte",       ["force","power"],            ["force","puissance"],     ["força","poder"]),
("Energie",      "die","Energien",     ["energy"],                   ["énergie"],               ["energia"]),
("Zeitlichkeit", "die","—",            ["temporality"],              ["temporalité"],           ["temporalidade"]),
("Räumlichkeit", "die","—",            ["spatiality"],               ["spatialité"],            ["espacialidade"]),
("Sein-zum-Tode","das","—",            ["being-toward-death"],       ["être-pour-la-mort"],     ["ser-para-a-morte"]),
("Nichts",       "das","—",            ["nothingness","nothing"],    ["néant","rien"],          ["nada","nulidade"]),

# ============================================================
# LEVEL 12 — Mind & consciousness
# ============================================================
("Bewusstsein",  "das","—",            ["consciousness"],            ["conscience"],            ["consciência"]),
("Unterbewusstsein","das","—",         ["subconscious"],             ["subconscient"],          ["subconsciente"]),
("Verstand",     "der","—",            ["understanding","intellect"],["entendement","raison"],  ["entendimento","razão"]),
("Vernunft",     "die","—",            ["reason"],                   ["raison"],                ["razão"]),
("Denken",       "das","—",            ["thinking","thought"],       ["pensée"],                ["pensamento"]),
("Gedanke",      "der","Gedanken",     ["thought"],                  ["pensée","idée"],         ["pensamento","ideia"]),
("Vorstellung",  "die","Vorstellungen",["representation","idea"],    ["représentation","idée"], ["representação","ideia"]),
("Einbildungskraft","die","—",         ["imagination"],              ["imagination"],           ["imaginação"]),
("Fantasie",     "die","Fantasien",    ["fantasy","imagination"],    ["fantaisie"],             ["fantasia","imaginação"]),
("Erinnerung",   "die","Erinnerungen", ["memory","recollection"],    ["mémoire","souvenir"],    ["memória","lembrança"]),
("Gedächtnis",   "das","Gedächtnisse", ["memory"],                   ["mémoire"],               ["memória"]),
("Aufmerksamkeit","die","—",           ["attention"],                ["attention"],             ["atenção"]),
("Wahrnehmung",  "die","Wahrnehmungen",["perception"],               ["perception"],            ["percepção"]),
("Empfindung",   "die","Empfindungen", ["sensation"],                ["sensation"],             ["sensação"]),
("Intuition",    "die","Intuitionen",  ["intuition"],                ["intuition"],             ["intuição"]),
("Anschauung",   "die","Anschauungen", ["intuition","view"],         ["intuition","vue"],       ["intuição","visão"]),
("Erfahrung",    "die","Erfahrungen",  ["experience"],               ["expérience"],            ["experiência"]),
("Erlebnis",     "das","Erlebnisse",   ["lived experience"],         ["vécu","expérience"],     ["experiência","vivência"]),
("Wille",        "der","—",            ["will"],                     ["volonté"],               ["vontade"]),
("Wollen",       "das","—",            ["willing"],                  ["vouloir"],               ["querer"]),
("Wunsch",       "der","Wünsche",      ["wish","desire"],            ["souhait","désir"],       ["desejo"]),
("Begierde",     "die","Begierden",    ["desire","craving"],         ["désir","convoitise"],    ["desejo","cobiça"]),
("Trieb",        "der","Triebe",       ["drive","instinct"],         ["pulsion","instinct"],    ["pulsão","instinto"]),
("Entschluss",   "der","Entschlüsse",  ["resolution","decision"],    ["résolution","décision"], ["resolução","decisão"]),
("Absicht",      "die","Absichten",    ["intention"],                ["intention"],             ["intenção"]),  # dedupe
("Motiv",        "das","Motive",       ["motive"],                   ["motif"],                 ["motivo"]),
("Instinkt",     "der","Instinkte",    ["instinct"],                 ["instinct"],              ["instinto"]),
("Reflex",       "der","Reflexe",      ["reflex"],                   ["réflexe"],               ["reflexo"]),
("Meinung",      "die","Meinungen",    ["opinion"],                  ["opinion","avis"],        ["opinião"]),
("Urteil",       "das","Urteile",      ["judgement"],                ["jugement"],              ["juízo","julgamento"]),
("Überzeugung",  "die","Überzeugungen",["conviction","belief"],      ["conviction"],            ["convicção"]),
("Zweifel",      "der","Zweifel",      ["doubt"],                    ["doute"],                 ["dúvida"]),
("Gewissheit",   "die","Gewissheiten", ["certainty"],                ["certitude"],             ["certeza"]),
("Ungewissheit", "die","—",            ["uncertainty"],              ["incertitude"],           ["incerteza"]),
("Illusion",     "die","Illusionen",   ["illusion"],                 ["illusion"],              ["ilusão"]),
("Täuschung",    "die","Täuschungen",  ["deception","illusion"],     ["tromperie","illusion"],  ["engano","ilusão"]),
("Reflexion",    "die","Reflexionen",  ["reflection"],               ["réflexion"],             ["reflexão"]),
("Selbst",       "das","—",            ["self"],                     ["soi"],                   ["si mesmo","self"]),
("Ich",          "das","—",            ["I","ego"],                  ["moi","ego"],             ["eu","ego"]),
("Identität",    "die","Identitäten",  ["identity"],                 ["identité"],              ["identidade"]),

# ============================================================
# LEVEL 13 — Ethics & value
# ============================================================
("Ethik",        "die","Ethiken",      ["ethics"],                   ["éthique"],               ["ética"]),
("Moral",        "die","Moralen",      ["morality"],                 ["morale"],                ["moral"]),
("Tugend",       "die","Tugenden",     ["virtue"],                   ["vertu"],                 ["virtude"]),
("Laster",       "das","Laster",       ["vice"],                     ["vice"],                  ["vício"]),
("Gute",         "das","—",            ["the good"],                 ["le bien"],               ["o bem"]),
("Böse",         "das","—",            ["the evil"],                 ["le mal"],                ["o mal"]),
("Pflicht",      "die","Pflichten",    ["duty","obligation"],        ["devoir"],                ["dever"]),
("Recht",        "das","Rechte",       ["right","law"],              ["droit"],                 ["direito"]),
("Unrecht",      "das","—",            ["wrong","injustice"],        ["tort","injustice"],      ["injustiça"]),
("Gerechtigkeit","die","—",            ["justice"],                  ["justice"],               ["justiça"]),
("Ungerechtigkeit","die","—",          ["injustice"],                ["injustice"],             ["injustiça"]),
("Verantwortung","die","Verantwortungen",["responsibility"],         ["responsabilité"],        ["responsabilidade"]),
("Schuld",       "die","—",            ["guilt"],                    ["culpabilité","faute"],   ["culpa"]),  # dedupe
("Sünde",        "die","Sünden",       ["sin"],                      ["péché"],                 ["pecado"]),
("Vergebung",    "die","—",            ["forgiveness"],              ["pardon"],                ["perdão"]),
("Mitleid",      "das","—",            ["compassion","pity"],        ["compassion","pitié"],    ["compaixão","pena"]),
("Barmherzigkeit","die","—",           ["mercy"],                    ["miséricorde"],           ["misericórdia"]),
("Nächstenliebe","die","—",            ["neighborly love"],          ["amour du prochain"],     ["amor ao próximo"]),
("Gewissen",     "das","Gewissen",     ["conscience"],               ["conscience"],            ["consciência"]),
("Wert",         "der","Werte",        ["value"],                    ["valeur"],                ["valor"]),
("Würde",        "die","—",            ["dignity"],                  ["dignité"],               ["dignidade"]),
("Ehre",         "die","Ehren",        ["honor"],                    ["honneur"],               ["honra"]),
("Ehrlichkeit",  "die","—",            ["honesty"],                  ["honnêteté"],             ["honestidade"]),
("Wahrhaftigkeit","die","—",           ["truthfulness"],             ["véracité"],              ["veracidade"]),
("Aufrichtigkeit","die","—",           ["sincerity"],                ["sincérité"],             ["sinceridade"]),
("Loyalität",    "die","—",            ["loyalty"],                  ["loyauté"],               ["lealdade"]),
("Treue",        "die","—",            ["fidelity","loyalty"],       ["fidélité"],              ["fidelidade"]),
("Verrat",       "der","—",            ["betrayal"],                 ["trahison"],              ["traição"]),
("Lüge",         "die","Lügen",        ["lie"],                      ["mensonge"],              ["mentira"]),
("Wahrheit",     "die","Wahrheiten",   ["truth"],                    ["vérité"],                ["verdade"]),
("Toleranz",     "die","—",            ["tolerance"],                ["tolérance"],             ["tolerância"]),
("Achtung",      "die","—",            ["respect"],                  ["respect"],               ["respeito"]),
("Respekt",      "der","—",            ["respect"],                  ["respect"],               ["respeito"]),
("Gleichheit",   "die","—",            ["equality"],                 ["égalité"],               ["igualdade"]),
("Ungleichheit", "die","Ungleichheiten",["inequality"],              ["inégalité"],             ["desigualdade"]),
("Autonomie",    "die","—",            ["autonomy"],                 ["autonomie"],             ["autonomia"]),
("Freiheit",     "die","Freiheiten",   ["freedom","liberty"],        ["liberté"],               ["liberdade"]),
("Zwang",        "der","Zwänge",       ["coercion","compulsion"],    ["contrainte"],            ["coerção","compulsão"]),
("Gebot",        "das","Gebote",       ["commandment"],              ["commandement"],          ["mandamento"]),
("Verbot",       "das","Verbote",      ["prohibition","ban"],        ["interdiction","défense"],["proibição"]),

# ============================================================
# LEVEL 14 — Politics & society
# ============================================================
("Staat",        "der","Staaten",      ["state"],                    ["État"],                  ["Estado"]),
("Regierung",    "die","Regierungen",  ["government"],               ["gouvernement"],          ["governo"]),
("Politik",      "die","—",            ["politics","policy"],        ["politique"],             ["política"]),
("Demokratie",   "die","Demokratien",  ["democracy"],                ["démocratie"],            ["democracia"]),
("Republik",     "die","Republiken",   ["republic"],                 ["république"],            ["república"]),
("Monarchie",    "die","Monarchien",   ["monarchy"],                 ["monarchie"],             ["monarquia"]),
("Diktatur",     "die","Diktaturen",   ["dictatorship"],             ["dictature"],             ["ditadura"]),
("Tyrannei",     "die","Tyranneien",   ["tyranny"],                  ["tyrannie"],              ["tirania"]),
("Herrschaft",   "die","Herrschaften", ["rule","dominion"],          ["domination","règne"],    ["domínio","soberania"]),
("Macht",        "die","Mächte",       ["power"],                    ["pouvoir","puissance"],   ["poder","potência"]),
("Gewalt",       "die","Gewalten",     ["violence","force","power"], ["violence","pouvoir"],    ["violência","poder"]),
("Autorität",    "die","Autoritäten",  ["authority"],                ["autorité"],              ["autoridade"]),
("Volk",         "das","Völker",       ["people","folk"],            ["peuple"],                ["povo"]),
("Nation",       "die","Nationen",     ["nation"],                   ["nation"],                ["nação"]),
("Bürger",       "der","Bürger",       ["citizen"],                  ["citoyen"],               ["cidadão"]),
("Bürgertum",    "das","—",            ["bourgeoisie"],              ["bourgeoisie"],           ["burguesia"]),
("Klasse",       "die","Klassen",      ["class"],                    ["classe"],                ["classe"]),
("Stand",        "der","Stände",       ["estate","status"],          ["état","condition"],      ["condição","estamento"]),
("Elite",        "die","Eliten",       ["elite"],                    ["élite"],                 ["elite"]),
("Masse",        "die","Massen",       ["mass","crowd"],             ["masse","foule"],         ["massa","multidão"]),
("Partei",       "die","Parteien",     ["party"],                    ["parti"],                 ["partido"]),
("Bewegung",     "die","Bewegungen",   ["movement"],                 ["mouvement"],             ["movimento"]),  # dedupe
("Revolution",   "die","Revolutionen", ["revolution"],               ["révolution"],            ["revolução"]),
("Reform",       "die","Reformen",     ["reform"],                   ["réforme"],               ["reforma"]),
("Krieg",        "der","Kriege",       ["war"],                      ["guerre"],                ["guerra"]),
("Frieden",      "der","—",            ["peace"],                    ["paix"],                  ["paz"]),  # dedupe
("Konflikt",     "der","Konflikte",    ["conflict"],                 ["conflit"],               ["conflito"]),
("Krise",        "die","Krisen",       ["crisis"],                   ["crise"],                 ["crise"]),
("Ordnung",      "die","Ordnungen",    ["order"],                    ["ordre"],                 ["ordem"]),  # dedupe
("Gesetz",       "das","Gesetze",      ["law"],                      ["loi"],                   ["lei"]),  # dedupe
("Verfassung",   "die","Verfassungen", ["constitution"],             ["constitution"],          ["constituição"]),
("Souveränität", "die","—",            ["sovereignty"],              ["souveraineté"],          ["soberania"]),
("Bürgerkrieg",  "der","Bürgerkriege", ["civil war"],                ["guerre civile"],         ["guerra civil"]),
("Ideologie",    "die","Ideologien",   ["ideology"],                 ["idéologie"],             ["ideologia"]),
("Sozialismus",  "der","—",            ["socialism"],                ["socialisme"],            ["socialismo"]),
("Kapitalismus", "der","—",            ["capitalism"],               ["capitalisme"],           ["capitalismo"]),
("Liberalismus", "der","—",            ["liberalism"],               ["libéralisme"],           ["liberalismo"]),
("Konservatismus","der","—",           ["conservatism"],             ["conservatisme"],         ["conservadorismo"]),
("Anarchie",     "die","Anarchien",    ["anarchy"],                  ["anarchie"],              ["anarquia"]),
("Widerstand",   "der","—",            ["resistance"],               ["résistance"],            ["resistência"]),

# ============================================================
# LEVEL 15 — Knowledge & truth
# ============================================================
("Wissen",       "das","—",            ["knowledge"],                ["savoir","connaissance"], ["saber","conhecimento"]),
("Erkenntnis",   "die","Erkenntnisse", ["cognition","insight"],      ["connaissance","aperçu"], ["conhecimento","insight"]),
("Wissenschaft", "die","Wissenschaften",["science","scholarship"],   ["science"],               ["ciência"]),
("Philosophie",  "die","Philosophien", ["philosophy"],               ["philosophie"],           ["filosofia"]),
("Theorie",      "die","Theorien",     ["theory"],                   ["théorie"],               ["teoria"]),
("Praxis",       "die","Praxen",       ["practice"],                 ["pratique"],              ["prática"]),
("Methode",      "die","Methoden",     ["method"],                   ["méthode"],               ["método"]),  # dedupe
("Erklärung",    "die","Erklärungen",  ["explanation"],              ["explication"],           ["explicação"]),
("Begründung",   "die","Begründungen", ["justification","reason"],   ["justification"],         ["justificação","fundamentação"]),
("Argument",     "das","Argumente",    ["argument"],                 ["argument"],              ["argumento"]),
("These",        "die","Thesen",       ["thesis"],                   ["thèse"],                 ["tese"]),
("Antithese",    "die","Antithesen",   ["antithesis"],               ["antithèse"],             ["antítese"]),
("Synthese",     "die","Synthesen",    ["synthesis"],                ["synthèse"],              ["síntese"]),
("Beweis",       "der","Beweise",      ["proof","evidence"],         ["preuve"],                ["prova","evidência"]),
("Widerlegung",  "die","Widerlegungen",["refutation"],               ["réfutation"],            ["refutação"]),
("Hypothese",    "die","Hypothesen",   ["hypothesis"],               ["hypothèse"],             ["hipótese"]),
("Wahrheit",     "die","Wahrheiten",   ["truth"],                    ["vérité"],                ["verdade"]),  # dedupe
("Irrtum",       "der","Irrtümer",     ["error","fallacy"],          ["erreur"],                ["erro","engano"]),
("Meinung",      "die","Meinungen",    ["opinion"],                  ["opinion"],               ["opinião"]),  # dedupe
("Zweifel",      "der","Zweifel",      ["doubt"],                    ["doute"],                 ["dúvida"]),  # dedupe
("Skepsis",      "die","—",            ["skepticism"],               ["scepticisme"],           ["ceticismo"]),
("Kritik",       "die","Kritiken",     ["critique"],                 ["critique"],              ["crítica"]),
("Analyse",      "die","Analysen",     ["analysis"],                 ["analyse"],               ["análise"]),
("Synthese",     "die","Synthesen",    ["synthesis"],                ["synthèse"],              ["síntese"]),  # dedupe
("Deduktion",    "die","Deduktionen",  ["deduction"],                ["déduction"],             ["dedução"]),
("Induktion",    "die","Induktionen",  ["induction"],                ["induction"],             ["indução"]),
("Logik",        "die","Logiken",      ["logic"],                    ["logique"],               ["lógica"]),
("Widerspruch",  "der","Widersprüche", ["contradiction"],            ["contradiction"],         ["contradição"]),
("Paradox",      "das","Paradoxe",     ["paradox"],                  ["paradoxe"],              ["paradoxo"]),
("Definition",   "die","Definitionen", ["definition"],               ["définition"],            ["definição"]),
("Erkenntnistheorie","die","—",        ["epistemology"],             ["épistémologie"],         ["epistemologia"]),
("Rationalität", "die","—",            ["rationality"],              ["rationalité"],           ["racionalidade"]),
("Empirie",      "die","—",            ["empiricism","experience"],  ["empirisme"],             ["empiria"]),
("A_priori",     "das","—",            ["a priori"],                 ["a priori"],              ["a priori"]),
("A_posteriori", "das","—",            ["a posteriori"],             ["a posteriori"],          ["a posteriori"]),
("Kategorie",    "die","Kategorien",   ["category"],                 ["catégorie"],             ["categoria"]),
("Prämisse",     "die","Prämissen",    ["premise"],                  ["prémisse"],              ["premissa"]),
("Schluss",      "der","Schlüsse",     ["conclusion","inference"],   ["conclusion","inférence"],["conclusão","inferência"]),
("Weisheit",     "die","—",            ["wisdom"],                   ["sagesse"],               ["sabedoria"]),
("Unwissenheit", "die","—",            ["ignorance"],                ["ignorance"],             ["ignorância"]),

# ============================================================
# LEVEL 16 — Language & meaning
# ============================================================
("Sprache",      "die","Sprachen",     ["language"],                 ["langue","langage"],      ["língua","linguagem"]),
("Wort",         "das","Wörter",       ["word"],                     ["mot"],                   ["palavra"]),
("Satz",         "der","Sätze",        ["sentence","proposition"],   ["phrase","proposition"],  ["frase","proposição"]),
("Text",         "der","Texte",        ["text"],                     ["texte"],                 ["texto"]),
("Rede",         "die","Reden",        ["speech","discourse"],       ["discours","parole"],     ["fala","discurso"]),
("Gespräch",     "das","Gespräche",    ["conversation"],             ["conversation"],          ["conversa"]),
("Dialog",       "der","Dialoge",      ["dialogue"],                 ["dialogue"],              ["diálogo"]),
("Monolog",      "der","Monologe",     ["monologue"],                ["monologue"],             ["monólogo"]),
("Diskurs",      "der","Diskurse",     ["discourse"],                ["discours"],              ["discurso"]),
("Grammatik",    "die","Grammatiken",  ["grammar"],                  ["grammaire"],             ["gramática"]),
("Syntax",       "die","—",            ["syntax"],                   ["syntaxe"],               ["sintaxe"]),
("Semantik",     "die","—",            ["semantics"],                ["sémantique"],            ["semântica"]),
("Bedeutung",    "die","Bedeutungen",  ["meaning"],                  ["signification","sens"],  ["significado","sentido"]),  # dedupe
("Bezeichnung",  "die","Bezeichnungen",["designation","label"],      ["désignation"],           ["designação"]),
("Zeichen",      "das","Zeichen",      ["sign"],                     ["signe"],                 ["signo","sinal"]),  # dedupe
("Symbol",       "das","Symbole",      ["symbol"],                   ["symbole"],               ["símbolo"]),
("Metapher",     "die","Metaphern",    ["metaphor"],                 ["métaphore"],             ["metáfora"]),
("Bild",         "das","Bilder",       ["image","picture"],          ["image"],                 ["imagem"]),  # dedupe
("Ausdruck",     "der","Ausdrücke",    ["expression"],               ["expression"],            ["expressão"]),
("Übersetzung",  "die","Übersetzungen",["translation"],              ["traduction"],            ["tradução"]),
("Auslegung",    "die","Auslegungen",  ["interpretation"],           ["interprétation"],        ["interpretação"]),
("Interpretation","die","Interpretationen",["interpretation"],       ["interprétation"],        ["interpretação"]),
("Hermeneutik",  "die","—",            ["hermeneutics"],             ["herméneutique"],         ["hermenêutica"]),
("Rhetorik",     "die","Rhetoriken",   ["rhetoric"],                 ["rhétorique"],            ["retórica"]),
("Poetik",       "die","Poetiken",     ["poetics"],                  ["poétique"],              ["poética"]),
("Literatur",    "die","Literaturen",  ["literature"],               ["littérature"],           ["literatura"]),
("Erzählung",    "die","Erzählungen",  ["narrative","story"],        ["récit","narration"],     ["narrativa","conto"]),
("Geschichte",   "die","Geschichten",  ["story","history"],          ["histoire"],              ["história"]),
("Roman",        "der","Romane",       ["novel"],                    ["roman"],                 ["romance"]),
("Gedicht",      "das","Gedichte",     ["poem"],                     ["poème"],                 ["poema"]),
("Poesie",       "die","—",            ["poetry"],                   ["poésie"],                ["poesia"]),
("Prosa",        "die","—",            ["prose"],                    ["prose"],                 ["prosa"]),
("Stil",         "der","Stile",        ["style"],                    ["style"],                 ["estilo"]),
("Genre",        "das","Genres",       ["genre"],                    ["genre"],                 ["gênero"]),
("Zitat",        "das","Zitate",       ["quotation"],                ["citation"],              ["citação"]),
("Kommentar",    "der","Kommentare",   ["commentary"],               ["commentaire"],           ["comentário"]),
("Anmerkung",    "die","Anmerkungen",  ["remark","note"],            ["remarque","note"],       ["observação","nota"]),
("Autor",        "der","Autoren",      ["author"],                   ["auteur"],                ["autor"]),
("Leser",        "der","Leser",        ["reader"],                   ["lecteur"],               ["leitor"]),
("Schrift",      "die","Schriften",    ["writing","script"],         ["écriture"],              ["escrita","escritura"]),

# ============================================================
# LEVEL 17 — Art & aesthetics
# ============================================================
("Kunst",        "die","Künste",       ["art"],                      ["art"],                   ["arte"]),
("Werk",         "das","Werke",        ["work"],                     ["œuvre","travail"],       ["obra"]),
("Kunstwerk",    "das","Kunstwerke",   ["work of art"],              ["œuvre d'art"],           ["obra de arte"]),
("Ästhetik",     "die","Ästhetiken",   ["aesthetics"],               ["esthétique"],            ["estética"]),
("Schönheit",    "die","Schönheiten",  ["beauty"],                   ["beauté"],                ["beleza"]),
("Erhabenheit",  "die","—",            ["sublime","loftiness"],      ["sublime"],               ["sublime","grandeza"]),
("Anmut",        "die","—",            ["grace"],                    ["grâce"],                 ["graça"]),
("Harmonie",     "die","Harmonien",    ["harmony"],                  ["harmonie"],              ["harmonia"]),
("Proportion",   "die","Proportionen", ["proportion"],               ["proportion"],            ["proporção"]),
("Symmetrie",    "die","Symmetrien",   ["symmetry"],                 ["symétrie"],              ["simetria"]),
("Geschmack",    "der","Geschmäcker",  ["taste"],                    ["goût"],                  ["gosto"]),  # dedupe
("Kritiker",     "der","Kritiker",     ["critic"],                   ["critique"],              ["crítico"]),
("Genie",        "das","Genies",       ["genius"],                   ["génie"],                 ["gênio"]),
("Talent",       "das","Talente",      ["talent"],                   ["talent"],                ["talento"]),
("Inspiration",  "die","Inspirationen",["inspiration"],              ["inspiration"],           ["inspiração"]),
("Muse",         "die","Musen",        ["muse"],                     ["muse"],                  ["musa"]),
("Malerei",      "die","Malereien",    ["painting"],                 ["peinture"],              ["pintura"]),
("Skulptur",     "die","Skulpturen",   ["sculpture"],                ["sculpture"],             ["escultura"]),
("Musik",        "die","Musiken",      ["music"],                    ["musique"],               ["música"]),
("Tanz",         "der","Tänze",        ["dance"],                    ["danse"],                 ["dança"]),
("Theater",      "das","Theater",      ["theater"],                  ["théâtre"],               ["teatro"]),
("Film",         "der","Filme",        ["film","movie"],             ["film"],                  ["filme"]),
("Fotografie",   "die","Fotografien",  ["photography","photograph"], ["photographie"],          ["fotografia"]),
("Architektur",  "die","Architekturen",["architecture"],             ["architecture"],          ["arquitetura"]),
("Design",       "das","Designs",      ["design"],                   ["design"],                ["design"]),
("Zeichnung",    "die","Zeichnungen",  ["drawing"],                  ["dessin"],                ["desenho"]),
("Farbe",        "die","Farben",       ["color"],                    ["couleur"],               ["cor"]),  # dedupe
("Klang",        "der","Klänge",       ["sound"],                    ["son"],                   ["som"]),
("Ton",          "der","Töne",         ["tone","sound"],             ["ton","son"],             ["tom","som"]),
("Melodie",      "die","Melodien",     ["melody"],                   ["mélodie"],               ["melodia"]),
("Rhythmus",     "der","Rhythmen",     ["rhythm"],                   ["rythme"],                ["ritmo"]),  # dedupe
("Komposition",  "die","Kompositionen",["composition"],              ["composition"],           ["composição"]),
("Bühne",        "die","Bühnen",       ["stage"],                    ["scène"],                 ["palco","cena"]),
("Publikum",     "das","Publika",      ["audience","public"],        ["public"],                ["público"]),
("Ausstellung",  "die","Ausstellungen",["exhibition"],               ["exposition"],            ["exposição"]),
("Vorstellung",  "die","Vorstellungen",["performance"],              ["représentation"],        ["apresentação","espetáculo"]),
("Meisterwerk",  "das","Meisterwerke", ["masterpiece"],              ["chef-d'œuvre"],          ["obra-prima"]),
("Klassik",      "die","—",            ["classical (period)"],       ["classicisme"],           ["classicismo","clássico"]),
("Moderne",      "die","—",            ["modernity","modernism"],    ["modernité","modernisme"],["modernidade","modernismo"]),
("Avantgarde",   "die","Avantgarden",  ["avant-garde"],              ["avant-garde"],           ["vanguarda"]),

# ============================================================
# LEVEL 18 — History & culture
# ============================================================
("Geschichte",   "die","Geschichten",  ["history"],                  ["histoire"],              ["história"]),  # dedupe
("Vergangenheit","die","Vergangenheiten",["past"],                   ["passé"],                 ["passado"]),  # dedupe
("Erinnerung",   "die","Erinnerungen", ["memory"],                   ["mémoire","souvenir"],    ["memória"]),  # dedupe
("Denkmal",      "das","Denkmäler",    ["monument"],                 ["monument"],              ["monumento"]),
("Kultur",       "die","Kulturen",     ["culture"],                  ["culture"],               ["cultura"]),
("Zivilisation", "die","Zivilisationen",["civilization"],            ["civilisation"],          ["civilização"]),
("Tradition",    "die","Traditionen",  ["tradition"],                ["tradition"],             ["tradição"]),
("Sitte",        "die","Sitten",       ["custom","mores"],           ["coutume","mœurs"],       ["costume"]),
("Brauch",       "der","Bräuche",      ["custom","tradition"],       ["coutume"],               ["costume","hábito"]),
("Herkunft",     "die","—",            ["origin","descent"],         ["origine","provenance"],  ["origem","procedência"]),
("Ahne",         "der","Ahnen",        ["ancestor"],                 ["ancêtre"],               ["ancestral","antepassado"]),
("Erbe",         "das","—",            ["heritage","legacy"],        ["héritage"],              ["herança","legado"]),
("Nachlass",     "der","Nachlässe",    ["estate","legacy"],          ["legs","succession"],     ["espólio","legado"]),
("Zeitgeist",    "der","—",            ["Zeitgeist","spirit of the age"],["esprit du temps"],   ["Zeitgeist","espírito do tempo"]),
("Antike",       "die","—",            ["antiquity"],                ["antiquité"],             ["antiguidade"]),
("Mittelalter",  "das","—",            ["Middle Ages"],              ["Moyen Âge"],             ["Idade Média"]),
("Renaissance",  "die","—",            ["Renaissance"],              ["Renaissance"],           ["Renascimento"]),
("Aufklärung",   "die","—",            ["Enlightenment"],            ["Lumières"],              ["Iluminismo"]),
("Romantik",     "die","—",            ["Romanticism"],              ["romantisme"],            ["Romantismo"]),
("Klassik",      "die","—",            ["classical age"],            ["classicisme"],           ["classicismo"]),  # dedupe
("Reformation",  "die","Reformationen",["Reformation"],              ["Réforme"],               ["Reforma"]),
("Revolution",   "die","Revolutionen", ["revolution"],               ["révolution"],            ["revolução"]),  # dedupe
("Kolonie",      "die","Kolonien",     ["colony"],                   ["colonie"],               ["colônia"]),
("Kolonialismus","der","—",            ["colonialism"],              ["colonialisme"],          ["colonialismo"]),
("Imperium",     "das","Imperien",     ["empire"],                   ["empire"],                ["império"]),
("Weltkrieg",    "der","Weltkriege",   ["world war"],                ["guerre mondiale"],       ["guerra mundial"]),
("Faschismus",   "der","—",            ["fascism"],                  ["fascisme"],              ["fascismo"]),
("Nationalismus","der","—",            ["nationalism"],              ["nationalisme"],          ["nacionalismo"]),
("Emanzipation", "die","Emanzipationen",["emancipation"],            ["émancipation"],          ["emancipação"]),
("Migration",    "die","Migrationen",  ["migration"],                ["migration"],             ["migração"]),
("Diaspora",     "die","Diasporas",    ["diaspora"],                 ["diaspora"],              ["diáspora"]),
("Heimat",       "die","Heimaten",     ["homeland"],                 ["patrie","chez soi"],     ["pátria","terra natal"]),
("Nation",       "die","Nationen",     ["nation"],                   ["nation"],                ["nação"]),  # dedupe
("Grenze",       "die","Grenzen",      ["border"],                   ["frontière"],             ["fronteira"]),  # dedupe
("Volk",         "das","Völker",       ["people"],                   ["peuple"],                ["povo"]),  # dedupe
("Ritual",       "das","Rituale",      ["ritual"],                   ["rituel"],                ["ritual"]),
("Mythos",       "der","Mythen",       ["myth"],                     ["mythe"],                 ["mito"]),
("Legende",      "die","Legenden",     ["legend"],                   ["légende"],               ["lenda"]),
("Ideal",        "das","Ideale",       ["ideal"],                    ["idéal"],                 ["ideal"]),
("Fortschritt",  "der","Fortschritte", ["progress"],                 ["progrès"],               ["progresso"]),

# ============================================================
# LEVEL 19 — Religion & myth
# ============================================================
("Gott",         "der","Götter",       ["god"],                      ["dieu"],                  ["Deus","deus"]),
("Göttin",       "die","Göttinnen",    ["goddess"],                  ["déesse"],                ["deusa"]),
("Glaube",       "der","—",            ["faith","belief"],           ["foi","croyance"],        ["fé","crença"]),
("Religion",     "die","Religionen",   ["religion"],                 ["religion"],              ["religião"]),
("Kirche",       "die","Kirchen",      ["church"],                   ["église"],                ["igreja"]),  # dedupe
("Tempel",       "der","Tempel",       ["temple"],                   ["temple"],                ["templo"]),
("Moschee",      "die","Moscheen",     ["mosque"],                   ["mosquée"],               ["mesquita"]),
("Synagoge",     "die","Synagogen",    ["synagogue"],                ["synagogue"],             ["sinagoga"]),
("Priester",     "der","Priester",     ["priest"],                   ["prêtre"],                ["padre","sacerdote"]),
("Prophet",      "der","Propheten",    ["prophet"],                  ["prophète"],              ["profeta"]),
("Heiliger",     "der","Heiligen",     ["saint"],                    ["saint"],                 ["santo"]),
("Engel",        "der","Engel",        ["angel"],                    ["ange"],                  ["anjo"]),
("Teufel",       "der","Teufel",       ["devil"],                    ["diable"],                ["diabo"]),
("Dämon",        "der","Dämonen",      ["demon"],                    ["démon"],                 ["demônio"]),
("Seele",        "die","Seelen",       ["soul"],                     ["âme"],                   ["alma"]),  # dedupe
("Himmel",       "der","Himmel",       ["heaven"],                   ["paradis"],               ["céu","paraíso"]),  # dedupe
("Hölle",        "die","Höllen",       ["hell"],                     ["enfer"],                 ["inferno"]),
("Paradies",     "das","Paradiese",    ["paradise"],                 ["paradis"],               ["paraíso"]),
("Sünde",        "die","Sünden",       ["sin"],                      ["péché"],                 ["pecado"]),  # dedupe
("Gnade",        "die","Gnaden",       ["grace","mercy"],            ["grâce"],                 ["graça"]),
("Erlösung",     "die","—",            ["redemption","salvation"],   ["rédemption","salut"],    ["redenção","salvação"]),
("Heil",         "das","—",            ["salvation","well-being"],   ["salut"],                 ["salvação"]),
("Offenbarung",  "die","Offenbarungen",["revelation"],               ["révélation"],            ["revelação"]),
("Wunder",       "das","Wunder",       ["miracle"],                  ["miracle"],               ["milagre"]),
("Gebet",        "das","Gebete",       ["prayer"],                   ["prière"],                ["oração","prece"]),
("Ritus",        "der","Riten",        ["rite"],                     ["rite"],                  ["rito"]),
("Segen",        "der","—",            ["blessing"],                 ["bénédiction"],           ["bênção"]),
("Fluch",        "der","Flüche",       ["curse"],                    ["malédiction","juron"],   ["maldição","praga"]),
("Bibel",        "die","Bibeln",       ["Bible"],                    ["Bible"],                 ["Bíblia"]),
("Koran",        "der","Korane",       ["Quran"],                    ["Coran"],                 ["Alcorão"]),
("Tora",         "die","—",            ["Torah"],                    ["Torah"],                 ["Torá"]),
("Schöpfung",    "die","Schöpfungen",  ["creation"],                 ["création"],              ["criação"]),
("Schöpfer",     "der","Schöpfer",     ["creator"],                  ["créateur"],              ["criador"]),
("Christentum",  "das","—",            ["Christianity"],             ["christianisme"],         ["cristianismo"]),
("Islam",        "der","—",            ["Islam"],                    ["islam"],                 ["islã"]),
("Judentum",     "das","—",            ["Judaism"],                  ["judaïsme"],              ["judaísmo"]),
("Buddhismus",   "der","—",            ["Buddhism"],                 ["bouddhisme"],            ["budismo"]),
("Hinduismus",   "der","—",            ["Hinduism"],                 ["hindouisme"],            ["hinduísmo"]),
("Mystik",       "die","—",            ["mysticism"],                ["mystique"],              ["misticismo"]),
("Sakrament",    "das","Sakramente",   ["sacrament"],                ["sacrement"],             ["sacramento"]),

# ============================================================
# LEVEL 20 — World & science
# ============================================================
("Natur",        "die","Naturen",      ["nature"],                   ["nature"],                ["natureza"]),  # dedupe
("Universum",    "das","Universen",    ["universe"],                 ["univers"],               ["universo"]),
("Kosmos",       "der","Kosmen",       ["cosmos"],                   ["cosmos"],                ["cosmos"]),
("Galaxie",      "die","Galaxien",     ["galaxy"],                   ["galaxie"],               ["galáxia"]),
("Planet",       "der","Planeten",     ["planet"],                   ["planète"],               ["planeta"]),
("Atom",         "das","Atome",        ["atom"],                     ["atome"],                 ["átomo"]),
("Molekül",      "das","Moleküle",     ["molecule"],                 ["molécule"],              ["molécula"]),
("Element",      "das","Elemente",     ["element"],                  ["élément"],               ["elemento"]),
("Stoff",        "der","Stoffe",       ["substance","material"],     ["matière","substance"],   ["substância","matéria"]),
("Wissenschaftler","der","Wissenschaftler",["scientist"],            ["scientifique"],          ["cientista"]),
("Physik",       "die","—",            ["physics"],                  ["physique"],              ["física"]),
("Chemie",       "die","—",            ["chemistry"],                ["chimie"],                ["química"]),
("Biologie",     "die","—",            ["biology"],                  ["biologie"],              ["biologia"]),
("Mathematik",   "die","—",            ["mathematics"],              ["mathématiques"],         ["matemática"]),
("Astronomie",   "die","—",            ["astronomy"],                ["astronomie"],            ["astronomia"]),
("Geologie",     "die","—",            ["geology"],                  ["géologie"],              ["geologia"]),
("Ökologie",     "die","—",            ["ecology"],                  ["écologie"],              ["ecologia"]),
("Evolution",    "die","Evolutionen",  ["evolution"],                ["évolution"],             ["evolução"]),
("Art",          "die","Arten",        ["species"],                  ["espèce"],                ["espécie"]),  # dedupe
("Gattung",      "die","Gattungen",    ["genus","kind"],             ["genre"],                 ["gênero"]),
("Organismus",   "der","Organismen",   ["organism"],                 ["organisme"],             ["organismo"]),
("Zelle",        "die","Zellen",       ["cell"],                     ["cellule"],               ["célula"]),
("Gen",          "das","Gene",         ["gene"],                     ["gène"],                  ["gene"]),
("DNA",          "die","—",            ["DNA"],                      ["ADN"],                   ["DNA"]),
("Experiment",   "das","Experimente",  ["experiment"],               ["expérience"],            ["experimento"]),
("Beobachtung",  "die","Beobachtungen",["observation"],              ["observation"],           ["observação"]),
("Messung",      "die","Messungen",    ["measurement"],              ["mesure"],                ["medição"]),
("Theorie",      "die","Theorien",     ["theory"],                   ["théorie"],               ["teoria"]),  # dedupe
("Modell",       "das","Modelle",      ["model"],                    ["modèle"],                ["modelo"]),
("Formel",       "die","Formeln",      ["formula"],                  ["formule"],               ["fórmula"]),
("Daten",        "die","—",            ["data"],                     ["données"],               ["dados"]),
("Forschung",    "die","Forschungen",  ["research"],                 ["recherche"],             ["pesquisa"]),
("Entdeckung",   "die","Entdeckungen", ["discovery"],                ["découverte"],            ["descoberta"]),
("Erfindung",    "die","Erfindungen",  ["invention"],                ["invention"],             ["invenção"]),
("Technik",      "die","Techniken",    ["technology","technique"],   ["technique"],             ["técnica","tecnologia"]),
("Technologie",  "die","Technologien", ["technology"],               ["technologie"],           ["tecnologia"]),
("Maschine",     "die","Maschinen",    ["machine"],                  ["machine"],               ["máquina"]),  # dedupe
("Roboter",      "der","Roboter",      ["robot"],                    ["robot"],                 ["robô"]),
("Algorithmus",  "der","Algorithmen",  ["algorithm"],                ["algorithme"],            ["algoritmo"]),
("Information",  "die","Informationen",["information"],              ["information"],           ["informação"]),

# ============================================================
# LEVEL 21 — Phenomenology & hermeneutics
# ============================================================
("Phänomenologie","die","—",           ["phenomenology"],            ["phénoménologie"],        ["fenomenologia"]),
("Intentionalität","die","—",          ["intentionality"],           ["intentionnalité"],       ["intencionalidade"]),
("Bewusstseinsakt","der","Bewusstseinsakte",["act of consciousness"],["acte de conscience"],    ["ato de consciência"]),
("Noema",        "das","Noemata",      ["noema"],                    ["noème"],                 ["noema"]),
("Noesis",       "die","Noesen",       ["noesis"],                   ["noèse"],                 ["noesis"]),
("Epoché",       "die","—",            ["epoché","bracketing"],      ["épochè"],                ["epoché"]),
("Lebenswelt",   "die","Lebenswelten", ["lifeworld"],                ["monde vécu"],            ["mundo da vida"]),
("Horizont",     "der","Horizonte",    ["horizon"],                  ["horizon"],               ["horizonte"]),
("Verstehen",    "das","—",            ["understanding"],            ["compréhension"],         ["compreensão"]),
("Auslegung",    "die","Auslegungen",  ["interpretation"],           ["interprétation"],        ["interpretação"]),  # dedupe
("Deutung",      "die","Deutungen",    ["interpretation"],           ["interprétation"],        ["interpretação"]),
("Sinnstiftung", "die","—",            ["sense-making"],             ["donation de sens"],      ["produção de sentido"]),
("Vorverständnis","das","Vorverständnisse",["pre-understanding"],    ["pré-compréhension"],     ["pré-compreensão"]),
("Zeitlichkeit", "die","—",            ["temporality"],              ["temporalité"],           ["temporalidade"]),  # dedupe
("Geworfenheit", "die","—",            ["thrownness"],               ["être-jeté","déréliction"],["dejeção","estar-lançado"]),
("Entwurf",      "der","Entwürfe",     ["project","projection"],     ["projet"],                ["projeto"]),
("Man",          "das","—",            ["the they","the one"],       ["le on"],                 ["o impessoal"]),
("Angst",        "die","Ängste",       ["Angst","anxiety"],          ["angoisse"],              ["angústia"]),  # dedupe
("Gewissen",     "das","Gewissen",     ["conscience","call"],        ["conscience"],            ["consciência"]),  # dedupe
("Sorge",        "die","Sorgen",       ["care"],                     ["souci"],                 ["cuidado"]),  # dedupe
("Zuhandenheit", "die","—",            ["readiness-to-hand"],        ["être-à-portée-de-main"], ["ser à mão"]),
("Vorhandenheit","die","—",            ["presence-at-hand"],         ["être-là-devant"],        ["ser-simplesmente-dado"]),
("Ereignis",     "das","Ereignisse",   ["event","enowning"],         ["événement","avènement"], ["evento","acontecimento"]),  # dedupe
("Kehre",        "die","Kehren",       ["turn","reversal"],          ["tournant"],              ["viragem"]),
("Alterität",    "die","—",            ["alterity","otherness"],     ["altérité"],              ["alteridade"]),
("Andere",       "der","Anderen",      ["the Other"],                ["autrui"],                ["Outro"]),
("Antlitz",      "das","Antlitze",     ["face","countenance"],       ["visage"],                ["rosto","face"]),
("Begegnung",    "die","Begegnungen",  ["encounter"],                ["rencontre"],             ["encontro"]),
("Zeugnis",      "das","Zeugnisse",    ["testimony"],                ["témoignage"],            ["testemunho"]),
("Spur",         "die","Spuren",       ["trace"],                    ["trace"],                 ["rastro","vestígio"]),
("Differenz",    "die","Differenzen",  ["difference"],               ["différence"],            ["diferença"]),
("Wiederholung", "die","Wiederholungen",["repetition"],              ["répétition"],            ["repetição"]),
("Auslegungshorizont","der","Auslegungshorizonte",["interpretive horizon"],["horizon interprétatif"],["horizonte interpretativo"]),
("Applikation",  "die","Applikationen",["application"],              ["application"],           ["aplicação"]),
("Vermittlung",  "die","Vermittlungen",["mediation"],                ["médiation"],             ["mediação"]),
("Ausdrucksgestalt","die","Ausdrucksgestalten",["expressive form"],  ["forme expressive"],      ["forma expressiva"]),
("Wirkungsgeschichte","die","—",       ["effective history"],        ["histoire des effets"],   ["história dos efeitos"]),
("Horizontverschmelzung","die","—",    ["fusion of horizons"],       ["fusion des horizons"],   ["fusão de horizontes"]),
("Leiblichkeit", "die","—",            ["embodiment","corporeity"],  ["corporéité"],            ["corporeidade"]),
("Fleisch",      "das","—",            ["flesh"],                    ["chair"],                 ["carne"]),

# ============================================================
# LEVEL 22 — Critical theory & modernity
# ============================================================
("Kritik",       "die","Kritiken",     ["critique","criticism"],     ["critique"],              ["crítica"]),  # dedupe
("Aufklärung",   "die","—",            ["Enlightenment"],            ["Lumières"],              ["Iluminismo"]),  # dedupe
("Vernunft",     "die","—",            ["reason"],                   ["raison"],                ["razão"]),  # dedupe
("Instrumentelle Vernunft","die","—",  ["instrumental reason"],      ["raison instrumentale"],  ["razão instrumental"]),
("Dialektik",    "die","Dialektiken",  ["dialectic"],                ["dialectique"],           ["dialética"]),
("Widerspruch",  "der","Widersprüche", ["contradiction"],            ["contradiction"],         ["contradição"]),  # dedupe
("Negation",     "die","Negationen",   ["negation"],                 ["négation"],              ["negação"]),
("Aufhebung",    "die","—",            ["sublation"],                ["Aufhebung","dépassement"],["superação","sublação"]),
("Entfremdung",  "die","Entfremdungen",["alienation"],               ["aliénation"],            ["alienação"]),
("Verdinglichung","die","—",           ["reification"],              ["réification"],           ["reificação"]),
("Ideologie",    "die","Ideologien",   ["ideology"],                 ["idéologie"],             ["ideologia"]),  # dedupe
("Falsches Bewusstsein","das","—",     ["false consciousness"],      ["fausse conscience"],     ["falsa consciência"]),
("Klassenkampf", "der","Klassenkämpfe",["class struggle"],           ["lutte des classes"],     ["luta de classes"]),
("Proletariat",  "das","—",            ["proletariat"],              ["prolétariat"],           ["proletariado"]),
("Bourgeoisie",  "die","Bourgeoisien", ["bourgeoisie"],              ["bourgeoisie"],           ["burguesia"]),
("Kapital",      "das","Kapitalien",   ["capital"],                  ["capital"],               ["capital"]),
("Ware",         "die","Waren",        ["commodity","good"],         ["marchandise"],           ["mercadoria"]),
("Warenfetisch", "der","—",            ["commodity fetish"],         ["fétichisme de la marchandise"],["fetichismo da mercadoria"]),
("Mehrwert",     "der","—",            ["surplus value"],            ["plus-value"],            ["mais-valia"]),
("Arbeit",       "die","—",            ["labor"],                    ["travail"],               ["trabalho"]),  # dedupe
("Ausbeutung",   "die","—",            ["exploitation"],             ["exploitation"],          ["exploração"]),
("Herrschaft",   "die","—",            ["domination"],               ["domination"],            ["dominação"]),  # dedupe
("Emanzipation", "die","Emanzipationen",["emancipation"],            ["émancipation"],          ["emancipação"]),  # dedupe
("Öffentlichkeit","die","—",           ["public sphere"],            ["espace public"],         ["esfera pública"]),
("Diskurs",      "der","Diskurse",     ["discourse"],                ["discours"],              ["discurso"]),  # dedupe
("Kommunikation","die","Kommunikationen",["communication"],          ["communication"],         ["comunicação"]),
("Handlung",     "die","Handlungen",   ["action"],                   ["action"],                ["ação"]),
("Kulturindustrie","die","—",          ["culture industry"],         ["industrie culturelle"],  ["indústria cultural"]),
("Kunstwerk",    "das","Kunstwerke",   ["artwork"],                  ["œuvre d'art"],           ["obra de arte"]),  # dedupe
("Aura",         "die","Auren",        ["aura"],                     ["aura"],                  ["aura"]),
("Reproduktion", "die","Reproduktionen",["reproduction"],            ["reproduction"],          ["reprodução"]),
("Postmoderne",  "die","—",            ["postmodernity"],            ["postmodernité"],         ["pós-modernidade"]),
("Struktur",     "die","Strukturen",   ["structure"],                ["structure"],             ["estrutura"]),  # dedupe
("Dekonstruktion","die","Dekonstruktionen",["deconstruction"],       ["déconstruction"],        ["desconstrução"]),
("Genealogie",   "die","Genealogien",  ["genealogy"],                ["généalogie"],            ["genealogia"]),
("Panoptikum",   "das","Panoptika",    ["panopticon"],               ["panoptique"],            ["panóptico"]),
("Disziplin",    "die","Disziplinen",  ["discipline"],               ["discipline"],            ["disciplina"]),
("Biopolitik",   "die","—",            ["biopolitics"],              ["biopolitique"],          ["biopolítica"]),
("Machtwissen",  "das","—",            ["power-knowledge"],          ["pouvoir-savoir"],        ["poder-saber"]),
("Hegemonie",    "die","Hegemonien",   ["hegemony"],                 ["hégémonie"],             ["hegemonia"]),

# ============================================================
# LEVEL 23 — Psychology & inner life
# ============================================================
("Psyche",       "die","Psychen",      ["psyche"],                   ["psyché"],                ["psique"]),
("Psychologie",  "die","Psychologien", ["psychology"],               ["psychologie"],           ["psicologia"]),
("Psychoanalyse","die","Psychoanalysen",["psychoanalysis"],          ["psychanalyse"],          ["psicanálise"]),
("Verdrängung",  "die","Verdrängungen",["repression"],               ["refoulement"],           ["recalque","repressão"]),
("Übertragung",  "die","Übertragungen",["transference"],             ["transfert"],             ["transferência"]),
("Es",           "das","—",            ["id"],                       ["ça"],                    ["id"]),
("Über-Ich",     "das","—",            ["superego"],                 ["surmoi"],                ["superego"]),
("Libido",       "die","—",            ["libido"],                   ["libido"],                ["libido"]),
("Trieb",        "der","Triebe",       ["drive","instinct"],         ["pulsion"],               ["pulsão"]),  # dedupe
("Todestrieb",   "der","Todestriebe",  ["death drive"],              ["pulsion de mort"],       ["pulsão de morte"]),
("Trauma",       "das","Traumata",     ["trauma"],                   ["trauma"],                ["trauma"]),
("Neurose",      "die","Neurosen",     ["neurosis"],                 ["névrose"],               ["neurose"]),
("Psychose",     "die","Psychosen",    ["psychosis"],                ["psychose"],              ["psicose"]),
("Melancholie",  "die","—",            ["melancholy"],               ["mélancolie"],            ["melancolia"]),
("Depression",   "die","Depressionen", ["depression"],               ["dépression"],            ["depressão"]),
("Manie",        "die","Manien",       ["mania"],                    ["manie"],                 ["mania"]),
("Zwang",        "der","Zwänge",       ["compulsion"],               ["contrainte"],            ["compulsão"]),  # dedupe
("Schock",       "der","Schocks",      ["shock"],                    ["choc"],                  ["choque"]),
("Anspannung",   "die","Anspannungen", ["tension","strain"],         ["tension"],               ["tensão"]),
("Entspannung",  "die","—",            ["relaxation"],               ["détente","relaxation"],  ["relaxamento"]),
("Erlebnis",     "das","Erlebnisse",   ["experience","event"],       ["vécu"],                  ["vivência"]),  # dedupe
("Gefühlswelt",  "die","Gefühlswelten",["emotional world"],          ["monde émotionnel"],      ["mundo emocional"]),
("Persönlichkeit","die","Persönlichkeiten",["personality"],          ["personnalité"],          ["personalidade"]),
("Charakter",    "der","Charaktere",   ["character"],                ["caractère"],             ["caráter"]),
("Temperament",  "das","Temperamente", ["temperament"],              ["tempérament"],           ["temperamento"]),
("Verhalten",    "das","—",            ["behavior"],                 ["comportement"],          ["comportamento"]),
("Motiv",        "das","Motive",       ["motive"],                   ["motif"],                 ["motivo"]),  # dedupe
("Bedürfnis",    "das","Bedürfnisse",  ["need"],                     ["besoin"],                ["necessidade"]),
("Verlangen",    "das","Verlangen",    ["longing","craving"],        ["envie","désir"],         ["anseio","desejo"]),
("Sucht",        "die","Süchte",       ["addiction"],                ["dépendance","toxicomanie"],["dependência","vício"]),
("Reiz",         "der","Reize",        ["stimulus"],                 ["stimulus"],              ["estímulo"]),
("Reaktion",     "die","Reaktionen",   ["reaction"],                 ["réaction"],              ["reação"]),
("Konditionierung","die","Konditionierungen",["conditioning"],       ["conditionnement"],       ["condicionamento"]),
("Selbstwert",   "der","—",            ["self-worth"],               ["estime de soi"],         ["autoestima"]),
("Selbstbild",   "das","Selbstbilder", ["self-image"],               ["image de soi"],          ["autoimagem"]),
("Ego",          "das","Egos",         ["ego"],                      ["ego"],                   ["ego"]),
("Introvertiertheit","die","—",        ["introversion"],             ["introversion"],          ["introversão"]),
("Extrovertiertheit","die","—",        ["extraversion"],             ["extraversion"],          ["extroversão"]),
("Empathie",     "die","—",            ["empathy"],                  ["empathie"],              ["empatia"]),
("Sympathie",    "die","Sympathien",   ["sympathy"],                 ["sympathie"],              ["simpatia"]),

# ============================================================
# LEVEL 24 — Economy, law & justice
# ============================================================
("Wirtschaft",   "die","Wirtschaften", ["economy"],                  ["économie"],              ["economia"]),
("Markt",        "der","Märkte",       ["market"],                   ["marché"],                ["mercado"]),  # dedupe
("Angebot",      "das","Angebote",     ["offer","supply"],           ["offre"],                 ["oferta"]),
("Nachfrage",    "die","Nachfragen",   ["demand"],                   ["demande"],               ["procura","demanda"]),
("Kapital",      "das","Kapitalien",   ["capital"],                  ["capital"],               ["capital"]),  # dedupe
("Eigentum",     "das","—",            ["property","ownership"],     ["propriété"],             ["propriedade"]),
("Besitz",       "der","—",            ["possession"],               ["possession"],            ["posse"]),
("Ware",         "die","Waren",        ["good","commodity"],         ["marchandise"],           ["mercadoria"]),  # dedupe
("Preis",        "der","Preise",       ["price"],                    ["prix"],                  ["preço"]),  # dedupe
("Wert",         "der","Werte",        ["value"],                    ["valeur"],                ["valor"]),  # dedupe
("Gewinn",       "der","Gewinne",      ["profit","win"],             ["profit","gain"],         ["lucro","ganho"]),
("Verlust",      "der","Verluste",     ["loss"],                     ["perte"],                 ["perda"]),
("Investition",  "die","Investitionen",["investment"],               ["investissement"],        ["investimento"]),
("Rendite",      "die","Renditen",     ["yield","return"],           ["rendement"],             ["retorno","rendimento"]),
("Schulden",     "die","—",            ["debts"],                    ["dettes"],                ["dívidas"]),
("Zins",         "der","Zinsen",       ["interest"],                 ["intérêt"],               ["juros"]),
("Inflation",    "die","Inflationen",  ["inflation"],                ["inflation"],             ["inflação"]),
("Rezession",    "die","Rezessionen",  ["recession"],                ["récession"],             ["recessão"]),
("Wachstum",     "das","—",            ["growth"],                   ["croissance"],            ["crescimento"]),
("Armut",        "die","—",            ["poverty"],                  ["pauvreté"],              ["pobreza"]),
("Reichtum",     "der","Reichtümer",   ["wealth"],                   ["richesse"],              ["riqueza"]),
("Vermögen",     "das","Vermögen",     ["fortune","assets"],         ["fortune","biens"],       ["fortuna","patrimônio"]),
("Steuer",       "die","Steuern",      ["tax"],                      ["impôt"],                 ["imposto"]),  # dedupe
("Zoll",         "der","Zölle",        ["tariff","customs"],         ["douane","tarif"],        ["alfândega","tarifa"]),
("Vertrag",      "der","Verträge",     ["contract","treaty"],        ["contrat","traité"],      ["contrato","tratado"]),  # dedupe
("Klage",        "die","Klagen",       ["lawsuit","complaint"],      ["plainte","poursuite"],   ["queixa","processo"]),
("Urteil",       "das","Urteile",      ["verdict","judgement"],      ["jugement","verdict"],    ["sentença","julgamento"]),  # dedupe
("Prozess",      "der","Prozesse",     ["trial","process"],          ["procès","processus"],    ["processo"]),
("Anwalt",       "der","Anwälte",      ["lawyer","attorney"],        ["avocat"],                ["advogado"]),
("Richter",      "der","Richter",      ["judge"],                    ["juge"],                  ["juiz"]),
("Gericht",      "das","Gerichte",     ["court","tribunal"],         ["tribunal","cour"],       ["tribunal","corte"]),
("Verbrechen",   "das","Verbrechen",   ["crime"],                    ["crime"],                 ["crime"]),
("Strafe",       "die","Strafen",      ["punishment"],               ["punition","peine"],      ["punição","pena"]),
("Menschenrechte","die","—",           ["human rights"],             ["droits de l'homme"],     ["direitos humanos"]),
("Rechtsstaat",  "der","Rechtsstaaten",["rule of law"],              ["État de droit"],         ["Estado de direito"]),
("Verfassung",   "die","Verfassungen", ["constitution"],             ["constitution"],          ["constituição"]),  # dedupe
("Gerichtsbarkeit","die","Gerichtsbarkeiten",["jurisdiction"],       ["juridiction"],           ["jurisdição"]),
("Verantwortung","die","Verantwortungen",["accountability","responsibility"],["responsabilité"], ["responsabilidade"]),  # dedupe
("Gerechtigkeit","die","—",            ["justice"],                  ["justice"],               ["justiça"]),  # dedupe
("Sozialstaat",  "der","Sozialstaaten",["welfare state"],            ["État-providence"],       ["Estado de bem-estar"]),

# ============================================================
# LEVEL 25 — Metaphysical & theological
# ============================================================
("Absolute",     "das","—",            ["the absolute"],             ["l'absolu"],              ["o absoluto"]),
("Transzendenz", "die","Transzendenzen",["transcendence"],           ["transcendance"],         ["transcendência"]),
("Immanenz",     "die","Immanenzen",   ["immanence"],                ["immanence"],             ["imanência"]),
("Universalie",  "die","Universalien", ["universal"],                ["universel"],             ["universal"]),
("Partikulare",  "das","—",            ["particular"],               ["particulier"],           ["particular"]),
("Endzweck",     "der","Endzwecke",    ["final purpose"],            ["fin ultime"],            ["fim último"]),
("Teleologie",   "die","Teleologien",  ["teleology"],                ["téléologie"],            ["teleologia"]),
("Vorsehung",    "die","—",            ["providence"],               ["providence"],            ["providência"]),
("Schicksal",    "das","Schicksale",   ["fate","destiny"],           ["destin","fatalité"],     ["destino"]),
("Bestimmung",   "die","Bestimmungen", ["destination","vocation"],   ["destination","vocation"],["destinação","vocação"]),
("Ewigkeit",     "die","Ewigkeiten",   ["eternity"],                 ["éternité"],              ["eternidade"]),  # dedupe
("Unsterblichkeit","die","—",          ["immortality"],              ["immortalité"],           ["imortalidade"]),
("Sterblichkeit","die","—",            ["mortality"],                ["mortalité"],             ["mortalidade"]),
("Erhabene",     "das","—",            ["the sublime"],              ["le sublime"],            ["o sublime"]),
("Numen",        "das","Numina",       ["numen"],                    ["numen"],                 ["numen"]),
("Heilige",      "das","—",            ["the sacred","the holy"],    ["le sacré"],              ["o sagrado"]),
("Profane",      "das","—",            ["the profane"],              ["le profane"],            ["o profano"]),
("Mysterium",    "das","Mysterien",    ["mystery"],                  ["mystère"],               ["mistério"]),
("Geheimnis",    "das","Geheimnisse",  ["secret","mystery"],         ["secret","mystère"],      ["segredo","mistério"]),
("Kontingenz",   "die","Kontingenzen", ["contingency"],              ["contingence"],           ["contingência"]),
("Notwendigkeit","die","—",            ["necessity"],                ["nécessité"],             ["necessidade"]),  # dedupe
("Freiheit",     "die","Freiheiten",   ["freedom"],                  ["liberté"],               ["liberdade"]),  # dedupe
("Prädestination","die","—",           ["predestination"],           ["prédestination"],        ["predestinação"]),
("Rechtfertigung","die","Rechtfertigungen",["justification"],        ["justification"],         ["justificação"]),
("Heilsgeschichte","die","—",          ["salvation history"],        ["histoire du salut"],     ["história da salvação"]),
("Apokalypse",   "die","Apokalypsen",  ["apocalypse"],               ["apocalypse"],            ["apocalipse"]),
("Eschatologie", "die","Eschatologien",["eschatology"],              ["eschatologie"],          ["escatologia"]),
("Dreieinigkeit","die","—",            ["Trinity"],                  ["Trinité"],               ["Trindade"]),
("Inkarnation",  "die","Inkarnationen",["incarnation"],              ["incarnation"],           ["encarnação"]),
("Auferstehung", "die","Auferstehungen",["resurrection"],            ["résurrection"],          ["ressurreição"]),
("Sündenfall",   "der","—",            ["Fall","original sin"],      ["chute","péché originel"],["queda","pecado original"]),
("Erbsünde",     "die","—",            ["original sin"],             ["péché originel"],        ["pecado original"]),
("Gebot",        "das","Gebote",       ["commandment"],              ["commandement"],          ["mandamento"]),  # dedupe
("Bund",         "der","Bünde",        ["covenant","alliance"],      ["alliance"],              ["aliança","pacto"]),
("Theodizee",    "die","Theodizeen",   ["theodicy"],                 ["théodicée"],             ["teodiceia"]),
("Ontologie",    "die","Ontologien",   ["ontology"],                 ["ontologie"],             ["ontologia"]),
("Metaphysik",   "die","Metaphysiken", ["metaphysics"],              ["métaphysique"],          ["metafísica"]),
("Kosmogonie",   "die","Kosmogonien",  ["cosmogony"],                ["cosmogonie"],            ["cosmogonia"]),
("Weltgeist",    "der","—",            ["world-spirit"],             ["esprit du monde"],       ["espírito do mundo"]),
("Absolutes Wissen","das","—",         ["absolute knowledge"],       ["savoir absolu"],         ["saber absoluto"]),
]

# --- generate noun-data.js ---
import json, os, re

def esc(s):
    return json.dumps(s, ensure_ascii=False)

def to_js():
    out = ["window.NOUNS_DATA = ["]
    for row in NOUNS:
        de, art, pl, en, fr, pt = row
        en_s = "[" + ",".join(esc(w) for w in en) + "]"
        fr_s = "[" + ",".join(esc(w) for w in fr) + "]"
        pt_s = "[" + ",".join(esc(w) for w in pt) + "]"
        out.append(f'  {{de:{esc(de)},art:{esc(art)},pl:{esc(pl)},en:{en_s},fr:{fr_s},pt:{pt_s}}},')
    out.append("];")
    return "\n".join(out) + "\n"

def audit():
    seen = {}
    dupes = []
    for i, row in enumerate(NOUNS):
        de = row[0]
        if de in seen:
            dupes.append((de, seen[de], i))
        else:
            seen[de] = i
    return dupes

if __name__ == "__main__":
    dupes = audit()
    print(f"total: {len(NOUNS)}")
    print(f"duplicates: {len(dupes)}")
    for d, i, j in dupes[:20]:
        print(f"  {d}: positions {i} and {j}")
    # write js
    here = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(here, "noun-data.js")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(to_js())
    print(f"wrote {out_path}")
