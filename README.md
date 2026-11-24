# Iterated Prisoner's Dilemma

This project simulates the prisoner's dilemma game. It pits different decision-making strategies against each other, runs simulations over a chosen number of rounds, and lets you examine which strategy pays off more in the long run.

## What's in the repo

- `game.py`: the payoff table and the `play_game` function, which simulates a game and returns each player's total score.
- `strategies.py`: the different strategies.
- `run_games.py`: the script that runs the simulations and records the results in comments. Run this script to play the games.
- `tests/`: two test files, `test_game.py` for the game and `test_strategies.py` for the strategies.
- `pyproject.toml` and `uv.lock`: project settings and the exact package versions.

## Strategies

- `tit_for_tat`: cooperates in the first round, then copies the opponent's last move.
- `random_choice`: chooses randomly each round.
- `always_cooperate`: always cooperates.
- `always_defect`: always defects.

Each strategy is a function that takes its own move history and the opponent's (`"C"` for cooperate, `"D"` for defect) and returns its next move.
