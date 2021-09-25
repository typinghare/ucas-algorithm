# author: ShotgunRO
# Algorithm 12 on page 37

# ---------- [ pseudocode ] ----------
# function QUICK-SORT(A)
# if ‖A‖ == 1 then
#   return;
# end if
# Create two empty arrays S- and S+;
# Choose an element A[j] form A uniformly at random and use it as pivot;
# for i = 0 to ‖A‖ -1 do:
# Put A[i] into S- if A[i] < A[j] and put A[i] into S+ otherwise;
# end for
# QUICK-SORT(S+);
# QUICK-SORT(S-);
# Return the concatenation of S-, A[j], and S+ as A;

# ---------- [ code ] ----------
def quick_sort(A):
    if len(A) <= 1:
        return A
    left = []
    right = []
    # choose one as pivot, here choose the first element
    p = A[0]
    for i in range(1, len(A)):
        left.append(A[i]) if A[i] < p else right.append(A[i])
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [p] + right


# ---------- [ test ] ----------
A = [5, 2, 1, 4, 3]
result = quick_sort(A)
print(result)
