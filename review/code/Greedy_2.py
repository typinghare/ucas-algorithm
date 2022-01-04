#
def solution(p, f):
    """
    :param p: time on the supercomputer
    :param f: time on the PCs
    :return: a schedule with as small a completion time as possible
    """

    # 根据网上的说法，对 f 进行排序，最优的 schedule 与 p 无关
    # 由于 Assignment 中要求翻回"a schedule"，因此只需要将一个序列列表与 f 一同进行排序即可
    # 网上说从大到小使用 merge sort 排序，其实其他排序方法也可以，这里用 quicksort 来排

    f_len = len(f)
    schedule = [i + 1 for i in range(f_len)]

    def quicksort(low, high):
        if low >= high:
            return

        # partition
        pivot = f[high]
        pi = low

        for i in range(low, high):
            if f[i] > pivot:
                f[pi], f[i] = f[i], f[pi]
                schedule[pi], schedule[i] = schedule[i], schedule[pi]
                pi += 1

        # pi 与 high 调换
        f[pi], f[high] = f[high], f[pi]
        schedule[pi], schedule[high] = schedule[high], schedule[pi]

        # 处理左右两部
        quicksort(low, pi - 1)
        quicksort(pi + 1, high)

    quicksort(0, f_len - 1)
    return schedule


# test
p = [10, 3, 5, 7]
f = [2, 7, 9, 4]  # sorted: [9, 7, 4, 2]
print(solution(p, f))   # prospect: [3, 2, 4, 1]
