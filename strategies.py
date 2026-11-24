# Strategies for the iterated prisoner's dilemma.
# Each strategy takes (my_history, opponent_history) and returns its next move: "C" or "D".

import random

def random_choice(my_history, opponent_history):
    return random.choice(["C", "D"])

def always_cooperate(my_history, opponent_history):
    return "C" 

def always_defect(my_history, opponent_history):
    return "D" 

def tit_for_tat(my_history, opponent_history):
    # Strategies for the iterated prisoner's dilemma.
    # Each strategy takes (my_history, opponent_history) and returns its next move: "C" or "D".
    if len(my_history) == 0:  # is this the first round?
        return "C"
    else:
        return opponent_history[-1]   # the opponent's last move
    
