'''
Second-phase reducer
Takes sorted dist,class nearest-first
Calculates frequencies in top 5
Prints the most common class
'''
import sys
import collections


def main():

  result = []

  for line in sys.stdin:
    line = line.strip()

    dist, cls = line.split('\t')

    result.append((dist, cls))

  top_n = collections.Counter([v for k, v in sorted(result)[:5]]).most_common(1)
  print(top_n)


if __name__ == '__main__':
  main()
