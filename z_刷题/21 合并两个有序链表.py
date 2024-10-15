"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

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
    if not l:
        return []

    val = l[idx]
    if idx == len(l) - 1:
        return ListNode(val)
    else:
        idx += 1
        return ListNode(val, get_linked_list(l, idx))


class Solution:
    def mergeTwoLists0(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        遍历
        :param list1:
        :param list2:
        :return:
        """
        if not list1:
            return list2
        elif not list2:
            return list1

        new_links = ListNode()
        curr_node = new_links
        val1, val2 = list1.val, list2.val
        while list1 or list2:
            curr_node.next = ListNode()
            curr_node = curr_node.next
            val1 = list1.val if list1 else val1
            val2 = list2.val if list2 else val2
            if (list1 and val1 <= val2) or (list1 and list2 is None):
                curr_node.val = val1
                list1 = list1.next
            else:
                curr_node.val = val2
                list2 = list2.next

        return new_links.next

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        遍历
        :param list1:
        :param list2:
        :return:
        """
        new_links = ListNode(-1)
        curr_node = new_links
        while list1 and list2:
            if list1.val <= list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        curr_node.next = list1 if list1 else list2
        return new_links.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归的方式
        :param list1:
        :param list2:
        :return:
        """
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def check_result(links: Optional[ListNode], target: list):
    res_ls = []
    while links:
        res_ls.append(links.val)
        links = links.next
    print(f"结果：{res_ls}；正解：{target}")


if __name__ == '__main__':
    # print(f"{a}:{a_value}", f"{b}:{b_value}", f"{c}:{c_value}", f"{d}:{d_value}")

    sl = Solution()
    links = sl.mergeTwoLists(get_linked_list([1, 2, 4]), get_linked_list([1, 3, 4]))
    check_result(links, [1, 1, 2, 3, 4, 4])

    links = sl.mergeTwoLists(get_linked_list([]), get_linked_list([]))
    check_result(links, [])

    links = sl.mergeTwoLists(get_linked_list([]), get_linked_list([0]))
    check_result(links, [0])

    links = sl.mergeTwoLists(get_linked_list([2]), get_linked_list([1]))
    check_result(links, [1, 2])

    links = sl.mergeTwoLists(get_linked_list([1, 2]), get_linked_list([1, 3, 4, 5, 6]))
    check_result(links, [1, 1, 2, 3, 4, 5, 6])
