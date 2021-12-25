# 1. 递归（8 min）
def solve(s, word_dict):
    """
    :param s: 要处理的字符串
    :param word_dict: 字符串列表
    """
    length = len(s)
    for i in range(length):
        if s[:i + 1] in word_dict:
            # 如果 curr 在列表中，将 s 分为前后两部
            # 前部为 curr，后部为其后的字符串
            # 1. 如果后部为空，则返回 True
            # 2. 如果后部不为空，则将后部进行递归，如果结果为 True，那就返回 True
            if i == length - 1 or solve(s[i + 1:], word_dict):
                return True

    # 遍历完了，还没返回 True，说明不行，返回 False
    return False


# 2. 迭代（20 min）
def solve2(s, word_dict):
    length = len(s)  # 给定字符串的长度
    segment = []  # 记录分块
    left = 0  # 当前分块左下标

    i = 0
    while i < length:
        # 如果匹配
        if s[left:i + 1] in word_dict:
            # 无后部，返回 True
            if i == length - 1:
                return True

            # 有后部，将当前分块的左下标记入 segment，更新左下标
            segment.append(left)
            left = i + 1
            i += 1
        # 如果不匹配，且 s 中的所有字符都已经遍历完毕
        elif i == length - 1:
            # 如果 segment 为 0，说明无任何匹配可能，直接返回 False
            if len(segment) == 0:
                return False
            # 如果 segment 不为 0，回溯
            i = left
            left = segment.pop()
        # 一般的不匹配情况
        else:
            i += 1


# test
s = "applepenapple"
word_dict = ["apple", "pen"]
print(solve(s, word_dict), solve2(s, word_dict))
