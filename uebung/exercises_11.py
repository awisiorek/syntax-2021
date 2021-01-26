from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice, OpenTextfield
from questions import single, multiple, offen, selection, luecke

blatt11_5_1 = [
    [OpenQuestion(
        "Berechnen Sie die Wahrscheinlichkeit für die Ableitung in der letzten Zeile.",
        "0.000864", ".000864", "0.0864 %", "0.0864%", ".0864 %", ".0864%",
        inst=offen
    )]
]

blatt11_5_2 = [
    [MultipleChoice(
        "Warum werden die Analysen in den Discard-Zeilen verworfen?",
        ["Ihre Wahrscheinlichkeiten sind zu gering."],
        ["Die Analysen sind mit der gegebenen Grammatik nicht möglich.",
         "Sie analysieren die Eingabesequenz nicht komplett.",
         "Das Verwerfen verhindert eine Endlosrekursion."],
        inst=single
    )]
]

blatt11_5_3 = [
    [SingleChoice(
        "Um welchen Parser kann es sich nicht handeln?",
        "ViterbiParser",
        "InsideChartParser",
        "InsideChartParser mit beam-size",
        "LongestChartParser"
    )],
    [SingleChoice(
        "Nach welchem Kriterium wird beim Parsen mit dem InsideChartParser (= <i>Lowest-Cost-First</i>-Strategie) die <i>edge queue</i> sortiert?",
        "nach der Wahrscheinlichkeit",
        "nach der Länge der Ableitung",
        "nach der beam-size"
    )],
    [SingleChoice(
        "Um welche Art der Ambiguität handelt es sich bei den beiden gefundenen Ableitungen?",
        "Koordinationsambiguität",
        "PP-Attachment-Ambiguität",
        "Temporale Ambiguität"
    )],
]
