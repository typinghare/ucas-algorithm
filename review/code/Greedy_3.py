# 1. Greedy（4.5 min）
def solution(n, l, p):
    """
    :param n: 人数
    :param l: 船的最大载重
    :param p: 人的体重（向量）
    """
    p.sort()
    # i 和 j 为双指针，c 为计数器（counter）
    i, j, c = 0, len(p) - 1, 0

    while i <= j:
        if p[j] + p[i] <= l:
            i += 1
        j -= 1
        c += 1

    return c


# test
l, p = 6, [1, 1, 2, 3, 4, 5, 5, 6]
print(solution(len(p), l, p))
