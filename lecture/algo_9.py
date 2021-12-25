# author: ShotgunRO
# Algorithm 9 on page 29

# ---------- [ pseudocode ] ----------
# function INSERTION-SORT(A, n)
# if n == 1 then
#   return;
# else
#   INSERTION-SORT(A, n-1);
#   key = A[n-1];
#   i = n - 1;      // may be "i = n - 2" ?
#   while i >= 0 and A[i] > key do
#     A[i+1] = A[i]
#     i--;
#   end while
#   A[i+1] = key
# end if


# ---------- [ code ] ----------
def insertion_sort(A: list, n: int):
    if n == 1:
        return
    else:
        insertion_sort(A, n - 1)  # To sort the subsequence which index from 0 to n-1
        key = A[n - 1]
        i = n - 2
        while i >= 0 and A[i] > key:  # Traverse from n-1 to 0, number that greater than key moves back
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key  # insert key into the right place


# ---------- [ test ] ----------
A = [5, 2, 1, 4, 3]
insertion_sort(A, len(A))
print(A)
