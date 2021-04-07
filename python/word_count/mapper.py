'''
Simple word count mapper
based on https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
'''
import sys
import re

for line in sys.stdin:
  line = line.strip()
  words = line.split()

  for word in words:
    print(f'{re.sub(r"[^a-zA-Z0-9]", "", word)}\t1')
