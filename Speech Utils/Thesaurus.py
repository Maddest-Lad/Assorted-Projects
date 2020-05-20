import itertools

import PySynonym

##########
# BROKEN #
##########


def get_synonyms(word) -> str:
    return PySynonym.synonym(word)


# Returns A Random Permutation of A Given Text
def thesuarize_text(text) -> []:
    # Creates A List Of Lists Of Synonyms For Each Word, Then Randomly Picks One
    return [PySynonym.synonym(word) for word in text.split()]


# Returns Every Possible Permutation of A Given Text
def all_permutations(text) -> [[]]:
    return itertools.product(*thesuarize_text(text))
