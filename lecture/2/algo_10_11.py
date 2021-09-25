# author: shotgun
# Algorithm 10 on page 31

# ---------- [ pseudocode ] ----------
# function MERGE-SORT(A, l, r)
# if l < r then
#   m = ⌈(l+2)/2⌉; // m denotes the middle point
#   MERGE-SORT(A, l, m);
#   MERGE-SORT(A, m + 1, r);
#   MERGE(A, l, m, r); // Merge the sorted Arrays
# else
#   return;
# end if
#
# function MERGE(A, l, m, r)
# Require: A[l..m] (denoted as L) and A[m+1..r] (denoted as R) have already been sorted.
# i = 0; j = 0;
# for k = l to r do
#   if L[i] > R[j] then
#     A[k] = R[j];
#     j++;
#     if all elements in R have been copied then
#       Copy the remainder elements from L into A
#       break;
#     end if
#   else
#     A[k] = L[i]
#     i++;
#     if all elements in L have been copied then
#       Copy the remainder elements from R into A;
#       break;
#     end if
#   end if
# end for

# ---------- [ code ] ----------
import math


def merge(A, l, m, r):
    L = A[l:m + 1]
    R = A[m + 1:r + 1]
    i = j = 0
    for k in range(l, r + 1):
        if L[i] > R[j]:
            A[k] = R[j]
            j += 1
            if j >= len(R):
                # Copy the remainder elements from L to A:
                A[k + 1:r + 1] = L[i:]
                break
        else:
            A[k] = L[i]
            i += 1
            if i >= len(L):
                # Copy the remainder elements from R to A:
                A[k + 1:r + 1] = R[j:]
                break


def merge_sort(A, l, r):
    if l < r:
        m = math.floor((l + r) / 2)
        merge_sort(A, l, m)
        merge_sort(A, m + 1, r)
        merge(A, l, m, r)
    else:
        return


# ---------- [ test ] ----------
A = [5, 2, 1, 4, 3]
merge_sort(A, 0, len(A) - 1)
print(A)
