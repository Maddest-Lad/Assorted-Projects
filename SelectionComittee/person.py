from Selection import utils


class Person:
    id: str
    _rank: list
    gender: str
    compared_to: list
    average_rank: float
    elo_rating: float

    def __init__(self, id: str, rank=None, gender=None):
        self._rank = []
        self.compared_to = []

        self.id = id

        if gender:
            self.gender = utils.ParseEngine.parse_gender(gender)
        else:
            self.gender = utils.UNKNOWN

        if rank:
            self.add_rank(rank)
        else:
            self.add_rank(0)

        self.elo_rating = 1000

    def add_rank(self, value: float):
        self._rank.append(value)
        self.average_rank = sum(self._rank) / len(self._rank)

    def add_competitor(self, player):
        self.compared_to.append(player)

    def __repr__(self):
        return str([self.id])
