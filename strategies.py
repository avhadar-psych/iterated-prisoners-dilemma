# At least two strategies: functions that take the history of moves and return the next move. For
# example, a simple strategy might be to always cooperate, while another might be to choose
# randomly. A more complex strategy might be to cooperate on the first move, and then copy the
# opponent’s last move for subsequent rounds (tit-for-tat). An even more complex strategy might be
# to cooperate on the first move, and then to play the move that would have given the opponent the
# highest score in the previous round (the “best response” strategy).

def always_cooperate(my_history, opponent_history):
    return "C" 

def always_defect(my_history, opponent_history):
    return "D" 

def tit_for_tat(my_history, opponent_history):
    if len(my_history) == 0:  # is this the first round?
        return "C"
    else:
        return opponent_history[-1]   # the opponent's last move
    
