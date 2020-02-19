#!/usr/bin/python

import sys

options = [["rock"], ["paper"], ["scissors"]]

def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    if n == 1:
        return options
    output = []

    listA = rock_paper_scissors(n - 1)
    for subList in listA:
        for play in options:
            newPlay = subList + play
            output.append(newPlay)
    return output

  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')