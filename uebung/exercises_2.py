from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice
from questions import single, multiple, offen, selection, luecke





blatt2_1a = [
    [SingleChoice("Warum gibt die parse-Funktion des Skripts vermutlich eine Sequenz zurück?", "strukturelle Ambiguität", "lexikalische Ambiguität", "Übergenerierung", sonst=True, inst= single)],
    [SingleChoice("Die Alternative <code>tree = parser.parse(sent)</code> ist weniger wünschenswert, da im Allgemeinen ________ Parse-Tree möglich ist.", "mehr als ein", "genau ein", sonst=False, inst=single)]
    ]

blatt2_1b = [
    [MultipleChoice("Zu welcher Phrase kann die Präpositionalphrase \"in my pajamas\" gehören?", correct=["Objekt-Nominalphrase", "Verbalphrase"],wrong=["Adverbialphrase", "Attributphrase", "Subjekt-Nominalphrase"],sonst=False, inst=multiple )]
    ]

blatt2_1c = [
	    [SingleChoice("Bzgl. welcher (nicht an der Oberflächensyntax ersichtlichen) Eigenschaft unterscheiden sich die PPs in den beiden Analysen?", "syntaktische Funktion", "Wortart des Phrasenkopfes", "Phrasentyp", sonst=True, inst=single)],
    [SelectionList("Was ist der Fall, wenn die PP ein Adverbial ist?", "die im Verb ausgedrückte Tätigkeit wird modifiziert","die PP wird dem Substantiv beigefügt", "der Ort des Geschehens wird festgelegt", sonst=True, inst=selection)],
    [SelectionList("Was ist der Fall, wenn die PP ein Attribut ist?", "die PP wird dem Substantiv beigefügt", "der Ort des Geschehens wird festgelegt", "die im Verb ausgedrückte Tätigkeit wird modifiziert", sonst=True, inst=selection)]
    ]




blatt2_2a = [
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 1 zugrunde?","Regelsystem","Regelbuch", "formale Grammatik","Theorie der Sprachstruktur", "Wissen um Sprachstruktur", sonst=False, inst=single)],
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 2 zugrunde?","Regelbuch", "Regelsystem", "formale Grammatik","Theorie der Sprachstruktur", "Wissen um Sprachstruktur", sonst=False, inst=single)],
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 3 zugrunde?","Theorie der Sprachstruktur", "Regelbuch", "Regelsystem", "formale Grammatik", "Wissen um Sprachstruktur", sonst=False, inst=single)]
    ]

blatt2_2b = [
    [MultipleChoice("Welche Gesetzmäßigkeiten umfasst die Grammatik als Regelsystem?", correct=["phonologische", "morphologische", "syntaktische"],wrong=["semantische", "pragmatische"],sonst=False, inst=multiple)],
    [Lueckentext("Die Syntax ist ein Teilbereich der Grammatik, der sich auf die syntaktischen Regularitäten bezieht.", {"Teilbereich":["Oberbegriff","Synonym"], "syntaktischen":["morphologischen","phonologischen","semantischen"]},inst=luecke)]
    ]




blatt2_3a = [
     [MultipleChoice("Was sind die 3 grundlegenden Beschreibungsebenen der Grammatik natürlicher Sprachen?", correct=["Lautebene, Wortebene, Satzebene"],wrong=["Morphemebene, Phrasenebene, Satzebene", "Satzebene, Textebene, Bedeutungsebene"],sonst=False, inst=single)]
     ]

blatt2_3b = [
    [Lueckentext("Für die Blätter gilt: natürlichsprachliche Wörter sind eine Teilmenge aus dem Alphabet der Grundsymbole der formalen Sprache; ein analysierter natürlichsprachlicher Satz ist ein in der formalen Grammatik ableitbares Wort der formalen Sprache.", {"Wort":["Morphem","Symbol"], "Grundsymbole":["Nicht-Terminale"]},inst=luecke)]
    ]    




blatt2_4a = [
    [MultipleChoice("Welche Typen von Syntaxbäumen (auch: Parsebäume, Ableitungsbäume) wurden gezeigt?", correct=["Konstituentenbaum mit Phrasenlabels als Knoten","Dependenzgraph mit gelabelten Kanten"],wrong=["Konstituentenbaum mit gelabelten Kanten", "Dependenzgraph mit Phrasenlabels als Knoten"],sonst=False, inst=multiple)]
    ]

