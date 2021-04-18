"""
Generates a set of random game outcomes for a set a players.
"""

import argparse
import itertools
import math
import random


def parse_args():
  parser = argparse.ArgumentParser(
      description='Generate random game outcomes for a set of players.')
  parser.add_argument('-p',
                      '--player',
                      action='append',
                      help='player id',
                      required=True)
  parser.add_argument('-n',
                      '--num_games',
                      help='number of games to produce outcomes for',
                      type=int,
                      required=True)
  parser.add_argument('-s',
                      '--num_splits',
                      help='number of splits for mappers',
                      type=int,
                      default=None)

  return parser.parse_args()


def partition_all(the_list, num_partitions):
  """
  returns list contents split over the number of requested partitions.
  Returns fewer partitions than requests if len(the_list) < num_partitions.

  >>> partition_all([], 2)
  []

  >>> partition_all([1], 2)
  [[1]]

  >>> partition_all([1, 2], 2)
  [[1], [2]]

  >>> partition_all([1, 2, 3], 2)
  [[1, 2], [3]]
  """
  if len(the_list) == 0:
    return []
  partition_size = math.ceil(len(the_list) / num_partitions)
  return [
      the_list[i:i + partition_size]
      for i in range(0, len(the_list), partition_size)
  ]


def generate_outcome_splits(players, num_games, num_splits):
  """
  Generates splits of randomly shuffled, randomly generated game outcomes for the players.

  >>> len(generate_outcome_splits(['bob'], 1, 1))
  1

  >>> generate_outcome_splits(['bob'], 1, 1)[0][0][0]
  'bob'

  >>> len(generate_outcome_splits(['bob'], 5, 2))
  2

  >>> len(generate_outcome_splits(['bob'], 5, 5))
  5
  """

  outcomes = ['w', 'l', 'd']

  player_outcomes = [
      zip(itertools.repeat(player), random.choices(outcomes, k=num_games))
      for player in players
  ]
  randomised_outcomes = list(itertools.chain.from_iterable(player_outcomes))
  random.shuffle(randomised_outcomes)

  return partition_all(randomised_outcomes, num_splits)


def main(args):
  players = args.player
  num_games = args.num_games
  num_splits = args.num_splits or len(players)

  for split in generate_outcome_splits(players, num_games, num_splits):
    print(split)


if __name__ == '__main__':
  main(parse_args())
