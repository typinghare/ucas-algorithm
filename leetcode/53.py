# see https://leetcode-cn.com/problems/maximum-subarray/
from typing import List


def maxSubArray(nums: List[int]) -> int:
    return getMaxSubArray(nums, 0, len(nums) - 1)


def getMaxSubArray(nums: List[int], l: int, r: int) -> int:
    # conquer
    if l == r:
        return nums[l]

    # divide
    mid = (l + r) // 2
    left = getMaxSubArray(nums, 0, mid)
    right = getMaxSubArray(nums, mid + 1, r)

    # combine
    lcur, rcur = nums[mid], nums[mid + 1]
    lmax, rmax = lcur, rcur
    for i in range(mid - 1, l - 1, -1):
        lcur += nums[i]
        if lcur > lmax:
            lmax = lcur
    for i in range(mid + 2, r + 1):
        rcur += nums[i]
        if rcur > rmax:
            rmax = rcur
    return max(left, right, lmax + rmax)


# Test
arr = [-84, -87, -78, -16, -94, -36, -87, -93, -50, -22, -63, -28, -91, -60, -64, -27, -41, -27, -73, -37, -12, -69,
       -68, -30, -83, -31, -63, -24, -68, -36, -30, -3, -23, -59, -70, -68, -94, -57, -12, -43, -30, -74, -22, -20, -85,
       -38, -99, -25, -16, -71, -14, -27, -92, -81, -57, -74, -63, -71, -97, -82, -6, -26, -85, -28, -37, -6, -47, -30,
       -14, -58, -25, -96, -83, -46, -15, -68, -35, -65, -44, -51, -88, -9, -77, -79, -89, -85, -4, -52, -55, -100, -33,
       -61, -77, -69, -40, -13, -27, -87, -95, -40]
print(maxSubArray(arr))
