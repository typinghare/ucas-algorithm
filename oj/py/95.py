# author: ShotgunRO

# <Triangle>
# leetcode 120 - https://leetcode.com/problems/triangle/
# Accepted

# def minimumTotal(triangle):
#     """
#     :param triangle: List[List[int]]
#     :return: int
#     """
#     height = len(triangle)
#     min_path = triangle[height - 1]
#     for layer in range(height - 2, -1, -1):
#         # for each layer, check it's every node
#         # choose the smaller child and add to itself, then update min_path
#         for i in range(0, layer + 1):
#             min_path[i] = triangle[layer][i] + min(min_path[i], min_path[i + 1])
#     return min_path[0]


# triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
# print(minimumTotal(triangle))

# --------------------------------------------------------------------------
# def minimumTotal(height, triangle):
#     """
#     :param height: int
#     :param triangle: List[List[int]]
#     :return: int
#     """
#     min_path = triangle[height - 1]
#     for layer in range(height - 2, -1, -1):
#         # for each layer, check it's every node
#         # choose the smaller child and add to itself, then update min_path
#         for i in range(0, layer + 1):
#             min_path[i] = triangle[layer][i] + min(min_path[i], min_path[i + 1])
#     return min_path[0]
#
#
# # INPUT
# height = int(input())
# tr = map(int, input()[:-1].split(' '))
# triangle = []
# start = 0
# for i in range(height):
#     triangle.append(tr[start:start + i + 1])
#     start += i + 1
#
# # OUTPUT
# print(minimumTotal(height, triangle))

# --------------------------------------------------------------------------
# faster version
def minimumTotal(height, triangle):
    start = (height - 1) * height // 2
    min_path = triangle[start:]
    for layer in range(height - 2, -1, -1):
        start -= layer + 1
        for i in range(0, layer + 1):
            min_path[i] = triangle[start + i] + min(min_path[i], min_path[i + 1])
    return min_path[0]


# INPUT
height = int(input())
triangle = list(map(int, input().split(' ')))

# OUTPUT
print(minimumTotal(height, triangle))
