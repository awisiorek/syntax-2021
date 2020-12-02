from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice, OpenTextfield
from questions import single, multiple, offen, selection, luecke

blatt5_2 = [
    [Lueckentext("Bei nicht allen Satzgliedern, die vom Verb abhängen handelt es sich um Ergänzungen. Die PP <i> mit der S-Bahn </i> stellt eine Angabe dar. ", {"nicht":[], "PP":["NP", "VP"], "Angabe":["Ergänzung"]})],
    [MultipleChoice("Mit welchen Tests kann die Funktion des obrigen Satzgliedes <i> mit der S-Bahn </i> festgestellt werden?", correct=["Weglassbarkeitstest", "geschehen-Test"], wrong=["Adverbialsatz-Test"])],
    [MultipleChoice("Bei welchen Sätzen wurden die Tests richtig angewendet?", correct=["Die neue Kollegin fährt zu ihrem neuen Arbeitsplatz.", "Die neue Kollegin fährt zu ihrem neuen Arbeitsplatz, und das geschieht mit der S-Bahn."], wrong=[])] 
]

blatt5_3b = [
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> fährt </i>.", correct=["Kollegin", "mit", "zu"], wrong=["der", "die", "S-Bahn", "neue", "Arbeitsplatz", "ihrem", "Es gibt keine."])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> Kollegin </i>.", correct=["die", "neue"], wrong=["der", "fährt", "S-Bahn", "Arbeitsplatz", "ihrem", "Kollegin", "mit", "zu", "Es gibt keine."])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> mit </i>.", correct=["S-Bahn"], wrong=["der", "fährt", "die", "neue", "Arbeitsplatz", "ihrem", "Kollegin", "zu", "Es gibt keine."])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> ihrem </i>.", correct=["Es gibt keine."], wrong=["der", "fährt", "die", "neue", "Arbeitsplatz", "Kollegin", "mit", "zu", "S-Bahn"])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> S-Bahn </i>.", correct=["der"],
                    wrong=["fährt", "die", "S-Bahn", "neue", "Arbeitsplatz", "ihrem", "Kollegin", "zu", "Es gibt keine."])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> Arbeitsplatz </i>.", correct=["ihrem", "neuen"],
                    wrong=["fährt", "die", "S-Bahn", "Arbeitsplatz", "Kollegin", "mit", "zu", "Es gibt keine."])]
]

blatt5_9b = [
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> kenne </i>.", correct=["Ich", "Bruder"], wrong=["einen", "älteren", "von", "Mädchen", "zwei", "lebhaften", "sehr", "Es gibt keine."])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> Bruder </i>.", correct=["einen", "älteren", "Mädchen"],
                    wrong=["zwei", "lebhaften", "sehr", "Ich", "Bruder", "Es gibt keine.", "kenne"])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> von </i>.", correct=["Es gibt keine."],
                    wrong=["einen", "älteren", "von", "zwei", "lebhaften", "sehr", "Ich", "Bruder",
                           "kenne", "Mädchen"])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> zwei </i>.", correct=["Es gibt keine."],
                    wrong=["einen", "älteren", "von", "zwei", "lebhaften", "sehr", "Ich", "Bruder", "Mädchen",
                           "kenne"])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> sehr </i>.", correct=["Es gibt keine."],
                    wrong=["einen", "älteren", "von", "Mädchen", "zwei", "lebhaften", "Ich", "Bruder", "kenne"])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> lebhaften </i>.", correct=["sehr"],
                    wrong=["einen", "älteren", "von", "Mädchen", "zwei", "lebhaften", "Ich", "Bruder", "Es gibt keine.", "kenne"])],
    [MultipleChoice("Markieren Sie alle direkten Dependenten des Wortes <i> Mädchen </i>.", correct=["zwei", "lebhaften", "von"],
                    wrong=["einen", "älteren", "Mädchen", "sehr", "Ich", "Bruder", "Es gibt keine.", "kenne"])]
]

