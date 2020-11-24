from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice, OpenTextfield
from questions import single, multiple, offen, selection, luecke

blatt4_6a = [
    [MultipleChoice("Wie ist im NLTK vorzugehen, wenn ein (wohlgeformter) Satz von einer Grammatik nicht erkannt wird?",correct=["<code>trace</code>-Output aktivieren und überprüfen"], wrong=["anderen Parser verwenden", "Grammatik neu einlesen"], inst=single)]
    ]

blatt4_6b = [
    [OpenTextfield("Wie können im NLTK die Regeln einer Grammatik ausgegeben werden?", initial="for p in grammar1.________(): _______(p)", correct="for p in grammar1.productions(): print(p)", inst="Vervollständigen Sie die Listcomprehension, indem sie an den Stellen der Unterstriche die richtigen Funktionen einsetzen.")]
]

blatt4_6c = [
    [MultipleChoice("Welche Beispiele zeigen direkte Rekursion?",correct=["NP -> NP"], wrong=["NP -> DET N PP", "PP -> P NP"], inst=multiple)]
]

blatt4_6d = [
    [MultipleChoice("Welche Beispiele für Phrasenstrukturregeln sind linksrekursiv?", correct=["NOM -> NOM PP"], wrong=["NOM -> ADJ NOM", "PP -> P NP"], inst=multiple)],
    [MultipleChoice("Welche Beispiele sind rechtsrekursiv?", correct=["NOM -> ADJ NOM"], wrong=["NOM -> NOM PP", "PP -> P NP"], inst=multiple)]
]