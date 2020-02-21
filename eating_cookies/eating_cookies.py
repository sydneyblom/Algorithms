#!/usr/bin/python
#
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
#chace parameter is here for you if you want to implement
#a sultion more effieciet than the naive recurisive soltioon
def eating_cookies(n, cache=None):
  #create a base case
  if cache:
    print('There is a catch')
  if n < 0:
    return 0
  if n == 0:
    return 1
  elif cache and  n in cache:
    return cache[n]
  else:
    if cache is None:
      cache = {}
    value = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    eating_cookies(n-3, cache)
    cache[n] = value
    return value




if __name__ == "__main__":
  if len(sys.argv) > 1: #this is just running the file as a program and it lets you do cl arguements
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')