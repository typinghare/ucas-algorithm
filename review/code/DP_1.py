# 1. 迭代，数组存储历史值（5 min）
def solve(nums):
    size = len(nums)
    dp = [0] * (size + 2)
    for i in range(size):
        dp[i + 2] = max(dp[i] + nums[i], dp[i + 1])
    return dp[size + 1]


# 2. 迭代，数组存储历史值，优化（3 min）
def solve2(nums):
    size = len(nums)
    dp = [nums[0], max(nums[0], nums[1])] + [0] * (size - 2)
    for i in range(size):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[size - 1]


# 3. 递归（3 min）
def solve3(nums):
    size = len(nums)
    if size == 0:
        return 0
    if size == 1:
        return nums[0]

    return max(nums[0] + solve3(nums[2:]), solve3(nums[1:]))


# 2. 房屋围成圈，递归（3 min）
def solve4(nums):
    # 1. 选 nums[0], 则 nums[n-1] 不能被选
    # 2. 不选 nums[0]，则 nums[n-1] 可以被选
    return max(nums[0] + solve3(nums[1:-1]), solve3(nums[1:]))


# test 1
nums = [4, 2, 3, 6]
print(solve(nums))
print(solve2(nums))
print(solve3(nums))

# test 2
print(solve4(nums))
