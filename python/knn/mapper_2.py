'''
Second-phase mapper
Takes reducer.py output
Flips class,list[dist] to dist,class
'''
import sys
import json


def main():
  for line in sys.stdin:
    line = line.strip()

    if len(line) > 0:
      cls, dists = line.split('\t')
      for dist in json.loads(dists):
        print(f'{dist}\t{cls}')


if __name__ == '__main__':
  main()
