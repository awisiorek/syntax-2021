from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice, OpenTextfield
from questions import single, multiple, offen, selection, luecke

blatt7_5 = [
    [MultipleChoice("Welche DET-Kategorien gibt es für den Satz?", correct=["[NUM=’pl’, PER=3]", "[GND=’masc’, NUM=’sg’, PER=3]"], wrong=["[NUM=’sg’, PER=3]", "[GND=’fem’, NUM=’sg’, PER=3]"])],
    [SingleChoice("Wieso wird der Satz von der Grammatik abgelehnt?", "nicht unifizierbar", "\'Katze\' ist kein gültiges Wort", sonst=True)],
    [MultipleChoice("Wo liegt das Problem, sodass der Satz abgeleht wird?", correct=["< N NUM > ≠ < DET NUM >", "< N GEN > ≠ < DET GEN >"], wrong=["< N PER > ≠ < DET PER >"])]
]