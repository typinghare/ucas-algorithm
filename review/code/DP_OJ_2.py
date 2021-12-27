# 1. name
def solve(nums):
    pass


# 2. Leetcode 老哥
def solve2(nums):
    res = nums[0]
    for i in range(1, len(nums)):
        res += max(nums[i] - nums[i - 1], 0)
    return res


nums = [5, 6, 7, 8]
print(solve2(nums))
