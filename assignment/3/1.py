# [Monkeys and Bananas]
# There are N Monkeys and N bananas are placed in a straight line.
# Each monkey want to have a banana, if two monkeys want to own the same banana, there
# will be a fight! A monkey can stay at his position, move one step right from x to x + 1, or
# move one step left from x to x 1. Any of these moves consumes 1 second. Assign monkeys to
# banana so that no monkey fight each other and the time when the last monkey gets a banana
# is minimized.

# see: https://blog.csdn.net/SL_World/article/details/103319892
from typing import List


def AssignBananaToMonkeys(n: int, monkeys: List[int], bananas: List[int]):
    """
    :param n: the number of monkeys(the same as the number of bananas)
    :param monkeys: the position of monkeys
    :param bananas: the position of bananas
    :return: minimum time (seconds)
    """
    # 1. each step: calculate the nearest banana of each monkey, and remove the nearest one
    # *** Time Complexity is not qualified ***
    # time = 0
    # for i in range(n):
    #     min_distance_of_all = abs(monkeys[n - i - 1] - bananas[0])
    #     monkey = monkeys[0]
    #     banana = bananas[0]
    #     for j in range(n - i):
    #         # the j-th from left monkey
    #         pos = monkeys[j]
    #         min_distance = abs(bananas[0] - pos)
    #         banana_pos = bananas[0]
    #         for k in range(1, j):
    #             # can be optimized
    #             curr_distance = abs(bananas[k] - pos)
    #             if curr_distance < min_distance:
    #                 min_distance = curr_distance
    #                 banana_pos = bananas[k]
    #         if min_distance < min_distance_of_all:
    #             min_distance_of_all = min_distance
    #             monkey = pos
    #             banana = banana_pos
    #     # remove <monkey> and <banana>
    #     time = max(time, abs(monkey - banana))
    #     monkeys.remove(monkey)
    #     bananas.remove(banana)
    # return time

    # 2. assign each monkey the corresponding banana (corresponding selection)
    # [Proof] We can use reduction to absurdity to prove this algorithm:
    # Suppose we arrange i-th monkey choose (i+1)-th banana, then for the (i+1)-th monkey,
    # it has to choose the (i+2)-th banana or i-th banana.
    # If it choose the (i+2)-th banana, then the (i+2)-th monkey has to choose the (i+3)-th or the i-th banana,
    # here we find it impossible for the (i+2)-th monkey to choose the i-th banana, because it spends
    # more time. Hence, the (i+1)-th monkey has to choose the i-th banana, then a cross turns up.
    # At any situation, time that a "cross selection" costs greater than or equals to "corresponding selection",
    # which is easy to prove.
    # In conclusion, the original supposition is dismissed.
    # ----------------------------------------------------------------------
    # We have to ensure the two lists are in order
    # in case one of the two lists is disordered, sort them at first
    monkeys = sorted(monkeys)
    bananas = sorted(bananas)
    time = 0
    for i in range(n):
        time = max(time, abs(monkeys[i] - bananas[i]))
    return time


# TEST
monkeys = [1, 2, 5, 12]
bananas = [3, 9, 13, 14]
n = len(monkeys)
print(AssignBananaToMonkeys(n, monkeys, bananas))
