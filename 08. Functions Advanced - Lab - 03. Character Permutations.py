# 03. Character Permutations:
import itertools


def combo(args):
    permutations = list(itertools.permutations(str(args), 2))
    [(print("".join(i))) for i in permutations]


combo(input())
