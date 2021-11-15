# see: https://leetcode.com/problems/partition-labels/
from typing import List


# Readily comprehensible version - 460 ms
# def partitionLabels(s: str) -> List[int]:
#     ans = []
#     n = len(s)
#     sec = [0, 0]
#     for i in range(n):
#         c = s[i]
#         for j in range(sec[1] + 1, n):
#             if s[j] == c:
#                 # expand
#                 sec[1] = j
#         if i == sec[1]:
#             ans.append(sec[1] - sec[0] + 1)
#             sec = [i + 1, i + 1]
#     return ans


# Faster version - 32 ms, faster than 96.99% submissions
def partitionLabels(s: str) -> List[int]:
    n = len(s)
    memo = {}  # record start position and end position of each char appears in the string
    for i in range(n):
        c = s[i]
        if c not in memo:
            memo[c] = [i, i]
        else:
            # update end position
            memo[c][1] = i

    ans = []
    start, end = 0, 0
    for i in range(n):
        c = s[i]
        end = max(end, memo[c][1])
        if i == end:
            ans.append(end - start + 1)
            start, end = i + 1, i + 1
    return ans


# TEST
s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))  # [9,7,8]
