from typing import List


# 求 arr 中的最大值（python 内置的 max 函数的原理是什么？）
def builtin_max(arr: List[int]) -> int:
    max_so_far = arr[0]
    for e in arr:
        if max_so_far < e:
            max_so_far = e
    return max_so_far


# Test
arr = [5, 4, 6, 9, 1, 2]
print(builtin_max(arr))
