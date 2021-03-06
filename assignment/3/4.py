# [Permutation Partition]
# Bob is given a permutation p1, p2, . . . , pn of integers from 1 to n and an integer k, such that
# 1 ≤ k ≤ n. A permutation means that every number from 1 to n is contained exactly once.
# Consider all partitions of this permutation into k disjoint segments. Formally, a partition is
# a set of segments {[s0, s1], [s1 + 1, s2], . . . , [sk 1 + 1, sk]}, such that: 1 = s0 < s1 < s2 < . . . <
# sk 1 < sk = n. Two partitions are different if there exists a segment that lies in one partition
# but not the other.
# Bob wants to calculate the partition value, defined as Pki=1 maxsi 1≤j≤sipj for all possible
# partitions of the permutation into k disjoint segments. Please help him find the maximum
# possible partition value over all such partitions, and the number of ways to make partition with
# this value.

# see: https://codeforces.com/problemset/problem/1326/C
from typing import List, Tuple


def permutationPartition(n: int, k: int, permutation: List[int]) -> Tuple[int, int]:
    return 1, 2


# Test
permutation = [2, 2, 3, 4, 4]
n = len(permutation)
k = 5
print(permutationPartition(n, k, permutation))

# 【1,2], [2,4], [6,6]