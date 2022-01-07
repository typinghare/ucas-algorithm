def solution(N, H, D):
    """
    :param N: 敌方英雄总数
    :param H: 敌方英雄的生命值（HP）
    :param D: 敌方英雄的伤害输出（DPS）
    :return: 我方英雄损失的 HP 值
    """
    # 计算 DPS / HP 的值并存储
    M = [D[i] / H[i] for i in range(N)]

    # 对 M 进行升序排序，order 为对应的英雄索引
    order = [i for i in range(N)]  # [0, 1, ..., N-1]
    order = [x for _, x in sorted(zip(M, order))]

    DPS_sum = sum(D)  # 敌人的总 DPS
    L = 0  # 我方英雄损失的 HP 值
    for i in range(N):
        j = order[N - i - 1]  # 当前攻击的敌人
        L += DPS_sum * H[j]  # 击败该敌人过程中损失的 HP 值
        DPS_sum -= D[j]  # 减去阵亡英雄的 DPS

    return L


# test
H = [105, 26, 49, 12]  # 696 + 962 + 1225 + 1050
D = [10, 12, 15, 21]  # 58 -> 37 -> 25 -> 10
print(solution(4, H, D))  # 3933
