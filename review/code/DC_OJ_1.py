DIVISOR = 1337


def super_pow(a, b):
    # a ^ b / DIVISOR
    if len(b) == 0:
        return 1
    ld = b.pop()  # last digit in b
    return pow_mod(super_pow(a, b), 10) * pow_mod(a, ld) % DIVISOR


def pow_mod(a, c):
    # 0 <= k <= 10
    a %= DIVISOR
    ret = 1
    for i in range(c):
        ret = ret * a % DIVISOR
    return ret
