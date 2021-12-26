class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 合并两个有序链表，递增（7 min）
def merge_linked_list(list1, list2):
    # point1 和 point2 是动态节点（理解成指针也可以）
    point1, point2 = list1, list2

    # 新链表的头节点（头节点是空的，在返回时会被舍弃）
    # point 是新链表的动态节点
    point = head = ListNode()

    while point1 is not None and point2 is not None:
        if point1.val < point2.val:
            point.next = point1  # node 插入 node1
            point1 = point1.next  # 过渡到下一节点
        else:
            point.next = point2  # node 插入 node2
            point2 = point2.next
        point = point.next  # 过渡到下一节点

    # 将 list1 或 list2 剩余的节点插入的新链表的末端
    if point1 is not None:
        point.next = point1
    else:
        point.next = point2

    # 舍弃头节点，返回剩下的链表
    return head.next


# 1. 递归，多次均分（5 min）
def solve(lists):
    length = len(lists)

    # conquer
    if length == 0:
        return None
    if length == 1:
        # return the only list
        return lists[0]

    # divide
    mid = length >> 1
    list1 = solve(lists[:mid])
    list2 = solve(lists[mid:])

    # combine - 合并 list1 and list2
    return merge_linked_list(list1, list2)


# 2. 迭代 (8 min)
def solve2(lists):
    curr_lists = lists  # 当前迭代要处理列表
    next_lists = []  # 下一轮迭代要出的列表
    length = len(curr_lists)  # 当前迭代要处理的列表的长度

    while length > 1:
        # 合并第一和第二个列表、第三和第四个列表，以此类推
        # 注意：a >> 1 表示取 a 的半数向下取整；a + 1 >> 1 则表示 a 的半数向上取整
        for i in range(1 + length >> 1):
            if 2 * i + 1 < length:
                next_lists.append(merge_linked_list(curr_lists[2 * i], curr_lists[2 * i + 1]))
            else:
                # 没人跟它组的，单身狗属于是
                next_lists.append(curr_lists[2 * i])
        # 更新迭代变量
        curr_lists = next_lists
        next_lists = []
        length = len(curr_lists)

    return curr_lists[0]


# 3. 迭代，leetcode 版（12 min）
def solve3(lists):
    length = len(lists)
    interval = 1  # 迭代间隔

    while length > interval:
        # 右区间为 length - interval 的原因是：
        # 当 i 为 length - interval - 1 时，i + interval 恰好是最后一个元素的下标
        # 可以由此证明列表中的所有元素都被遍历
        for i in range(0, length - interval, interval * 2):
            lists[i] = merge_linked_list(lists[i], lists[i + interval])
        interval *= 2

    return lists[0]


s = [
    ListNode(1, ListNode(3, ListNode(8))),
    ListNode(2, ListNode(4, ListNode(5))),
    ListNode(0, ListNode(6, ListNode(7))),
]

# r = solve(s)
r = solve3(s)
while r is not None:
    print(r.val)
    r = r.next
