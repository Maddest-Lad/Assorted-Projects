import math


# Returns The Probability of Player_1 Winning Against Player_2
def expected(player_1, player_2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (player_1.elo_rating - player_2.elo_rating) / 400))


def update_elo_rating(player_1, player_2, winner=0, k=30):
    p1_expected = expected(player_1, player_2)
    p2_expected = expected(player_2, player_1)

    # Player 1 Wins
    if winner == 1:
        player_1.elo_rating = player_1.elo_rating + k * (1 - p1_expected)
        player_2.elo_rating = player_2.elo_rating + k * (0 - p2_expected)

    # Player 2 Wins
    if winner == -1:
        player_2.elo_rating = player_2.elo_rating + k * (1 - p2_expected)
        player_1.elo_rating = player_1.elo_rating + k * (0 - p1_expected)

    if winner == 0:
        # Draw Does Nothing
        pass

    player_1.add_competitor(player_2)
    player_2.add_competitor(player_1)


# Maps From Range [in_from : in_to] -> [out_from : out_to]
def translate(value, in_from, in_to, out_from, out_to):
    return out_from + ((value - in_from) / (in_to - in_from)) * (out_to - out_from)


def print_winner(winner: int):
    if winner == 1:
        print("Applicant A", "Wins")
    if winner == -1:
        print("Applicant B", "Wins")
    if winner == 0:
        print("It was a Tie")
