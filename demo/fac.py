def factorial(n):
    # 求 n!
    # n! = (n-1)! * n
    # 递归： 一定有终止
    # callstack（函数调用栈）溢出 ？
    if n == 1:
        return 1
    return factorial(n - 1) * n


print(factorial(4))

def solve(n):
    # 1, 1, 2, 3, 5
    if n == 1 or n == 2:
        return 1
    return solve(n - 1) + solve(n - 2)
