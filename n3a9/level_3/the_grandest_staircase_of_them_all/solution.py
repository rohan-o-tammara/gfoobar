from __future__ import print_function
import math

# Combinations
# i.e, Number of ways of choosing r items from n items without order
def nCr(n, r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))

# Integer Partition function P
# Partitioning Integer is same as distributing
# n identical objects into r identical bins
#
# Implemention of theorem at
# https://brilliant.org/wiki/identical-objects-into-identical-bins/
cache = {}
def P(n, r):
    key = '{} {}'.format(n, r)
    try:
        return cache[key]
    except KeyError:
        result = None
        if r > n:
            result = 0
        else:
            if r == 2:
                if (n % 2) == 0:
                    result = n/2
                else:
                    result = (n-1)/2
            elif r == 1:
                result = 1
            elif r == n:
                result = 1
            elif r == n-1:
                result = 1
            else:
                result = sum(list(map(lambda x: P(n-r, x), range(1, r+1))))
        cache[key] = result
        return result

# Integer Partition function Q
# Number of distinct partitions of n into r
#
# Implemention of equation at
# https://mathworld.wolfram.com/PartitionFunctionQ.html
def Q(n, r):
    return P(n - nCr(r, 2), r)

def answer(n):
    # Check if 3 <= n <= 200
    if n < 3 or n > 200:
        raise Exception("Value of n (bricks) is out of bounds. 3 <= n <= 200")
    # Max levels possible for a given n is the solution to x(x+1)/2 = n
    # i.e., sum of integers till max_levels is largest number <= n
    max_levels = int(math.floor((math.sqrt(1 + 8*n)-1)/2))
    # Sum of number distributions with all valid level sizes (atleast 2 steps until 'max_levels' steps)
    result = sum(list(map(lambda x: Q(n, x), range(2, max_levels+1))))

    return int(result)

if __name__ == "__main__":
    print(answer(3))
    print(answer(4))
    print(answer(5))
    print(answer(6))
    print(answer(200))
