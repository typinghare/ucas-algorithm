# [Maximum Number of Coins You Can Get]
# There are 3n piles of coins of different size, you and your friends will take piles of coins as
# follows: In each step, you will choose any 3 piles of coins (not necessarily consecutive). Your
# friend Alice will pick the pile with the maximum number of coins. You will pick the pile with
# sub-maximal number of coins. Your friend Bob will pick the last pile. Repeat until there are no
# more piles of coins. Given an array of integers piles where piles[i] is the number of coins in the
# i-th pile. Return the maximum number of coins which you can have.

# see: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from typing import List


def solve(piles: List[int]):
    count = len(piles)  # the number of piles
    list.sort(piles)  # sort piles list in ascending order
    pos = count  # the index of pile which "I" choose
    result = 0  # sum of coins "I" have

    # In each step, we choose two most piles and one least pile
    # The choice of the first few times are as follow:
    # 1: piles[0]   piles[n-2]  piles[n-1]
    # 2: piles[1]   piles[n-4]  piles[n-2]
    # 3: piles[2]   piles[n-6]  piles[n-5]
    # ...
    # The middle pile is what "I" choose, and the indices are regular, namely:
    # n-2, n-4, n-6, ...
    # We use <pos> to record the index of pile "I" choose in each step. At the beginning, it could be
    # n, then in each loop it minus 2
    for i in range(count // 3):
        pos -= 2
        result += piles[pos]
    return result


# TEST
piles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solve(piles))
