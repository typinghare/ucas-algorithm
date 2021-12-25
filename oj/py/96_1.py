# author: ShotgunRO

# <Maximum Alternating Subsequence Sum>
# leetcode 1911 - https://leetcode.com/problems/maximum-alternating-subsequence-sum/

def maxAlternatingSum(nums):
    """
    :param nums: List[int]
    :return: int
    """
    odd, even = 0, 0
    for num in nums:
        # suppose now we have selected k numbers, which in a row: [n1, n2, ..., nk],
        # this list serves as a subsequence we temporarily make.
        # now we are considering whether choose the nums[k+1]:

        # - If k is an even number, then if we choose nums[k+1], we have to make sure that
        # the result is greater than the old <odd>, otherwise nums[k+1] will be passed,
        # the result can be counted by (even - num), which means we need to pick up
        # the greater one between (odd) and (even - num);
        # - If k is an odd number, then if we choose nums[k+1], we have to make sure that
        # the result is greater than old <even>, otherwise nums[k+1] will be passed,
        # the result can be counted by (odd + num), which means we need to pick up
        # the greater one between (even) and (odd + num).
        odd, even = max(odd, even - num), max(even, odd + num)
    return even


test_nums = [5, 1, 8, 4, 3, 20, 3, 9, 7, 2]
print(maxAlternatingSum(test_nums))

# ---------------------------------------------------------------------------------------------------
# nums = map(int, input().split(' '))
# print(type(nums))
#
#
# def maxAlternatingSum(nums):
#     odd, even = 0, 0
#     for num in nums:
#         odd, even = max(odd, even - num), max(even, odd + num)
#     return even
#
#
# print(maxAlternatingSum(nums))
