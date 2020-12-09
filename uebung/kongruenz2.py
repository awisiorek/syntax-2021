from itertools import product
from nltk import FeatStruct
from sklearn.metrics import accuracy_score
lexicon = {
    "Messer": [
        FeatStruct(GEN="neu", NUM="sg", KAS="nom"),
        FeatStruct(GEN="neu", NUM="sg", KAS="akk"),
        FeatStruct(GEN="neu", NUM="sg", KAS="dat"),
        FeatStruct(GEN="neu", NUM="pl", KAS="nom"),
        FeatStruct(GEN="neu", NUM="pl", KAS="akk"),
        FeatStruct(GEN="neu", NUM="pl", KAS="gen")
    ],
    "Gabel": [FeatStruct(NUM="sg", GEN="fem")],
    "Löffel": [
        FeatStruct(GEN="mas", NUM="sg", KAS="nom"),
        FeatStruct(GEN="mas", NUM="sg", KAS="akk"),
        FeatStruct(GEN="mas", NUM="sg", KAS="dat"),
        FeatStruct(GEN="mas", NUM="pl", KAS="nom"),
        FeatStruct(GEN="mas", NUM="pl", KAS="akk"),
        FeatStruct(GEN="mas", NUM="pl", KAS="gen"),
    ],

    "der": [
        FeatStruct(NUM="sg", GEN="mas", KAS="nom"),
        FeatStruct(NUM="sg", GEN="fem", KAS="dat"),
        FeatStruct(NUM="sg", GEN="fem", KAS="gen"),
        FeatStruct(NUM="pl", KAS="gen")
    ],
    "des": [
        FeatStruct(NUM="sg", GEN="mas", KAS="gen"),
        FeatStruct(NUM="sg", GEN="neu", KAS="gen")
    ],
    "dem": [
        FeatStruct(NUM="sg", GEN="mas", KAS="dat"),
        FeatStruct(NUM="sg", GEN="neu", KAS="dat"),
    ],
    "den": [
        FeatStruct(NUM="sg", GEN="mas", KAS="akk"),
        FeatStruct(NUM="pl", KAS="dat"),
    ],
    "die": [
        FeatStruct(NUM="sg", GEN="fem", KAS="nom"),
        FeatStruct(NUM="sg", GEN="fem", KAS="akk"),
        FeatStruct(NUM="pl", KAS="nom"),
        FeatStruct(NUM="pl", KAS="akk")
    ],
    "das": [
        FeatStruct(NUM="sg", GEN="neu", KAS="nom"),
        FeatStruct(NUM="sg", GEN="neu", KAS="akk"),
    ]
}


def predict(artikel, nomen):
    return True
    # == your code goes here == #


test_cases = product(
    ["der", "des", "dem", "den", "die", "das"], ["Messer", "Löffel", "Gabel"]
)
truth = [
    True, True, True,
    False, False, False,
    True, False, True,
    False, False, True,
    True, True, True,
    True, False, False
]

predictions = []
for artikel, nomen in test_cases:
    predictions.append(predict(artikel, nomen))

print(
    "Accuracy: {:.0f}%".format(
        accuracy_score(truth, predictions)*100
    )
)