blatt5_3d = [
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> Kollegin </i> und <i> die </i> ?", "det", "amod", "nsubj", "prep", "pcomp", "Keine")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> Kollegin </i> und <i> neue </i> ?", "amod", "det", "nsubj", "prep", "pcomp", "Keine")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> Kollegin </i> und <i> S-Bahn </i> ?", "Keine", "det", "amod", "nsubj", "prep", "pcomp")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> fährt </i> und <i> Kollegin </i> ?", "nsubj", "det", "amod", "prep", "pcomp", "Keine")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> fährt </i> und <i> zu </i> ?", "prep", "nsubj", "det", "amod", "pcomp", "Keine")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> fährt </i> und <i> ihrem </i> ?", "Keine", "nsubj", "det", "amod", "prep", "pcomp")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> mit </i> und <i> S-Bahn </i> ?", "pcomp", "nsubj", "det", "amod", "prep", "Keine")]
]

blatt5_9d = [
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> Bruder </i> und <i> einen </i> ?", "det", "amod", "nmod", "nsubj", "case", "nummod", "advmod", "Keine")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> Bruder </i> und <i> älteren </i> ?", "amod", "det", "nsubj", "nmod", "case", "advmod", "nummod", "Keine")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> Bruder </i> und <i> Mädchen </i> ?", "nmod", "det", "amod", "nsubj", "case", "nummod", "Keine", "advmod")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> kenne </i> und <i> ich </i> ?", "nsubj", "det", "amod", "nmod", "advmod", "nummod", "case", "Keine")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> Bruder </i> und <i> von </i> ?", "Keine", "nsubj", "det", "advmod", "nmod", "amod", "nummod", "Keine")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> lebhaften </i> und <i> sehr </i> ?", "advmod", "nmod", "case", "Keine", "nsubj", "det", "amod", "nummod")],
    [SingleChoice("Welche Art von Dependenz besteht zwischen <i> zwei </i> und <i> Bruder </i> ?", "Keine", "nsubj", "det", "amod", "nmod", "case", "nummod", "advmod")]
]



blatt5_3e = [
    [SingleChoice("Welche Art von Dependenz besteht jetzt zwischen <i> fährt </i> und <i> Kollegin </i> ?", "nsubj", "det", "amod", "prep", "pcomp", "Keine", "case", "obl")],
    [SingleChoice("Welche Art von Dependenz besteht jetzt zwischen <i> fährt </i> und <i> zu </i> ?", "Keine", "case", "obl", "prep", "nsubj", "det", "amod", "pcomp")],
    [SingleChoice("Welche Art von Dependenz besteht jetzt zwischen <i> fährt </i> und <i> Arbeitsplatz </i> ?", "obl", "case", "Keine", "nsubj", "det", "amod", "prep", "pcomp")],
    [SingleChoice("Welche Art von Dependenz besteht jetzt zwischen <i> mit </i> und <i> S-Bahn </i> ?", "case", "obl", "pcomp", "nsubj", "det", "amod", "prep", "Keine")]
]

blatt5_3f = [
    [MultipleChoice("Welche Konstituenten lassen sich am Dependenzbaum direkt ablesen?", correct=["die neue Kollegin", "mit der S-Bahn", "ihrem neuen Arbeitsplatz", "zu ihrem neuen Arbeitsplatz", "Die neue Kollegin fährt mit der S-Bahn zu ihrem neuen Arbeitsplatz", "der S-Bahn"], wrong=["fährt mit der S-Bahn zu ihrem neuen Arbeitsplatz"])]
]

