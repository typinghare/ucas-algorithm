# 假设有一个包含n个二元组数组L，每个二元组均由两个0~100的整数组成。设计一个算法，找出数组中所有
# 相同的二元组，并将他们的下标返回

# Example 1
# Input:    [(34, 25), (17, 22), (34, 56), (34, 25)]
# Output:   [[0, 3]]
# Explanation: Input 中有两个相同的二元组，即 (34, 25)，它们对应的下标为 0 和 3

# Example 2
# Input:    [(91, 24), (39, 6), (39, 6), (91, 24), (39, 6)]
# Output:   [[0, 3], [1, 2, 4]]
# Explanation: Input 中有两组二元组，分别为 (91, 25) 和 (39, 6)。(91, 25) 对应的下标为 0 和 3，
#              (39, 6) 对应的下标为 1, 2 和 4
from typing import List, Tuple


def solve(arr: List[Tuple[int]]) -> List[List[int]]:
    pass