blatt2_4b = [
    [SingleChoice("In welcher Form wird die syntaktische Struktur eines Satzes beim Aufruf von NLTK print(tree) erstellt?","Klammernotation","Baumdiagramm", sonst=True, inst=single)],
    [SingleChoice("In welcher Form wird die syntaktische Struktur eines Satzes beim Aufruf von NLTK tree.draw() erstellt?","Baumdiagramm", "Klammernotation", sonst=True, inst=single)]
    ]

blatt2_4c_tree = """
(I-shot-an_elephant-in_my_pajamas
  I
  (shot-an_elephant-in_my_pajamas
    shot
    (an_elephant-in_my_pajamas
      an_elephant
      in_my_pajamas
    )
  )
)
"""

blatt2_4d_tree = """

(I-shot-an_elephant-in_my_pajamas
  I
  (shot-an_elephant-in_my_pajamas
    (shot-an_elephant
      shot
      an_elephant
    )
    (in_my_pajamas)
  )
)
"""




blatt2_5 = [
    [SingleChoice("Was ist der Ursprung der Ambiguität?","strukturelle Ambiguität", "lexikalische Ambiguität", "morphologisch ambige Formen", sonst=True, inst=single)],
    [MultipleChoice("In welcher Beziehung können Gerund und nachfolgendes Nomen stehen?", correct=["Nomen ist Kopf einer NP-Phrase", "Gerund ist Kopf eines nichtfiniten Teilsatzes", "Nomen ist Dependent in einem nichtfiniten Teilsatz"],wrong=["Nomen ist Dependent einer NP-Phrase"],sonst=False, inst=multiple)],
    [SingleChoice("Welche Funktion im Satz nimmt das Nomen ein, wenn es Kopf der Gerund-Nomen-Phrase ist?", "Subjekt", "Objekt", sonst=False, inst=single)],
    [SingleChoice("Welche Funktion innerhalb der Gerund-Nomen-Phrase nimmt das Nomen ein, wenn das Gerund Kopf dieser Phrase ist?", "Objekt", "Subjekt", sonst=False, inst=single)],
    [SingleChoice("Welche Funktion im Hauptsatz nimmt das Gerund ein, wenn es Kopf der Gerund-Nomen-Phrase ist?", "Subjekt", "Objekt", sonst=False, inst=single)],
    [SingleChoice("Welche Funktion nimmt das Gerund ein, wenn das Nomen Kopf der Gerund-Nomen-Phrase ist?", "Attribut", "Objekt", sonst=False, inst=single)],
    ]



    
blatt2_6a = [
    [MultipleChoice("Hinsichtlich welcher syntaktischen Grundprinzipien werden natürliche Sprachen mit formalen Methoden analysiert?", correct=["Konstituenz", "Dependenz"],wrong=["Synonymie", "Korrektheit"],sonst=False, inst=multiple)],
    [SingleChoice("Konstituenz ist synonym zu:","Phrasenstruktur","Dependenz", "Abhängigkeitsstruktur", "Wortstruktur", sonst=True, inst=single)],
    [SingleChoice("Dependenz ist synonym zu:","Abhängigkeitsstruktur", "Phrasenstruktur", "Konstituenz",  "Wortstruktur", sonst=True, inst=single)],
    ]

blatt2_6b = [
    [SingleChoice("Welche Mittel kommen in einer formalen Syntaxanalyse zum Einsatz?", "formale Grammatik + Parser", "Parsebäume", "formale Grammatik", "Parser", sonst=False, inst=single)],
    ]

blatt2_6c = [
    [MultipleChoice("Die ________ eines Satzes bzgl. der formalen Grammatik wird erkannt.", correct=["Wohlgeformtheit", "Grammatikalität"],wrong=["Sinnhaftigkeit"],sonst=False, inst=multiple)],
#     [SingleChoice("Bei einer solchen Analyse wird welche ja/nein-Entscheidung unweigerlich getroffen?","Wohlgeformtheit", "Sinnhaftigkeit", "Korrektheit", sonst=True, inst=single)],
    ]

blatt2_6d = [
    [MultipleChoice("Welche Vorteile hat die Modellierung der Satzstruktur mit Hilfe einer formalen Grammatik?", correct=["Eine unendliche Menge an Sätzen kann mit endlichen Mitteln beschrieben werden.", "Eine automatische Strukturanalyse wird möglich."], wrong=["Eine endliche Menge an Sätzen kann mit unendlichen Mitteln beschrieben werden."], inst=multiple)]
    ]