blatt5_4 = [
    [SingleChoice("Um welchen Attributtyp handelt es sich bei dem Attribut <i>lang ersehnte</i>?", "Adjektivattribut", "Genitivattribut", "präpositionales Attribut", "attributiver Relativsatz")],
    [SingleChoice("Um welchen Attributtyp handelt es sich bei dem Attribut <i>der Klasse 5b</i>?", "Genitivattribut", "Adjektivattribut", "präpositionales Attribut", "attributiver Relativsatz")],
    [SingleChoice("Um welchen Attributtyp handelt es sich bei dem Attribut <i>nach Paris</i>?", "präpositionales Attribut", "Genitivattribut", "Adjektivattribut", "attributiver Relativsatz")],
    [SingleChoice("Um welchen Attributtyp handelt es sich bei dem Attribut <i>die sich aus irgendeinem Grunde immer wieder verzögert hatte</i>?", "attributiver Relativsatz", "präpositionales Attribut", "Genitivattribut", "Adjektivattribut")]
]

blatt5_5 = [
    [Lueckentext("Die Wortgruppe <i> sehr_gut </i> stellt im Satz ein Modaladverbial dar. Dieses Adverbial wird als Adjektivphrase realisiert. Innerhalb der Adjektivphrase tritt ein Adverb auf, das Wort <i> sehr </i>. Das Wort teilt mit anderen Wörtern derselben Klasse formale Eigenschaften. Die Bezeichnung \" Adverbial \" gibt die Satzgliedfunktion an. Diese lässt sich immer nur im konkreten Satz bestimmen.", {"Adverb":["Adverbial"], "Adverbial":["Adverb"], "Modaladverbial":["Lokaladverbial", "Modaladverb", "Lokaladverb"], "sehr":["gut"], "Adjektivphrase":["Nominalphrase", "Präpositionalphrase"]})]
]

blatt5_6 = [
    [MultipleChoice("Was sind Identifikationskriterien für das Subjekt?", correct=["Agenseigenschaften", "drückt häufig das Topik aus", "Kongruenz mit Verb", "steht im Nominativ"], wrong=["Patienseigenschaften", "steht im Akkusativ", "Kongruenz mit Artikel"])],
    [MultipleChoice("Was gilt <b>nicht</b> für die NP <i> ein Fehler </i> ?", correct=["Agenseigenschaften", "drückt das Topik aus"], wrong=["Patienseigenschaften", "Verb kongruiert mit NP", "steht im Nominativ"])],
    [MultipleChoice("Was spricht dafür, dass es sich bei <i> ein Fehler </i> eher um ein Objekt handelt?", correct=["Patienseigenschaften", "drückt nicht das Topik aus"], wrong=["Verb kongruiert mit NP", "steht im Nominativ", "Agenseigenschaften"])]
]

blatt5_7a = [
    [MultipleChoice("Welche Gründe sprechen für eine Klassifizierung als direktes Objekt?", correct=["unmittelbare Nachbarschaft zum Verb", "Distanzstellung nur bedingt möglich (<i>..dass man ihn des Diebstahls endlich überführt hat</i>)"], wrong=["Genitivmarkierung"])],
    [MultipleChoice("Welche im Deutschen für das Objekt typische Kriterien werden dagegen nicht erfüllt?", correct=["Passivierbarkeit", "Akkusativmarkierung"], wrong=["Relativierbarkeit (<i>..der Diebstahl, dessen man ihn endlich überführt hat</i>)"])],
]

blatt5_7b = [
    [SingleChoice("Im Englischen wird das indirekte Objekt __________. ", "präpositional angeschlossen", "kasusmarkiert")],
    [SingleChoice("Im Deutschen wird das indirekte Objekt __________. ", "kasusmarkiert", "präpositional angeschlossen")]
]

blatt5_8a = [
    [Lueckentext("Laut Weglassbarkeitstest ist die Entscheidung \"weglassbar\" gleichbedeutend damit, dass es sich um eine Angabe handelt.", {"Angabe":["Ergänzung"]})],
    [SingleChoice("Schlägt der Adverbialsatz-Test fehl, so handelt es sich um eine:", "Ergänzung", "Angabe")],
    [SingleChoice("Schlägt der geschehen-Test fehl, so handelt es sich um eine:", "Ergänzung", "Angabe")],

    [MultipleChoice("Welche Tests ergeben, dass es sich bei <i> auf das Pferd </i> im 1. Satz um eine Angabe handelt?", correct=[], wrong=["Adverbialsatz-Test", "Weglassbarkeitstest", "geschehen-Test"])],
    [MultipleChoice("Welche Tests ergeben, dass es sich bei <i> das Pferd </i> im 2. Satz um eine Angabe handelt?", correct=[], wrong=["Weglassbarkeitstest", "geschehen-Test", "Adverbialsatz-Test"])],
    [MultipleChoice("Welche Tests ergeben, dass es sich bei <i> das Pferd </i> im 3. Satz um eine Angabe handelt?", correct=["Weglassbarkeitstest"], wrong=["Adverbialsatz-Test", "geschehen-Test"])],
]

