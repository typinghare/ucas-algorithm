n = 100  # 假设这是问题的规模

# 这种是循环的规模与问题规模有关，且一层循环，故 O(n)
for i in range(n):
    pass

# 这种是循环的规模是常数级别的，故 O(1)
for i in range(3):
    pass

# 这种是循环的规模与问题规模有关，且两层循环，故 O(n^2)
for i in range(n):
    for j in range(n):
        pass

# 这种是循环的规模与问题规模有关，外层循环与 n 相关，
# 内层是常数级别，故为 O(n)
for i in range(n):
    for j in range(3):
        pass
