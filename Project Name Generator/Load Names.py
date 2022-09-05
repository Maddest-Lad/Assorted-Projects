from random import randint


def names():
    adj = tuple(open('adjectives.txt', 'r'))
    nouns = tuple(open('nouns.txt', 'r'))
    adjPick = adj[randint(0, 626)].capitalize().splitlines()[0]
    nounPick = nouns[randint(0, 2453)].capitalize().splitlines()[0]
    return adjPick + " " + nounPick


def sci_names():
    try:
        adj = tuple(open('adjectivesSci.txt', 'r'))
        nouns = tuple(open('nounsSci.txt', 'r'))
        adjPick = adj[randint(0, 53)].capitalize().splitlines()[0]
        nounPick = nouns[randint(0, 57)].capitalize().splitlines()[0]
        return adjPick + " " + nounPick
    except:
        return ""


def big_names():
    adj = tuple(open('adjectivesLong.txt', 'r'))
    nouns = tuple(open('nounsLong.txt', 'r'))
    adjPick = adj[randint(0, 28479)].capitalize().splitlines()[0]
    nounPick = nouns[randint(0, 90963)].capitalize().splitlines()[0]
    return adjPick + " " + nounPick


def food():
    try:
        adj2 = tuple(open('adjectivesLong.txt', 'r'))
        adj = tuple(open('adjectivesTaste.txt', 'r'))
        nouns = tuple(open('FoodNouns.txt', 'r'))
        adjPick = adj[randint(0, 20)].capitalize().splitlines()[0]
        adjPick2 = adj2[randint(0, 28479)].capitalize().splitlines()[0]
        nounPick = nouns[randint(0, 228)].capitalize().splitlines()[0]
        return adjPick + " " + adjPick2 + " " + nounPick
    except:
        pass

        return ""


for i in range(50):
    print(sci_names())
