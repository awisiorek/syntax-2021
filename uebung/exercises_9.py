from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice
from questions import single, multiple, offen, selection, luecke

blatt9_2a = [
    [MultipleChoice("Welche Operationen hat der Recursive Descent Parser?", correct=["Scan", "Predict"], wrong=["Shift", "Reduce", "Complete"])],
    [MultipleChoice("Welche Operationen hat der Shift Reduce Parser?", correct=["Shift", "Reduce"], wrong=["Scan", "Predict", "Complete"])],
    [MultipleChoice("Welche Operationen hat der Earley Parser?", correct=["Scan", "Predict", "Complete"], wrong=["Shift", "Reduce"])]
]    

# der det mann"
blatt9_2b_z = [
    [SingleChoice("Um welchen Parser handelt es sich?", "Shift Reduce", "Earley", "Recusive Descent")],
    [SingleChoice("Welche Operation folgt als nächstes?", "Reduce", "Shift", "Scan", "Predict", "Complete")]
]

#Q0: (S' -> *S, 0)
blatt9_2b_1 = [
    [SingleChoice("Um welchen Parser handelt es sich?", "Earley", "Shift Reduce", "Recusive Descent")],
    [SingleChoice("Welche Operation folgt als nächstes?", "Predict", "Reduce", "Shift", "Scan", "Complete")]
]

blatt9_2b_2 = [
    [SingleChoice("Um welchen Parser handelt es sich?", "Recusive Descent", "Earley", "Shift Reduce")],
    [SingleChoice("Welche Operation folgt als nächstes?", "Predict", "Reduce", "Shift", "Scan", "Complete")]
]

blatt9_2b_3 = [
    [SingleChoice("Um welchen Parser handelt es sich?", "Earley", "Shift Reduce", "Recusive Descent")],
    [SingleChoice("Welche Operation folgt als nächstes?", "Scan", "Predict", "Reduce", "Shift", "Complete")]
]

blatt9_2b_4 = [
    [SingleChoice("Um welchen Parser handelt es sich?", "Earley", "Shift Reduce", "Recusive Descent")],
    [SingleChoice("Welche Operation folgt als nächstes?", "Complete", "Scan", "Predict", "Reduce", "Shift")]
]

blatt9_2b_5 = [
    [SingleChoice("Welche Operation folgt als nächstes?", "Scan", "Complete", "Predict", "Reduce", "Shift", "Keine der Alternativen")]
]

blatt9_2b_6 = [
    [SingleChoice("Welche Operation folgt als nächstes?", "Complete", "Scan", "Predict", "Reduce", "Shift", "Keine der Alternativen")]
]

blatt9_2b_7 = [
    [SingleChoice("Welche Operation folgt als nächstes?", "Predict", "Complete", "Scan",  "Reduce", "Shift", "Keine der Alternativen")]
]

blatt9_2b_8 = [
    [SingleChoice("Welche Operation folgt als nächstes?",  "Predict", "Scan", "Complete", "Reduce", "Shift", "Keine der Alternativen")]
]

blatt9_2b_9 = [
    [SingleChoice("Welche Operation folgt als nächstes?", "Keine der Alternativen", "Complete", "Scan", "Predict", "Reduce", "Shift")]
]

blatt9_2b_10 = [
    [SingleChoice("Welche Operation folgt als nächstes?", "Scan", "Complete",  "Predict", "Reduce", "Shift", "Keine der Alternativen")]
]

blatt9_2b_11 = [
    [SingleChoice("Welche Operation folgt als nächstes?", "Shift", "Complete", "Scan", "Predict", "Reduce", "Keine der Alternativen")]
]

blatt9_2b_12 = [
    [SingleChoice("Welche Operation folgt als nächstes?", "Keine der Alternativen", "Complete", "Scan", "Predict", "Reduce", "Shift")]
]

blatt9_2b_13 = [
    [SingleChoice("Welche Operation folgt als nächstes?", "Reduce", "Complete", "Scan", "Predict", "Shift", "Keine der Alternativen")]
]
