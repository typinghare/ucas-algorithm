def solution(monkeys, banana):
    monkeys.sort()
    banana.sort()
    n = len(monkeys)

    max_time = abs(monkeys[0] - banana[0])
    for i in range(1, n):
        d = abs(monkeys[i] - banana[i])
        if d > max_time:
            max_time = d

    return max_time


# test
monkeys = [1, 5, 7, 9, 10]
banana = [8, 2, 4, 12, 11]
print(solution(monkeys, banana))
