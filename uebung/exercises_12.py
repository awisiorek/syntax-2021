from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice
from questions import single, multiple, offen, selection, luecke

blatt12_4 = [
    [
        MultipleChoice(
            "Welche der folgenden Bedingungen wird an eine PCFG gestellt?",
            ["Die Summe aller Regelwahrscheinlichkeiten für jede LHS ist jeweils 1."],
            ["Die Summe aller Regelwahrscheinlichkeiten für jede RHS ist jeweils 1.",
             "Die Summe aller Regelwahrscheinlichkeiten innerhalb einer Grammatik ist 1."],
            inst=single
        )
    ],
    [
        MultipleChoice(
            "Was ist die Aufgabe des Viterbi-Algorithmus?",
            ["Bestimmung des wahrscheinlichsten Syntaxbaums"],
            ["Finden aller Konstituenten",
             "Bestimmung der Köpfe und Dependenzrelationen"],
            inst=single
        )
    ],
    [
        MultipleChoice(
            "Warum muss zwischen zwei Schichten eines Feedforward-Netzwerks eine nicht-lineare Aktivierungsfunktion eingefügt werden?",
            ["Weil die zwei Schichten sonst nicht mehr lernen können als nur eine Schicht."],
            ["Weil Vektoren normalisiert werden müssen, um bestimmte Funktionen zu lernen.",
             "Weil nicht-lineare Funktionen die Effizienz des Netzwerks verbessern.",
             "Weil eine valide Wahrscheinlichkeitsverteilung nur mit Normalisierung gelernt werden kann."],
            inst=single
        )
    ]
]

blatt12_5a = [
    [MultipleChoice("Welche zwei Faktoren führen bei der syntaktischen Analyse natürlicher Sprache mittels formaler Grammatiken zu mehr Ambiguität (Anzahl an Ableitungen)?", correct=[
                    "Zunahme der Anzahl von Regeln", "längere Sätze"], wrong=["kürzere Sätze", "Abnahme der Anzahl von Regeln"], inst="Wählen Sie die zwei korrekten Antworten aus.")]
]

blatt12_5b = [
    [MultipleChoice("Welche zwei Arten von Ambiguität unterscheidet man hier?", correct=["strukturelle Ambiguität", "lexikalische Ambiguität"], wrong=[
                    "Attachment-Ambiguität", "Koordinierungsambigutiät"], inst="Wählen Sie die zwei korrekten Antworten aus.")]
]
