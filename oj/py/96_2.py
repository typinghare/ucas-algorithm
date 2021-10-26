# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/1298585/JavaC%2B%2BPython-Easy-and-Concise
def maxAlternatingSum(nums):
    """
    :param nums: List[int]
    :return: int
    """
    res = nums[0]
    for i in range(1, len(nums)):
        res += max(nums[i] - nums[i - 1], 0)
    return res


nums = [5, 6, 7, 8]
print(maxAlternatingSum(nums))
