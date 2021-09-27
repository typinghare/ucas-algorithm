# exercise 1 2021.9.26 17:50 Time: 30min39 没写出来

def SumArray(A, l, r):
    # conquer
    if l == r:
        return A[l]

    # divide
    mid = (l + r) // 2
    left = SumArray(A, l, mid)
    right = SumArray(A, mid + 1, r)

    # combine
    cross_left = A[mid]
    max_left = cross_left
    cross_right = A[mid + 1]
    max_right = cross_right

    for i in range(mid - 1, l - 1, -1):
        cross_left = cross_left + A[i]
        if cross_left > max_left:
            max_left = cross_left
    for j in range(mid + 2, r + 1):
        cross_right = cross_right + A[j]
        if cross_right > max_right:
            max_right = cross_right

    cross = max_left + max_right

    return max(left, right, cross)


A = [-2, 6, -1, 5, 4, -7, 2, 3]
l = 0
r = len(A) - 1
print(SumArray(A, l, r))
