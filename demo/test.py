import numpy as np

# 使矩阵的元素的类型为 int
matrix = np.zeros((3, 4), int)

# 最后一行赋值
matrix[2][0] = 1
matrix[2][1] = 3
matrix[2][2] = 4

# 输出最后一行最大的数
print(max(matrix[2]))

# arr = [3, 5, 7, 2, 1, 0]
# maxNumber = max(arr)
# minNumber = min(arr)
# print(maxNumber)
# print(minNumber)
