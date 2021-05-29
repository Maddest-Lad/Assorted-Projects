# Static Vars
MALE = "MALE"
FEMALE = "FEMALE"
NONBINARY = "NONBINARY"
UNKNOWN = "UNKNOWN"


class ParseEngine:

    def __init__(self, rank_mode=False, gender=False):
        pass

    @staticmethod
    def parse_gender(s: str):
        if s in ["female", "she", "her"]:
            return FEMALE

        if s in ["male", "he", "him"]:
            return MALE

        if s in ["nonbinary", "they", "them"]:
            return NONBINARY

        return UNKNOWN
