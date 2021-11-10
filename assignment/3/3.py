# [Cross the River]
# Some people want to cross a river by boat. Each person has a weight, and each boat can
# carry an equal maximum weight limit. Each boat carries at most 2 people at the same time,
# provided the sum of the weight of those people is at most boat’s weight limit. Return the
# minimum number of boats to carry every given person.
# Note that it is guaranteed each person can be carried by a boat.

# see: https://leetcode.com/problems/boats-to-save-people/
from typing import List


# [Wrong idea]
# def crossTheRiver(people: List[int], limit: int) -> int:
#     list.sort(people)
#     half = (limit >> 1) + 1
#
#     i = len(people)
#     ans = 0
#     while i >= 0:
#         i -= 1
#         if people[i] >= half:
#             ans += 1
#         elif people[i] <= half - 1:
#             break
#         elif people[i] + people[i - 1] <= limit:
#             ans += 1
#             i -= 1
#
#     ans += (i >> 1)
#     return ans

def crossTheRiver(people: List[int], limit: int) -> int:
    people = sorted(people)
    people_number = len(people)
    ans = 0  # number of rescue boats
    i, j = 0, people_number - 1

    while i <= j:
        if people[i] + people[j] <= limit:
            # 最重 + 最轻 < L
            i += 1
            ans += 1
            j -= 1
        else:
            ans += 1
            j -= 1
    return ans


# TEST
people = [1, 2, 3, 3, 4, 4, 5, 5, 6]
# people = [3, 2, 2, 1]
limit = 6
print(crossTheRiver(people, limit))
