n = 5

a = [1, 2, 3, 4, 5]
b = [[0 for i in range(n)] for j in range(n)]
b[1][1] = 6

print(a)
print(b)
print(len(b))
