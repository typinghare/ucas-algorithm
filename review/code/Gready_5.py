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


# 3. PPT 的意思
def solution3(nums):
    # c 为计数器（记录处理次数）
    c = 0

    for i in range(1, len(nums)):
        # "计算相邻元素的差值"
        diff = nums[i] - nums[i - 1]

        # "选择其中为负的差值，相加"
        if diff < 0:
            c += diff

    # "求反（指相反数，不是按位取反）"
    return -c


# test
nums = [4, 2, 6, 3, 9]
print(solution(nums[:]))
print(solution2(nums[:]))
print(solution3(nums[:]))
