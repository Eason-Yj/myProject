# https://leetcode-cn.com/problems/add-two-numbers/
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, _val=0, _next=None):
        self.val = _val
        self.next = _next


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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_val = 0
        res_ln = curr_ln = ListNode()

        while l1 or l2 or add_val != 0:
            _val1 = l1.val if l1 else 0
            _val2 = l2.val if l2 else 0

            sum_val = _val1 + _val2 + add_val
            add_val = sum_val // 10

            curr_ln.next = ListNode(sum_val % 10)

            curr_ln = curr_ln.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if res_ln.next:
            res_ln = res_ln.next

        return res_ln


if __name__ == '__main__':
    _l1 = [9, 9, 9, 9]
    _l2 = [9, 9, 9, 9, 9, 9, 9]

    lst1 = get_linked_list(_l1)
    lst2 = get_linked_list(_l2)

    res = Solution().addTwoNumbers(lst1, lst2)

    res_ls = []
    while res:
        res_ls.append(res.val)
        res = res.next
    print(res_ls)
