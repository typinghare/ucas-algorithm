# [Toy Buildings]
# Bob has n toy buildings in a line, the i-th from left of which has height ai. He wants to
# make these building non-decreasing in height from left to right. In one operation, he can take
# any contiguous subsegment of them and add 1 to each of their heights.
# Help Bob find the minimum number of operations he needs to perform to make his toy
# buildings non-decreasing.
from typing import List, Tuple


def toyBuildings(n: int, buildings: List[int]) -> int:
    return 0


# Test
n = 5
buildings = [5, 7, 2, 4, 1]
print(toyBuildings(n, buildings))
