# 06. Expressions:
import itertools


def expressions(*args):
    numbers = list(*args)
    possible_entries = numbers

    integrated = set()
    for subset in itertools.combinations(possible_entries * 2, len(list(*args))):
        integrated .add(subset)

    print(integrated)
expressions(input().split(", "))
