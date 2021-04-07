'''
Takes mapped point distances class,dist
Output class,list[dist] for top-5 distances
'''
import sys
import json


def main():
  current_class = None
  current_top_dist = []
  cls = None

  for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    cls, dist = line.split('\t')

    # convert count (currently a string) to int
    try:
      dist = float(dist)
    except ValueError:
      # count was not a number, so silently
      # ignore/discard this line
      continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_class is None or current_class == cls:
      current_top_dist.append(dist)
      current_top_dist = sorted(current_top_dist)[:5]
      current_class = cls
    else:
      if current_class:
        # write result to STDOUT
        print(f'{current_class}\t{json.dumps(current_top_dist)}')
      current_top_dist = []
      current_class = cls

  # do not forget to output the last word if needed!
  if current_class == cls:
    print(f'{current_class}\t{json.dumps(current_top_dist)}')


if __name__ == '__main__':
  main()
