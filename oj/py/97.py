# see: https://leetcode.com/problems/valid-parenthesis-string/

# [Wrong answer]
# don't know which part goes wrong
# def checkValidString(s: str) -> bool:
#     stack = 0  # number of '('
#     star = 0  # number of '*'
#     for c in s:
#         if c == '(':
#             stack += 1
#         elif c == ')':
#             if stack > 0:
#                 stack -= 1
#             else:
#                 if star == 0:
#                     return False
#                 # consume star
#                 star -= 1
#         else:
#             star += 1
#     return star >= stack

# reference: https://leetcode.com/problems/valid-parenthesis-string/discuss/543521/Java-Count-Open-Parenthesis-O(n)-time-O(1)-space-Picture-Explain
# 这个方法比较难理解，大意是：由于我不知道 * 可能是哪种情况，所以我干脆在遍历的过程中讨论所有可能的情形，具体操作如下：
# （必须结合连接中的图进行理解）（虽然这个方法很难想，但 Leetcode 上 Discuss 的前三都是这种方法及其变种，所以还是得掌握）
# 1. 用 cmax 保存直至当前字符，在所有可能分支中，待匹配的 '(' 的个数的最大值
# 2. 用 cmin 保存直至当前字符，在所有可能分支中，待匹配的 '(' 的个数的最小值
# 遍历字符串：
# 1. 若当前字符为 '(' ，则 cmin 和 cmax 都自增 1
# 2. 若当前字符为 ')' ，则 cmin 和 cmax 都自减 1。若 cmin < 0，则令 cmin = 0，即抛弃那些不成立的分支
# 3. 若当前字符为 '*' ，对应了三种可能的情形：
#    a. '*' 取 '(': cmax 自增 1
#    b. '*' 取 ')': cmin 自减 1
#    c. '*' 取 '': 无变化
#    由于要同时考虑以上三种情况，所以在此分支下，cmax 自增 1，cmin 自减 1
# 4. 在进行上述操作后，如果 cmax 小于 0，则意味着没有任何一个分支满足题目的要求，直接返回 False
# 遍历字符串后，cmin 为 0 则表明有至少一条分支满足：无待匹配的 '('，故返回 True
# 如果 cmin > 0，表明没有一条分支满足无待匹配的 '('，故返回 False
def checkValidString(s: str) -> bool:
    cmin, cmax = 0, 0
    for c in s:
        if c == '(':
            cmin += 1
            cmax += 1
        elif c == ')':
            cmin -= 1
            cmax -= 1
        elif c == '*':
            cmin -= 1
            cmax += 1
        if cmax < 0:
            return False
        if cmin < 0:
            cmin = 0
    return cmin == 0


# TEST
# s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
# print(checkValidString(s))  # False

# OJ
s = input()[:-1]
print("True" if checkValidString(s) else "NO")
