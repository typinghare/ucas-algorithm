# for <variable> in <string|list|tuple|set|dict>


# string
# for i in 'hello':
#     print(i)

# list
# for i in [1, 2, 3]:
#     print(i)

# tuple
# for i in ('a', 'b', 'c'):
#     print(i)

# set
# for i in {1, 2, 2, 3}:
#     print(i)

# dict
# key-value
__dict = {'apple': 'red', 'orange': 'yellow', 'avocado': 'green'}
# for key in __dict:
#     print(key)

# for key, value in __dict.items():
#     print(key, '-', value)

# -------------------
# range(start, stop [, step = 1])
# for i in range(5):  # range(0, 5) # 前闭后开
#     print(i)

# for i in range(2, 5):
#     print(i)

for i in range(5, 2, -1):
    print(i)