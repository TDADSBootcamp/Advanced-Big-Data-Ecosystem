Supports a manual walkthrough of a map/reduce operation.

## The Problem

As a game player
I want to see my position on a score leaderboard
So that I can compete with other players

## The Game

The game is still in development, but is expected to be a smash hit with millions of players.
An outcome for a player is a win, loss, or draw represented by the characters (`w`, `d`, `l`).

Scores as as follows:
- 10 points for a win
- 2 points for a draw
- 0 points for a loss

Outcomes are recorded as they happen and stored in the geographically nearest available storage system to the player.
Other details are left out for brevity.

If alice has a win and a draw, bob has a win and charlie has a loss, the leaderboard result should consist of:
| total_score | player  |
|-------------|---------|
| 12          | alice   |
| 10          | bob     |
| 0           | charlie |

## The Simulation

A Python script is provided to simulate outcomes so that a leaderboard computation can be developed.

### Usage
```
usage: generate_outcomes.py [-h] -p PLAYER -n NUM_GAMES [-s NUM_SPLITS]

Generate random game outcomes for a set of players.

optional arguments:
  -h, --help            show this help message and exit
  -p PLAYER, --player PLAYER
                        player id
  -n NUM_GAMES, --num_games NUM_GAMES
                        number of games to produce outcomes for
  -s NUM_SPLITS, --num_splits NUM_SPLITS
                        number of splits for mappers
```

### Example
```python
pipenv run python python/awesome_game/generate_outcomes.py -p alice -p bob -p charlie -n 3 -s 5
[('alice', 'l'), ('charlie', 'd')]
[('bob', 'w'), ('bob', 'l')]
[('bob', 'd'), ('alice', 'w')]
[('charlie', 'd'), ('charlie', 'd')]
[('alice', 'l')]
```

## Steps

1. **Input** Run the script for an appropriately-size set of players and games, with `num_splits` set to produce one split per team member.
2. **Framework (Split)**
    1. Assign one split per team member
3. **Mapper**
    1. Each team member performs an appropriate mapping operation on their split, sharing the result in a Google Sheet.
4. **Framework (Shuffle)**
    1. Sort the sheet
    2. Split the results into one split per key
5. **Reducer**
    1. Have volunteers execute an appropriate reduce operation
6. **Framework (Split)**
    1. Assign splits as appropriate, possibly only one
7. **Mapper**
    1. Volunteer(s) perform another map operation
8. **Framework (Shuffle)**
    1. Sort the sheet
9. **Reducer**
    1. Any more work to do?
10. **Framework (Done)** 
    1. Job complete, leaderboard available.

