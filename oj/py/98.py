# see: https://leetcode.com/problems/partition-labels/
from typing import List


# [Analysis]
# 遍历 s 中的字符（记该字符对应的下标为 i），找到这个字符在 s 中最后出现的位置（记该位置的下标为 j）
# sec[] 表示当前分隔（partition）的区间，每次遍历一个字符，如果 i > sec[1]，
# 则需要扩展该区间，即 sec[1] = i
# 直至 i == sec[0]，说明该区间中所有的字符都不会出现在 i 以后的位置，将 sec[] 保存到 ans[] 中
# 更新 sec[]（继续遍历 i 之后的字符串）

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
def partitionLabels(s):
    n = len(s)
    # 先遍历一次字符串，记录每个字符串最后出现的位置
    memo = {}  # record end position of each char appears in the string
    for i in range(n):
        c = s[i]
        memo[c] = i

    ans = []
    start, end = 0, 0  # 这里不使用列表，而使用两个整形，效率更高
    for i in range(n):
        c = s[i]
        end = max(end, memo[c])
        if i == end:
            ans.append(end - start + 1)
            start, end = i + 1, i + 1
    return ans


# TEST
# s = "ababcbacadefegdehijhklij"
# print(partitionLabels(s))  # [9,7,8]

# OJ
print(' '.join(map(str, partitionLabels(input()))))
