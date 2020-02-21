#!/usr/bin/python
# As far as base cases go, again, think about some cases where we'd want the
#    recursion to stop executing. What should happen when the amount of cents
#    given is 0? What should happen when the amount of cents given is negative?
#    What about when we've used up all of the available coin denominations?
#  * As far as performance optimizations go, caching/memoization might be one
#    avenue we could go down. 
#  * Building up values in our cache in an iterative fashion might also be a good
#    way to go about improving our implementation. 
import sys

def making_change(amount, denominations, cache=0):
    ways = [0 for i in range(amount +1)]

    ways[0] = 1

    for value in denominations:
        for higher_amount in range(1, amount + 1):
          if value <= higher_amount:
             ways[higher_amount] += ways[higher_amount - value]
    return ways[amount]



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")