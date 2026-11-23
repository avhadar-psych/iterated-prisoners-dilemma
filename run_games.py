import random
from game import play_game, prisoners_dilemma
from strategies import (tit_for_tat, random_choice, always_cooperate, always_defect)

random.seed(42)  # makes the random strategy reproducible

# Game 1: always_defect vs tit_for_tat
print(play_game(always_defect, tit_for_tat, 10, prisoners_dilemma))
# Result: (14, 9)

# Game 2: always_cooperate vs random_choice
print(play_game(always_cooperate, random_choice, 10, prisoners_dilemma))
# Result: (24, 34)

# Game 3: tit_for_tat vs random_choice
print(play_game(tit_for_tat, random_choice, 10, prisoners_dilemma))
# Result: (24, 29)