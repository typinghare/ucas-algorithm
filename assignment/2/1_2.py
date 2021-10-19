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
# iterative method
def money_robbing(i, selected=None):
    if selected is None:
        selected = []

    # recursion termination
    if i == n:
        return 0

    res_select = 0
    # if (i - 1) is included in [selected], only skip is allowed
    # otherwise, two situations are needed to consider
    if (i - 1) not in selected:
        # select
        selected.append(i)
        res_select = nums[i] + money_robbing(i + 1, selected)
        selected.remove(i)
    # skip
    res_skip = money_robbing(i + 1, selected)

    return max(res_select, res_skip)


# ---------- [ test ] ----------
# money of each house
nums = [1, 2, 3, 1]
n = len(nums)
print(money_robbing(0))
