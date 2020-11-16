from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice, OpenTextfield
from questions import single, multiple, offen, selection, luecke

blatt3_2a = [
    [MultipleChoice("Welche Eigenschaften hat <i>gerne</i> in Satz 1?", correct=["Es fungiert als Satzglied mit der syntaktischen Funktion Adverbial.", "Es bezeichnet die näheren Umstände des im Verb ausgedrückten Geschehens."], wrong=["Es ist flektierbar."], inst=multiple)],
    [SingleChoice("Welche Wortart folgt damit für das Wort <i>gerne</i> in Satz 1?", "Adverb", "Adjektiv", "Partikel", sonst=True, inst= single)]
    ]

blatt3_2b = [
    [MultipleChoice("Welche Eigenschaften hat <i>gut</i> in Satz 2?", correct=["Es ist flektierbar.","Es fungiert als Satzglied mit der syntaktischen Funktion Adverbial.", "Es bezeichnet die näheren Umstände des im Verb ausgedrückten Geschehens."], wrong=[], inst=multiple)],
    [SingleChoice("Welche Wortart folgt damit für das Wort <i>gut</i> in Satz 2?", "Adjektiv", "Adverb", "Partikel", sonst=True, inst= single)],
    [SingleChoice("Welche Wortart könnte man für das Wort <i>gut</i> in Satz 2 vermuten, wenn man Adverbien nicht morphologisch, sondern semantisch charakterisiert (als Wortart, die der Modifizierung des Verbalgeschehens dient)?", "Adverb", "Adjektiv", "Partikel", sonst=True, inst= single)]    
]

blatt3_5 = [
    [Lueckentext("Das Partizip <i>Verloren<i> ist eine Konstituente , aber keine Phrase . Es gehört zu einer komplexen VP . Aus dieser wurde es extrahiert und ins Vorfeld gestellt. Die gesamte VP umfasst die Konstituenten <i>seinen Schlüsselbund zwar noch nie verloren haben.</i>", {"Konstituente":["Phrase"], "Phrase":["Konstituente"], "VP":["NP", "PP"], "Vorfeld":["Mittelfeld", "Nachfeld"], "Konstituenten":["Phrasen"]},inst=luecke)]
]

blatt3_7 = [
    [MultipleChoice("Welcher ist der richtig permutierte Satz?", correct=["Nur mit einem Schritt beginnt auch eine Reise von tausend Meilen."], wrong=["Nur beginnt eine Reise von tausend Meilen auch mit einem Schritt", "Mit einem Schritt beginnt eine Reise von tausend Meilen auch nur.", "Nur mit beginnt eine Reise von tausend Meilen auch einem Schritt."], inst=single)],
    [MultipleChoice("<i>Eine Reise beginnt auch nur mit einem Schritt.</i><br>Welche Tests wurden angewandt?", correct=["Eliminierungstest"], wrong=["Substitutionstest", "Permutationstest", "Koordinationstest"], inst=multiple)]


]

blatt3_8a = [
    [SingleChoice("Was ist der Input eines Part-of-Speech-Taggers?", "Wortfolge", "Folge von Wortklassen", sonst=True, inst=single)],
    [SingleChoice("Was ist der Output eines Part-of-Speech-Taggers?", "Folge von Wortklassen", "Wortfolge", sonst=True, inst=single)],
    [OpenTextfield(text="Wie wirt der POS-Tagger im NLTK aufgerufen?", initial="nltk.____()", correct="nltk.pos_tag()", inst="Geben Sie die entsprechende Funktion anstelle des Unterstrichs ein.", klammer=False)]
]

blatt3_8b = [
    [MultipleChoice("Was leistet die Funktion <code>nltk.similar()</code>?", correct=["Zu einem Wort wird ein Index seiner Kontexte aufgebaut.", "Zu einem Wort werden alle Wörter gefunden, die in gleichen Kontexten vorkommen."], wrong=["Zu einem Wort werden alle Synonyme gefunden.", "Zu einem Wort werden seine Kookkurrenzpartner gefunden."], inst=multiple)]
]

blatt3_8c = [
    [Lueckentext("In der ersten Zeile des Codes werden Bigramm -Tupel von Wort+POS-Tag -Tupeln aus einem englischen Korpus erstellt. Zeile 2 und 3 dienen der Erzeugung einer Frequenzliste von POS-Tags derjenigen Bigramme, deren zweites Element das POS-Tag 'NOUN' trägt. Das Ergebnis sind die häufigsten zweistelligen syntaktischen Muster des Englischen mit NOUN als rechtem Kontext, nämlich NOUN+NOUN, DET+NOUN und ADJ+NOUN; diese Ergebnisse geben Hinweis auf die NP- Phrasenstruktur im Englischen.",
    {"Bigramm":["Trigramm", "Unigramm"],"Wort+POS-Tag":["POS", "POS+Wort+POS"], "'NOUN'":["'DET'", "'ADJ'"],"Phrasenstruktur":["Köpfe", "Länge"]}, inst=luecke)]

]

blatt3_8d = [
    [MultipleChoice("Was sind morphologische Kriterien für Wortkategorien?", correct=["Flexionstyp", "gleiche Endungen"], wrong=["gleicher Kontext", "gleiche syntagmatische Position"], inst=multiple)],
    [MultipleChoice("Was sind syntaktische Kriterien für Wortkategorien?", wrong=["Flexionstyp", "gleiche Endungen"], correct=["gleicher Kontext", "gleiche syntagmatische Position"], inst=multiple)],
    [SingleChoice("Was bedeutet das Tag <i>VB</i> im Browntagset (siehe 5.7)?", "base", "3rd singular present", "past participle", "gerund", "simple past", sonst=False, inst=single)],
    [SingleChoice("Was bedeutet das Tag <i>VBZ</i> im Browntagset (siehe 5.7)?", "3rd singular present", "base", "past participle", "gerund", "simple past", sonst=False, inst=single)],
    [SingleChoice("Was bedeutet das Tag <i>VBN</i> im Browntagset (siehe 5.7)?", "past participle", "3rd singular present", "base", "gerund", "simple past", sonst=False, inst=single)],
    [SingleChoice("Was bedeutet das Tag <i>VBG</i> im Browntagset (siehe 5.7)?", "gerund", "past participle", "3rd singular present", "base", "simple past", sonst=False, inst=single)],
    [SingleChoice("Was bedeutet das Tag <i>VBD</i> im Browntagset (siehe 5.7)?", "simple past", "gerund", "past participle", "3rd singular present", "base", sonst=False, inst=single)]
]

blatt3_9a = [
    [Lueckentext("Ersetzbarkeit einer längeren durch eine kürzere Sequenz unter Erhalt der Wohlgeformtheit .", {"längeren":["kürzeren"], "kürzere":["längere"], "Wohlgeformtheit":["Bedeutung"]}, inst=luecke)]

]



blatt3_9c = [
    [Lueckentext("Die Koordination von Phrasen ist dadurch eingeschränkt, dass nur gleichartige Phrasen verkettet werden können. Das Ergebnis ist eine Phrase des gleichen Typs, also der gleichen syntaktischen Kategorie.", {"gleichartige":["unterschiedliche"], "syntaktischen":["morphologischen"]}, inst=luecke)]
]