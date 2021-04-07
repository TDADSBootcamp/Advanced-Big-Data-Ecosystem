'''
Maps 4-dimensional float points to a distance from a reference point
Takes reference point w,x,y,z as a string argument
Reads lines from dataset w,x,t,z,class
Produces class,distance
'''
import sys


def distance(a, b):
  """Return manhatten distance between a and b

    >>> distance((1,2,3,4), (1,2,3,4))
    0.0

    >>> distance((1,2,3,4), (1,2,3,5))
    1.0

    >>> distance((5.1,3.5,1.4,0.2), (5.1,3.5,1.4,0.2))
    0.0
    """
  w1, x1, y1, z1 = [float(c) for c in a]
  w2, x2, y2, z2 = [float(c) for c in b]
  return abs(w1 - w2) + abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def main():
  point_to_classify = sys.argv[1]

  # input comes from STDIN (standard input)
  for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    if len(line) > 0:
      w1, x1, y1, z1, cls = line.split(',')

      print(
          f'{cls}\t{distance((w1, x1, y1, z1), point_to_classify.split(","))}')


if __name__ == '__main__':
  main()
