# see: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)

    # ensure the length of <nums1> is less than the length of <nums2>
    if m > n:
        nums1, nums2 = nums2, nums1
        m, n = n, m

    # the number of elements on the left side of parting line
    left_total = (m + n + 1) // 2

    # Find a proper paring line that separates <nums1>,
    # which make nums1[i-1] <= nums2[j] && nums2[j-1] <= nums1[i].
    # We want to find the parting position at <nums1> by means of binary search,
    # and <left> and <right> are pointer for it.
    left, right = 0, m
    while left < right:
        # i and j jointly
        i = (right + left + 1) // 2  # binary search
        j = left_total - i

        if nums1[i - 1] > nums2[j]:
            right = i - 1
        else:
            left = i

    i = left
    j = left_total - 1

    # below: <left> and <right> represent the median
    if i == 0:
        left = nums2[j - 1]
    if i == m:
        right = nums2[j]
    if j == 0:
        left = nums1[i - 1]
    if j == n:
        right = nums1[i]
    if i != 0 and i != m and j != 0 and j != n:
        left = max(nums1[i - 1], nums2[j - 1])
        right = max(nums2[i], nums2[j])

    if ((m + n) % 2) == 1:
        # the number of elements is an odd number
        return left
    else:
        # the number of elements is an even number
        return (left + right) / 2
