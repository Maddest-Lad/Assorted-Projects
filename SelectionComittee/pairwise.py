import random
from math import floor

from Selection.elo_utils import update_elo_rating, translate, expected, print_winner
from Selection.ranking_merge import test_case_a

if __name__ == '__main__':

    applicants = test_case_a()

    for applicant in applicants:
        applicant.elo_rating = translate(applicant.average_rank, 0, len(applicants), 1000, 1600)

    for i in range(0, 100):
        applicant_1 = applicants[random.randint(0, len(applicants) - 1)]
        applicant_2 = applicants[random.randint(0, len(applicants) - 1)]

        # No Duplicate Matches
        if applicant_1 not in applicant_2.compared_to:
            winner = random.randint(-1, 1)

            print("{} {}% vs {} {}%".format(applicant_1, floor(100 * expected(applicant_1, applicant_2)), applicant_2,
                                            floor(100 * expected(applicant_2, applicant_1))))

            update_elo_rating(applicant_1, applicant_2, winner, k=30)

            print_winner(winner)

            print()

    applicants.sort(key=lambda x: x.elo_rating, reverse=True)

    for i in range(0, len(applicants) - 1):
        print("Rank", i, ":", applicants[i].id, floor(applicants[i].elo_rating))
