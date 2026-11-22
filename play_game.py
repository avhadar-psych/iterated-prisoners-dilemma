prisoners_dilemma = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (1, 1),
}

def play_game(strategy1, strategy2, rounds, game):
    """Play `rounds` rounds and return the total score of each player."""
    history1 = []  # player 1's moves so far
    history2 = []  # player 2's moves so far
    score1 = 0
    score2 = 0
    for round_number in range(rounds):
        # 1. ask each strategy for its next move
        # 2. look up both payoffs in game
        # 3. add the payoffs to the scores
    .append(...)    # 4. add the moves to the histories
    return score1, score2