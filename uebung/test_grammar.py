from nltk import load_parser
from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument("grammar")
p.add_argument("sentence", nargs='+')
args = p.parse_args()

parser = load_parser(args.grammar)

trees = parser.parse(args.sentence)
i = -1
for i, tree in enumerate(trees):
    tree.draw()
if i < 0:
    print("Satz nicht akzeptiert!")