blatt5_8b = [
    [MultipleChoice("Unter der Annahmen, dass alle präpositional angeschlossenen Glieder Angaben sind: in welchen der Sätze ist das in Frage stehende Satzglied eine Angabe?", correct=["1. Satz (auf das Pferd)"], wrong=["2. Satz (das Pferd)", "3. Satz (das Pferd)"])],
    [MultipleChoice("Unter der Annahmen, dass alle Adverbiale Angaben sind: in welchen der Sätze ist das in Frage stehende Satzglied eine Angabe?", correct=["1. Satz (auf das Pferd)"], wrong=["2. Satz (das Pferd)", "3. Satz (das Pferd)"])],

    [SingleChoice("Wie könnte man abschließend das in Frage stehende Satzglied in Satz 1 charakterisieren?", "adverbiale Ergänzung", "Angabe", "fakultative Ergänzung")],
    [SingleChoice("Wie könnte man abschließend das in Frage stehende Satzglied in Satz 2 charakterisieren?", "Ergänzung", "Angabe")],
    [SingleChoice("Wie könnte man abschließend das in Frage stehende Satzglied in Satz 3 charakterisieren?", "fakultative Ergänzung", "Angabe", "adverbiale Ergänzung")],

]


blatt5_10 = [
    [SingleChoice("Handelt es sich im Satz bei der Präpositionalphrase um ein präpositionales Objekt?", "Ja", "Nein")],
    [MultipleChoice("Wieso?", correct=["fehlende Austauschbarkeit", "keine Eigensemantik", "vom Verb gefordert"], wrong=["austauschbar","trägt Eigensemantik"])]
]

blatt5_11 = [
    [Lueckentext("Im Satz hängen sowohl das Subjekt <i> Peter </i> als auch das Modaladverbial <i> gerne </i> und das Lokaladverbial <i> im Zelt </i> vom Verb <i> schlafen </i> ab, sind also Dependentien des Verbs .",{"Dependentien":["Valenzen"], "Subjekt":["Objekt"], "Modaladverbial":["Lokaladverbial"], "Lokaladverbial":["Modaladverbial"]})],
    [Lueckentext("Doch nur das Subjekt gehört zur Valenz von <i> schlafen </i>. Die Valenz bezieht sich auf die Verbindungsfähigkeit von relationalen Wörtern (Verben, Adjektiven, Substantiven), während die Dependenz Abhängigkeitsbeziehungen verschiedener Art zusammenfasst.", {"Valenz":["Dependenz"], "Dependenz":["Valenz"], "Subjekt":["Modaladverbial", "Lokaladverbial"]})]
]

blatt5_13a =[
    [MultipleChoice("Welche Kriterien stimmen?", correct=["H bestimmt die Distributionsklassen von C", "H ist obligatorisch, D kann optional sein", "H wählt D aus", "H bestimmt die morphologische Form von D", "H bestimmt den semantischen Typ von C"], wrong=["H und D sind optional"])]
]

blatt5_13b = [
    [MultipleChoice("Wie läßt sich die Einführung von einem Nicht-Terminal TV für transitive Verben (usw.) interpretieren?", correct=["Modellierung von Subkategorisierung der syntaktischen Kategorie V durch Kategorienerweiterung"], wrong=["Modellierung eines Subkategorisierungsrahmens über Merkmale im Lexikoneintrag"])]
]