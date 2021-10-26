def largest_divisible_subset(nums):
    S = {1: []}  # mapping: max number of list => list
    for num in sorted(nums):
        for m in list(S.keys()):
            # cuz we've sorted <nums>, <num> is certainly greater than <m>
            if num % m == 0:
                # <num> is divisible by <m> means <num> is divisible by any number in S[m] (this
                # can be proved by means of mathematical induction)
                # clone S[m] and append <num>, then insert it into S with key <num>
                S[num] = S[m][:] + [num]

    # we output the largest list in S
    # parameter <key> of function <max> is a map function
    return max(S.values(), key=len)


# ---------- [ test ] ----------
nums = [3, 8, 4, 5, 6, 12, 7, 16, 2]
result = largest_divisible_subset(nums)
print(result)
