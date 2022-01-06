def solution(n, s):
    """
    :param n: 字符串长度
    :param s: 字符串
    """
    # 准备工作：记录 s 中不同字符的末位置
    memo = {}
    for i in range(n):
        memo[s[i]] = i

    partition, begin, end = [], 0, 0
    for i in range(n):
        end = max(end, memo[s[i]])
        if i == end:
            # 植树问题，要加 1
            partition.append(end - begin + 1)
            begin = end + 1
    return partition


# TEST
s = "ababcbacadefegdehijhklij"
print(solution(len(s), s))  # [9,7,8]
