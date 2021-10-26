# https://leetcode.com/problems/largest-divisible-subset/discuss/84002/4-lines-in-Python
def largestDivisibleSubset(nums):
    S = {-1: set()}
    for x in sorted(nums):
        S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
    return list(max(S.values(), key=len))


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(largestDivisibleSubset(nums))
