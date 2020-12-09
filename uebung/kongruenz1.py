from nltk import FeatStruct
from sklearn.metrics import accuracy_score
from itertools import product
test_cases = product(
    ["der", "die", "das"], ["Löffel", "Gabel", "Messer"]
)
truth = [
    True, False, False,
    False, True, False,
    False, False, True
]

pred = []
for nomPhr in test_cases:
    # Baseline: Alles ist grammatisch!
    pred.append(True)

print("Acc: {}".format(accuracy_score(truth, pred)))
