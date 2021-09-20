# author: ShotgunRO

# ---------- [ subject ] ----------
# Given an integer array nums and an integer k, please return the k-th largest element
# in the array. Your algorithm's runtime complexity must be in the order of O(nlogn),
# prove the correctness and analyse the complexity. (k is much smaller than n, n is the
# length of the array.)


# ---------- [ code ] ----------
import math


def partition(arr: list):
    pivot = arr[0]
    les = [x for x in arr if x <= pivot]  # set consists of element that less than or equal pivot
    gs = [x for x in arr if x > pivot]  # set consists of element that greater than pivot
    return les, gs, pivot


def get_k_th_largest(arr: list, ordinal: int):
    (les, gs, pivot) = partition(arr)
    if len(gs) > ordinal:
        return get_k_th_largest(gs, ordinal)
    elif len(gs) == ordinal:
        # pivot is the smallest number in les
        return pivot
    else:
        # len(gs) < ordinal
        if len(les) > ordinal:
            return get_k_th_largest(les, ordinal - len(gs))
        else:
            ordinal -= len(gs)
            smallest = les[0]
            for i in range(1, ordinal):
                if smallest > gs[i]:
                    smallest = gs[i]
            return smallest


def find_target_element(arr: list, ordinal: int) -> list:
    l = len(arr)
    if len(arr) < 2 * ordinal:
        # not enough to divide, return a set of elements, each of which is less than the
        # k-th largest number in the list
        pns = []  # possible numbers set
        for i in range(0, len(arr)):
            arr.sort()  # ascending sort
            return arr[0:ordinal]

    m = math.ceil(l / 2)
    right_pns = find_target_element(arr[0:m], ordinal)
    left_pns = find_target_element(arr[m:l], ordinal)

    # combine
    new_arr = []
    i = 0
    j = 0
    for k in range(0, 4):
        if left_pns[i] > right_pns[j]:
            new_arr.append(right_pns[j])
            j += 1
        else:
            new_arr.append(left_pns[i])
            i += 1
    return new_arr


# ---------- [ test ] ----------
arr = [4, 3, 6, 9, 7, 2, 1, 4, 3, 2, 8]
print(get_k_th_largest(arr, 2))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
