"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]


提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

from typing import List, Optional


class ListNode:
    def __init__(self, value: int = 0, next_node=None):
        self.val = value
        self.next = next_node


def get_linked_list(l: List[int], idx: int = 0):
    """
    获取链表
    :param l:
    :param idx:
    :return:
    """
    val = l[idx]
    if idx == len(l) - 1:
        return ListNode(val)
    else:
        idx += 1
        return ListNode(val, get_linked_list(l, idx))


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(0, head)
        curr_node = head
        length = 0
        while curr_node:  # 获取总共的节点数
            length += 1
            curr_node = curr_node.next

        curr_node = head
        curr_n = 1
        target_node = length - n + 1
        while curr_n < target_node - 1:  # 删除正数的第「总节点数-N+1」节点
            curr_n += 1
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next
        return head.next

    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_node = head
        length = 0
        while curr_node:
            length += 1
            curr_node = curr_node.next

        head = ListNode(0, head)  # 删除第1节点的情况特殊，增加一个第0节点
        target_node = length - n + 1
        curr_node = head
        ls = []
        for _ in range(1, target_node):
            ls.append(curr_node.val)
            curr_node = curr_node.next

        curr_node.next = curr_node.next.next
        return head.next

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        利用栈的原理，依次向栈中加入每个节点信息，然后再取出N个节点，此时栈中的最后一个节点为链表中的倒数第N-1个节点。
        :param head:
        :param n:
        :return:
        """
        head = ListNode(0, head)
        curr_node = head
        stack = []
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.next

        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return head.next

    def removeNthFromEnd3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(0, head)
        first = head
        for _ in range(n):
            first = first.next

        second = head
        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next
        return head.next


def check_result(links: Optional[ListNode], target: list):
    res_ls = []
    while links:
        res_ls.append(links.val)
        links = links.next
    print(f"结果：{res_ls}；正解：{target}")


if __name__ == '__main__':
    # print(f"{a}:{a_value}", f"{b}:{b_value}", f"{c}:{c_value}", f"{d}:{d_value}")

    sl = Solution()
    link_ls = get_linked_list([1, 2, 3, 4, 5])
    links_table = sl.removeNthFromEnd(link_ls, 2)
    check_result(links_table, target=[1, 2, 3, 5])

    link_ls = get_linked_list([1])
    links_table = sl.removeNthFromEnd(link_ls, 1)
    check_result(links_table, target=[])

    link_ls = get_linked_list([1, 2])
    links_table = sl.removeNthFromEnd(link_ls, 1)
    check_result(links_table, target=[1])

    link_ls = get_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    links_table = sl.removeNthFromEnd(link_ls, 5)
    check_result(links_table, target=[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13])

    link_ls = get_linked_list([1, 2, 3, 4])
    links_table = sl.removeNthFromEnd(link_ls, 4)
    check_result(links_table, target=[2, 3, 4])
