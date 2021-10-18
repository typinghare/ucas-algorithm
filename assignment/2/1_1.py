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
def money_robbing(S, n):
    if len(S) == 0:
        return 0

    max_opt = 0
    for h in S:  # h = house
        m = money_map[h]
        _S = renew_set(S, h, n)
        opt = m + money_robbing(_S, n)
        if opt > max_opt:
            max_opt = opt
    return max_opt


def renew_set(S, choice, n):
    _S = S[:]  # clone a new set
    _S.remove(choice)

    left = choice - 1
    right = choice + 1

    # if left adjacent has been chosen, right adjacent is banned
    if left >= 0 and left not in _S and right in _S:
        _S.remove(right)

    # if right adjacent has been chosen, left adjacent is banned
    if right < n and right not in _S and left in _S:
        _S.remove(left)

    # check left adjacent
    if left in _S and left > 0 and (left - 1) not in _S:
        _S.remove(left)
    if left not in _S and left > 0 and (left - 1) in _S:
        _S.remove(left - 1)

    # check right adjacent
    if right in _S and right < n - 1 and (right + 1) not in _S:
        _S.remove(right)
    if right not in _S and right < n - 1 and (right + 1) in _S:
        _S.remove(right + 1)
    return _S


# ---------- [ test ] ----------
# house_number => money
money_map = {
    0: 6,
    1: 9,
    2: 5,
    3: 4
}
S = list(money_map.keys())
result = money_robbing(S, len(S))
print(result)
