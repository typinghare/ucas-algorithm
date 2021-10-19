# author: ShotgunRO

# ---------- [ subject ] ----------
# <Money robbing>
# A robber is planning to rob houses along a street. Each house has a certain amount of
# money stashed, the only constraint stopping you from robbing each of them is that
# adjacent houses were broken into on the same night.
# 1. Given a list of non-negative integers representing the amount of money of each
#    house, determine the maximum amount of money you can rob tonight without alerting
#    the police.
# 2. What if all houses are arranged in a circle?


# ---------- [ code ] ----------
def money_robbing(nums):
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


# ---------- [ test ] ----------
# money of each house
nums = [1, 2, 3, 1]
print(money_robbing(nums))
