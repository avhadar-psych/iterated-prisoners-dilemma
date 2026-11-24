# The game itself: payoff tables and the function that plays a game between two strategies.

# Prisoner's dilemma payoffs: (player 1 move, player 2 move) -> (player 1 payoff, player 2 payoff)
prisoners_dilemma = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (1, 1),
}
# "C" = cooperate, "D" = defect


def play_game(strategy1, strategy2, rounds, game):
    """Play `rounds` rounds and return the total score of each player."""
    history1 = []  # player 1's moves so far
    history2 = []  # player 2's moves so far
    score1 = 0
    score2 = 0
    for round_number in range(rounds):
        # 1. ask each strategy for its next move
        move1 = strategy1(history1, history2)
        move2 = strategy2(history2, history1)
        # 2. look up both payoffs in game
        payoff1, payoff2 = game[(move1, move2)]
        # 3. add the payoffs to the scores
        score1 += payoff1
        score2 += payoff2
        # 4. add the moves to the histories
        history1.append(move1)
        history2.append(move2)
    return score1, score2


#   Run at least two games (in a reproducible way) and record the results in comments.  
