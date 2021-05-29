from Selection.person import Person


def merge_rankings(rankings: list):
    people_map = dict()

    for ranking in rankings:

        for i in range(0, len(ranking)):
            if ranking[i] not in people_map:
                people_map[ranking[i]] = Person(ranking[i], rank=i)
            else:
                people_map[ranking[i]].add_rank(i)

    ranked = list(people_map.values())

    ranked.sort(key=lambda x: x.average_rank, reverse=False)

    return ranked


def print_rankings_pool_style(ranked: list):
    tracker = 0
    for i in range(0, int(ranked[len(ranked) - 1].get_rank()) + 1):
        ranks_for_i = [j for j in ranked if int(j.get_rank()) == i]
        if len(ranks_for_i) != 0:
            print("Rank :", tracker, " ", *ranks_for_i)
            tracker += 1


def test_case_a():
    ranking_a = [4428, 9811, 6055, 1761, 6194, 6327, 1000, 4807, 8554, 6892, 6324, 4864, 2047, 5882, 1753, 3157,
                 1874, 4958, 3043, 6606, 7262, 2152, 8165, 2583, 7617, 7504, 2535, 8179, 1442, 1863, 9216, 1757,
                 5413, 2047, 3674, 8180, 7308, 6885, 1619, 4752, 6233, 2721, 7301, 8673, 3524, 4990, 5832, 8241,
                 1476, 1718, 2990, 9845, 4529, 7606, 7320, 9861, 6800, 4372, 8670]
    ranking_b = [1485, 8670, 2698, 9216, 1476, 2093, 2047, 7431, 7262, 4921, 7320, 5275, 7586, 5413, 1863, 6194,
                 3157, 7626, 1753, 8144, 5882, 3043, 2990, 3927, 1757, 8179, 7617, 2871]
    ranking_c = [1863, 9845, 1718, 8554, 7301, 3043, 4958, 6606, 6885, 6055, 4807, 5275, 7586, 6324, 2871, 8673,
                 2698, 8165, 2721, 3954, 3674, 3927, 6892, 4921, 1619, 1753, 1442, 7320, 7617, 4990, 5413, 7431,
                 9216, 7262, 8241]

    global_ranking = merge_rankings([ranking_a, ranking_b, ranking_c])

    return global_ranking


if __name__ == "__main__":
    print_rankings_pool_style(test_case_a())
