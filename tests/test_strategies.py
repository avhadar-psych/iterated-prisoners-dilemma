# A set of tests that demonstrate that your functions work as expected.

from strategies import always_cooperate, always_defect, tit_for_tat


def test_always_cooperate_cooperates_even_after_betrayal():
    assert always_cooperate(["C", "C"], ["D", "D"]) == "C"

def test_always_defect_defects_even_after_cooperation():
    assert always_defect(["C", "C"], ["C", "C"]) == "D"
    

def test_tit_for_tat_cooperates_on_first_move():
    assert tit_for_tat([], []) == "C"

def test_tit_for_tat_defects_after_opponent_defects():
    assert tit_for_tat(["C", "D"], ["D", "D"]) == "D"

def test_tit_for_tat_cooperates_after_opponent_cooperates():
    assert tit_for_tat(["C", "C"], ["D", "C"]) == "C"