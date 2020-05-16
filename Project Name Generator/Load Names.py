from random import randint
from Tools.scripts.treesync import raw_input


def names():
    adj = tuple(open('adjectives.txt', 'r'))
    nouns = tuple(open('nouns.txt', 'r'))
    adjPick = adj[randint(0, 626)].capitalize().splitlines()[0]
    nounPick = nouns[randint(0, 2453)].capitalize().splitlines()[0]
    return adjPick + " " + nounPick


def sci_names():
    adj = tuple(open('adjectivesSci.txt', 'r'))
    nouns = tuple(open('nounsSci.txt', 'r'))
    adjPick = adj[randint(0, 53)].capitalize().splitlines()[0]
    nounPick = nouns[randint(0, 57)].capitalize().splitlines()[0]
    return adjPick + " " + nounPick


def big_names():
    adj = tuple(open('adjectivesLong.txt', 'r'))
    nouns = tuple(open('nounsLong.txt', 'r'))
    adjPick = adj[randint(0, 28479)].capitalize().splitlines()[0]
    nounPick = nouns[randint(0, 90963)].capitalize().splitlines()[0]
    return adjPick + " " + nounPick


def prints():  # Prints 10 Names From Each Name Pool Set
    print("\n" + "Logical Names:")
    for i in range(10):
        print(names())

    print("\n" + "Crazy Names:")
    for i in range(10):
        print(big_names())

    print("\n"+"Sci-Fi Names:")
    for i in range(10):
        print(sci_names())

    print("\n")


prints()
raw_input("Press Enter to Close")
