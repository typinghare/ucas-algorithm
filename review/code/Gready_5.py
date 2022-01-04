# 1. 按部就班
def solution(nums):
    # i 为指针变量，c 为计数器（记录处理次数）
    length, i, c = len(nums), 1, 0

    while i < length:
        if nums[i] < nums[i - 1]:
            # 连续子区间元素增 1
            for k in range(i, length):
                nums[k] += 1
            c += 1
        else:
            # 继续处理后方的元素
            i += 1
    return c


class A:
    def __iter__(self):
        pass


# 2. 取巧型
def solution2(nums):
    # i 为指针变量，c 为计数器（记录处理次数）
    length, i, c = len(nums), 1, 0

    while i < length:
        if nums[i] < nums[i - 1]:
            m = nums[i - 1] - nums[i]
            # 连续子区间元素增 m
            for k in range(i, length):
                nums[k] += m
            c += m
        else:
            # 继续处理后方的元素
            i += 1

    return c


# test
nums = [4, 2, 6, 3, 9]
print(solution(nums[:]))
print(solution2(nums[:]))
