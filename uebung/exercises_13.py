from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice
from questions import single, multiple, offen, selection, luecke

blatt13_6a = [
    [SingleChoice("Um was für ein Sprachkonstrukt handelt es sich?", "center embedding", "garden-path sentence", "cross-serial dependencies", sonst=True)],
    [SingleChoice("Welchem Typ muss eine Grammatik mindestens genügen, um solche Sätze modellieren zu können?", "kontextfrei", "kontextsensitiv", "regulär", "rekursiv aufzählbar")],
    [SelectionList("Welche Rekursionstiefe hat der Satz?", "3", "2", "1", "4")]
]

blatt13_6b = [
    [SingleChoice("Um was für ein Sprachkonstrukt handelt es sich?", "garden-path sentence", "center embedding", "cross-serial dependencies", sonst=True)],
    [SingleChoice("Ist der Satz ambig?", "Nein", "Ja")],
    [SingleChoice("Sind Teile des Satzes ambig?", "Ja", "Nein")]
]

blatt13_7 = [
    [MultipleChoice(
        "Welche der Formeln berechnen Precision, Recall, Accuracy und F1-Score korrekt?",
        ["F1 = (2 * Precision * Recall) / (Precision + Rrecall)",
         "Accuracy = (true positives + true negatives) / Anzahl aller Vorhersagen",
         "Recall = true positives / (true positives + false negatives)",
         "Precision = von allen Instanzen, für die 1 vorhergesagt wurde, wie viele wurden richtig vorhergesagt?"],
        wrong=["F1 = (Precision * Recall + 1) / (Precision + Recall)",
               "Accuracy = true positives / Anzahl aller Vorhersagen",
               "Precision = true positives / true negatives",
               "Recall = von allen Instanzen, für die 1 vorhergesagt wurde, wie viele wurden richtig vorhergesagt?"])]
]

# interaktiv: nltk 7.2-4 chunking, developing and evaluating chunkers, cascaded chunkers

# chunk vs phrase
blatt13_8 = [
    [MultipleChoice("Wo ist der Unterschied zwischen Chunks und Phrasen?", correct=["Chunks sind oft kürzer als Phrasen."], wrong=["Chunks sind oft länger als Phrasen.", "Es gibt keinen Unterschied."], inst=single)],
    [SingleChoice("Wozu sind Tag Pattern ähnlich?", "regular expressions", "part-of-speech tags", "XML-Tags", sonst=True)],
    [MultipleChoice("Was kann mit Chinking erreicht werden?", ["ein vorher erkannter Chunk wird nicht mehr erkannt", "ein Chunk wird in zwei Chunks aufgeteilt", "ein Chunk wird verkürzt"], wrong=["zwei Chunks werden zu einem größeren zusammengefasst"])],
    [SingleChoice("Welche Klammern zeigen Chinking an?", "} {", "{ }")],
    [SingleChoice("Welche Klammern zeigen Chunking an?", "{ }", "} {")],

]
# arten von chunkpasern
# regexpparser
# unigramchunker
# bigramchunker
# consecutivenpchunker

# chunk vs phrase 2
blatt13_9 = [
    [MultipleChoice("Wodurch kann mit einem RegexpParser eine hierarchische Chunk-Struktur aufgebaut werden (ähnlicher den hierarchischen Analysen mit einer Phrasenstrukturgrammatik)?", ["Output einer Chunk-Regel (Chunk-Tag) als Input einer folgenden Regel (Hintereinanderschalten)", "Loopen über bereits erkannte Chunk-Muster"], wrong=["Verwendung von Chinking-Regeln", "Verwendung von Splitting-Regeln"])],

]
