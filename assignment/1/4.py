# # author: ShotgunRO
#
# # ---------- [ subject ] ----------
# # Given an array of integers nums sorted in ascending order, find the starting and ending
# # position of a given target value. If the target is not found in the array, return [-1, -1].
# # For example, if the array is [5, 7, 7, 8, 8, 10] and the target is 8, then the output
# # should be [3, 4]
#
#
# # ---------- [ code ] ----------
# # def solve(arr, target, l, r):
# #     # Conquer
# #     if l == r:
# #         # if the only one element in array equals to target, (0, 0) is returned,
# #         # (-1, -1) is returned otherwise.
# #         return (0, 0) if arr[l] == target else (-1, -1)
# #
# #     # Divides
# #     m = (l + r) >> 1  # medium index
# #     left = solve(arr, target, l, m) if arr[m] >= target else (-1, -1)
# #     right = solve(arr, target, m + 1, r) if arr[m + 1] <= target else (-1, -1)
# #
# #     # Combine
# #     deviation = m - l + 1
# #     if left[0] == -1:
# #         # in this case, left part does not contain target element.
# #         # left == (-1, -1)
# #         return left if right[0] == -1 else (right[0] + deviation, right[1] + deviation)
# #     else:
# #         # in this case, left part contains at least one target element.
# #         return left if right[0] == -1 else (left[0], right[1] + deviation)
#
# def solve(arr, target, l, r):
#     # Conquer
#     if l == r:
#         # leaf node position
#         return (r, r) if arr[r] == target else (-1, -1)
#
#     # Divides
#     m = (l + r) >> 1
#     left = solve(arr, target, l, m) if arr[m] >= target else (-1, -1)
#     right = solve(arr, target, m + 1, r) if arr[m + 1] <= target else (-1, -1)
#
#     # Combine
#     if left[0] == -1:
#         # in this case, left half does not contain target element.
#         return right
#     else:
#         # in this case, left part contains at least one target element.
#         return left if right[0] == -1 else (left[0], right[1])
#
#
# # ---------- [ test ] ----------
# arr = [5, 7, 7, 8, 8, 10]
# target = 7
# result = solve(arr, target, 0, len(arr) - 1)
# print(result)
#
# # ---------- [ correctness ] ----------
# # Loop invariant: answer = [min(left[0], right[0]), max(left[1], right[1])
# # left[0] <= starting <= right[0], left[1] <= ending <= right[1]
