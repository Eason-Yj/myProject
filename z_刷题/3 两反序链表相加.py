# https://leetcode-cn.com/problems/add-two-numbers/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            curr.next = ListNode(total % 10)

            curr = curr.next
            carry = total // 10

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: curr.next = ListNode(carry)
        return dummy.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]


def get_lb(l):
    """
    获取链表
    :param l:
    :return:
    """
    val = l.pop(0)
    if len(l) == 0:
        return ListNode(val=val)
    else:
        return ListNode(val=val, next=get_lb(l))


res = get_lb(l1)

# Solution().addTwoNumbers(l1=lst1, l2=lst2)
