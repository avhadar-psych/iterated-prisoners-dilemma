import random
from game import play_game, prisoners_dilemma
from strategies import (tit_for_tat, random_choice, always_cooperate, always_defect)

random.seed(123)  # makes the random strategy reproducible

# Game 1: always_defect vs tit_for_tat
print(play_game(always_defect, tit_for_tat, 500000, prisoners_dilemma))
# Result: (500004, 499999)

# Game 2: always_cooperate vs random_choice
print(play_game(always_cooperate, random_choice, 500000, prisoners_dilemma))
# Result: (749871, 2000086)

# Game 3: tit_for_tat vs random_choice
print(play_game(tit_for_tat, random_choice, 500000, prisoners_dilemma))
# Result: (1124669, 1124674)

# Game 4: always_cooperate vs always_defect
print(play_game(always_cooperate, always_defect, 500000, prisoners_dilemma))
# Result: (0, 2500000)

# Game 5: always_cooperate vs tit_for_tat
print(play_game(always_cooperate, tit_for_tat, 500000, prisoners_dilemma))
# Result: (1500000, 1500000)













