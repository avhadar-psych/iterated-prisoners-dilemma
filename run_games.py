import random
from game import play_game, prisoners_dilemma
from strategies import (tit_for_tat, random_choice, always_cooperate, always_defect)

random.seed(42)  # makes the random strategy reproducible

# Game 1: random_choice vs tit_for_tat
print(play_game(random_choice, tit_for_tat, 10, prisoners_dilemma))
# Result: (28, 28)

# Game 2: always_cooperate vs always_defect
print(play_game(always_cooperate, always_defect, 10, prisoners_dilemma))
# Result: (0, 50)

# Game 3: tit_for_tat vs random_choice
print(play_game(tit_for_tat, random_choice, 10, prisoners_dilemma))
# Result: (24, 29)