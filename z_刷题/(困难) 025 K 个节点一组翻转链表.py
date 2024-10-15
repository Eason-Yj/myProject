"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

示例 1：
输入：head = [1,2,3,4]
输出：[3, 2, 1, 4]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

示例 4：
输入：head = [1,2,3,4,5,6,7]
输出：[3, 2, 1, 6, 5, 4, 7]
"""

from typing import List
from typing import Optional
from typing import Union
from typing import Any


class ListNode:

    def __init__(self, value: int = 1, next_node=None):
        """

        :param value:
        :param next_node:
        """
        self.val = value
        self.next = next_node


def get_links_list(all_ls: Union[List[List], List]) -> Optional[List[ListNode]]:
    if not all_ls:
        return None

    def run(_ls: List) -> Optional[ListNode]:

        if len(_ls) == 1:
            return ListNode(value=_ls[-1])
        else:
            val = _ls.pop(0)
            return ListNode(value=val, next_node=run(_ls))

    if isinstance(all_ls[0], list):
        return [run(ls.copy()) for ls in all_ls if ls]
    else:
        return run(all_ls.copy())


def check_links_list(lks: Union[ListNode, List[ListNode]], target: List = None):
    result_ls = []
    if isinstance(lks, list):
        for lk in lks:
            res_ls = []
            while lk:
                res_ls.append(lk.val)
                lk = lk.next
            result_ls.append(res_ls)
    else:
        while lks:
            result_ls.append(lks.val)
            lks = lks.next
    print(f"{result_ls}; 正解：{target}")


class Solution:
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法一：
        思路：直接生成 next_node (val为当前节点的val，next为当下一个节点的next)，
        在将当前节点的val赋值为下一节点的val，next为生成的next_node
        :param head:
        :return:
        """
        if not head:
            return None

        curr_node = head
        while curr_node and curr_node.next:
            next_node = ListNode(curr_node.val, curr_node.next.next)
            curr_node.val, curr_node.next = curr_node.next.val, next_node
            curr_node = next_node.next
        return head

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法二：
        思路：利用交换的两个节点的上一个节点「node0」进行交换，
        交换后的node0的next为node2，node1的next为node2的next，node2的next为此时的node1
        :param head:
        :return:
        """
        if not head:
            return None

        head = node0 = ListNode(0, head)
        while node0.next and node0.next.next:
            node1, node2 = node0.next, node0.next.next
            node0.next = node2
            node1.next = node2.next
            node2.next = node1
            node0 = node1

        return head.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        方法三：递归处理，终止条件为链表中的节点为空或节点只有一个
        每轮的new_head为 head的next，而此时head的next为下一轮的new_head，则每轮返回new_head
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head
        else:
            new_head = head.next
            curr_node = head
            for _ in range(k):
                node1, node2 = curr_node.next, curr_node
                node2.next = node1.next
                node1.next = node2
                curr_node = curr_node.next

            head.next = self.reverseKGroup(curr_node, k)
            new_head.next = head
            return new_head


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    prev = None
    curr = head
    while curr:
        next_n = curr.next
        curr.next = prev
        prev = curr
        curr = next_n


if __name__ == '__main__':
    sl = Solution()
    lst = [1, 2, 3, 4, 5]
    lik = get_links_list(lst)
    check_links_list(sl.swapPairs(lik), [3, 2, 1, 4, 5])

    lst = [1, 2, 3, 4, 5, 6, 7]
    lik = get_links_list(lst)
    check_links_list(sl.swapPairs(lik), [3, 2, 1, 6, 5, 4, 7])

    lst = [1]
    lik = get_links_list(lst)
    check_links_list(sl.swapPairs(lik), [1])

    lst = []
    lik = get_links_list(lst)
    check_links_list(sl.swapPairs(lik), [])
