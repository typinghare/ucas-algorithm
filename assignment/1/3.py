# # author: ShotgunRO
#
# # ---------- [ subject ] ----------
# # Given an integer array, one or more consecutive integers in the array form a sub-array. Find
# # the maximum value of the sum of all sub-arrays.
# # Please give an algorithm with O(nlogn) complexity.
#
#
# # ---------- [ code ] ----------
# def solve(arr: list, l: int, r: int) -> int:
#     # Conquer
#     if l == r:
#         return arr[l]
#
#     # Divide
#     mid = (l + r) >> 1  # middle index
#     left_solution = solve(arr, l, mid)
#     right_solution = solve(arr, mid + 1, r)
#
#     # Combine
#     # a probability that the sub-array go across division
#     # [left]
#     left_sum = left_max_sum = arr[mid]
#     for i in range(mid - 1, l-1, -1):
#         left_sum += arr[i]
#         if left_sum > left_max_sum:
#             left_max_sum = left_sum
#     # [right]
#     right_sum = right_max_sum = arr[mid + 1]
#     for i in range(mid + 2, r):
#         right_sum += arr[i]
#         if right_sum > right_max_sum:
#             right_max_sum = right_sum
#
#     return max(left_solution, right_solution, left_max_sum + right_max_sum)
#
#
# # ---------- [ test ] ----------
# arr = [5, 4, -1, 7, 8]
# result = solve(arr, 0, len(arr) - 1)
# print(result)
