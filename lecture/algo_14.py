# author: ShotgunRO
# Algorithm 14 on page 43

# ---------- [ pseudocode ] ----------
# function LOMUTO-QUICKSORT(A, l, r)
# if l<r then
#   p = PARTITION(A, l, r) // Use A[r] as pivot
#   LOMUTO-QUICKSORT(A, l, p-1)
#   LOMUTO-QUICKSORT(A, p+1, r)
# end if
#
# function PARTITION(A, l, r)
# pivot = A[r]; i = l;
# for j = l to r-1 do
#   if A[j] < pivot then
#     Swap A[i] with A[j];
#     i++;
#   end if
# end for
# Swap A[i] with A[r]; // Put pivot in its correct position
# return i;


# ---------- [ code ] ----------
def lomuto_quick_sort(A: list, l: int, r: int):
    if l < r:
        p = partition(A, l, r)  # Use A[r] as pivot
        lomuto_quick_sort(A, l, p - 1)
        lomuto_quick_sort(A, p + 1, r)


def partition(A: list, l: int, r: int):
    pivot = A[r]
    i = l
    for j in range(l, r):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    swap(A, i, r)
    return i


def swap(A: list, i: int, j: int):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# ---------- [ test ] ----------
A = [5, 2, 1, 4, 3]
lomuto_quick_sort(A, 0, len(A) - 1)
print(A)
