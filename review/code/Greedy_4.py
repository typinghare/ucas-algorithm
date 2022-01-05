import random


# 1. 假设一个分割中可以仅包含一个元素
def solution(nums, k):
    # 要使得分割的最大值的和最大，那么最大的 k 个数必然存在于每个分割中
    # 假设最大的 k 个数组成集合 A，我们在一次遍历中定位所有 A 中的元素，
    # 并用列表记录两个这样的元素间的距离
    # 在计算分割的组合时，我们把每个元素间的分割可能性相乘即可
    # 如果两个 A 元素间有 d 个元素，那么这个间隔内的分割可能性总数为：
    # C(d+1,2)+(d+1) = (d+1)d / 2 + (d+1) = (d+1)(d+2) / 2
    nums_len = len(nums)
    j, cv, distances = 0, nums_len - k, []
    for i in range(nums_len):
        if nums[i] > cv:
            distances.append(i - j)
            j = i + 1
    distances.append(nums_len - j)

    ret = 1
    for d in distances:
        ret *= (d + 1) * (d + 2) // 2
    return ret


n, k = 6, 2
nums = [i + 1 for i in range(n)]
random.shuffle(nums)  # 生成一个 1 ~ n 的排列
print(f"nums: {nums}")
print(solution(nums, k))
