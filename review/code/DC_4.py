# 1. 递归
def solve(arr, target, l, r):
    if len(arr) == 0:
        return (-1, -1)

    # conquer
    if l == r:
        # leaf node position
        return (r, r) if arr[r] == target else (-1, -1)

    # divides
    m = (l + r) >> 1
    left = solve(arr, target, l, m) if arr[m] >= target else (-1, -1)
    right = solve(arr, target, m + 1, r) if arr[m + 1] <= target else (-1, -1)

    # combine
    if left[0] == -1:
        # in this case, left half does not contain target element.
        return right
    else:
        # in this case, left part contains at least one target element.
        return left if right[0] == -1 else (left[0], right[1])


# 2. 迭代，二分（16 min）
def solve2(A, target):
    # 最终的返回值
    ret = [-1, -1]

    # 空数组情况
    if len(A) == 0:
        return ret

    # 查找左边界
    # 迭代变量，target 的边界始终控制在 [l, r] 区间中
    l, r = 0, len(A) - 1
    mid = l + r >> 1
    while l < r:
        if A[mid] < target:
            l = mid + 1
        elif A[mid] > target:
            r = mid - 1
        else:
            # A[mid] == target
            # 由于寻找的是左边界，这时候 mid 一定等于左边界或在左边界的右侧
            r = mid
        # 这里更新 mid 很重要，一定要向下取整，否则当一次循环后恰好出现 r = mid，
        # l = mid - 1 时，若向上取整就会进入死循环，向下取整就会更新 l （进入第一分支）
        mid = l + r >> 1

    if A[l] == target:
        # 记录左边界
        ret[0] = l
    else:
        # 左边界不存在，右边界也一定不存在
        return ret

    # 查找右边界（镜像）
    # 迭代变量重新初始化
    l, r = 0, len(A) - 1
    mid = l + r >> 1
    while l < r:
        if A[mid] < target:
            l = mid + 1
        elif A[mid] > target:
            r = mid - 1
        else:
            # A[mid] == target
            # 由于寻找的是右边界，这时候 mid 一定等于右边界或在右边界的左侧
            l = mid
        # 同上，这里一定要向上取整，否则当一次循环后恰好出现 l = mid，
        # r = mid + 1 时，若向下取整会进入死循环，向上取整则会更新 r （进入第二分支）
        mid = 1 + l + r >> 1

    # 记录右边界
    ret[1] = l
    return ret


# test
arr = [5, 7, 7, 8, 8, 10]
# print(solve(arr, 7, 0, len(arr) - 1))
print(solve2(arr, 8))
