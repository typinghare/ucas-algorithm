# author: ShotgunRO

# Algorithm 9 on page 29
# ---------- [ pseudocode ] ----------
# function INSERTION-SORT(A, n)
# if n == 1 then
#   return;
# else
#   INSERTION-SORT(A, n-1);
#   key = A[n-1];
#   i = n - 1;
#   while i >= 0 and A[i] > key do
#     A[i+1] = A[i]
#     i--;
#   end while
#   A[i+1] = key
# end if
# ------------------------------------

def insertion_sort(A: list, n: int):
    if n == 1:
        return
    else:
        insertion_sort(A, n - 1)
    pass
