# Tests for play_game

from game import play_game, prisoners_dilemma
from strategies import always_cooperate, always_defect


def test_two_cooperators_get_3_points_each_round():
    assert play_game(always_cooperate, always_cooperate, 10, prisoners_dilemma) == (30, 30)

def test_two_defectors_get_1_point_each_round():
    assert play_game(always_defect, always_defect, 10, prisoners_dilemma) == (10, 10)

def test_cooperator_and_defector_get_0_and_5_points():
    assert play_game(always_cooperate, always_defect, 10, prisoners_dilemma) == (0, 50)
    
def test_zero_rounds():
    assert play_game(always_cooperate, always_cooperate, 0, prisoners_dilemma) == (0, 0)
