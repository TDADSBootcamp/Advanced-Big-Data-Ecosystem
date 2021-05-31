Supports a manual walkthrough of a map/reduce operation.

## The Problem

```
As a game player
I want to see my position on a score leaderboard
So that I can compete with other players
```

## The Game

The game is still in development, but is expected to be a smash hit with millions of players.
An outcome for a player is a win, loss, or draw represented by the characters (`w`, `d`, `l`).

Scores as as follows:
- 10 points for a win
- 2 points for a draw
- 0 points for a loss

Outcomes are recorded as they happen and stored in the geographically nearest available storage system to the player.
Other details are left out for brevity.

If:
- alice has played two games for a win and a draw
- bob has played one game and won
- charlie has player one game and lost

Then the leaderboard result should be:

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
`pipenv run python python/awesome_game/generate_outcomes.py -p player1 -p player2 -p player3 -n 5 -s 4`


Output:
```python
[('player1', 'l'), ('player3', 'w'), ('player2', 'w'), ('player2', 'w')]
[('player3', 'w'), ('player3', 'w'), ('player2', 'd'), ('player3', 'd')]
[('player1', 'd'), ('player1', 'l'), ('player1', 'w'), ('player2', 'l')]
[('player3', 'w'), ('player2', 'w'), ('player1', 'w')]
```

## Steps

First, discuss how to solve the problem as a group.

- At least as many players as students
- Use [Google Worksheet](https://docs.google.com/spreadsheets/d/1j_HX9LwwB89io3GjaQupiSHoCr-h5ySkHJIbpFZochk/edit#gid=0)

1. **Input** Run the script for an appropriately-size set of players and games, with `num_splits` set to produce one split per team member.
2. **Framework (Split)**
    1. Assign one split per team member
    2. Paste splits into Google Sheet
3. **Mapper**
    1. Each team member performs an appropriate mapping operation on their split
    2. They share the result in the sheet, one pair per line, same format as input
    3. (copy your split into a text file, edit the values, drop each value onto a new line, paste back into the sheet in the reduce column)
4. **Framework (Shuffle)**
    1. Sort the range in the map column (pick appropriate direction)
    2. Split the results into one split per key
5. **Reducer**
    1. Have volunteers execute an appropriate reduce operation, same process as mapper
6. **Framework (Split)**
    1. Assign splits as appropriate
7. **Mapper**
    1. Volunteer(s) perform another map operation
8. **Framework (Shuffle)**
    1. Sort the range in the map column (pick appropriate direction)
9. **Reducer**
    1. Any more work to do?
10. **Framework (Done)** 
    1. Job complete, leaderboard available.

