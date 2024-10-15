from typing import List
from typing import Optional
from typing import Union
from typing import Dict


class ListNode:
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next = next_val


def get_linked_list(lists: List[Union[str, int]]):
    if not ls:
        return None
    head = ListNode(lists[0])
    curr_node = head
    for val in lists[1:]:
        curr_node.next = ListNode(val)
        curr_node = curr_node.next
    return head


def check_linked_list(head: ListNode, lists: List[int]):
    current = head
    res_ls = []
    while current:
        res_ls.append(current.val)
        current = current.next
    print(res_ls, f"正解：{lists}")


class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        hair = ListNode(0, head)
        curr_node, prev = head, hair

        while curr_node:
            n += 1
            # if n < k:
            #     next_node = curr_node.next
            #     curr_node.next = prev
            #     prev = curr_node
            #     curr_node = next_node
            # else:
            #     n = 0
            #     pass
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        return hair


# ls = [1, 2, 3, 4]
# sl = Solution()
# check_linked_list(sl.reverseLinkedList(get_linked_list(ls)), ls)
#
# ls = []
# sl = Solution()
# check_linked_list(sl.reverseLinkedList(get_linked_list(ls)), ls)
#
# ls = [1, 2, 3, 4, 5, 6, 7, 8]
# sl = Solution()
# check_linked_list(sl.reverseLinkedList(get_linked_list(ls)), ls)
#


ls = [1, 2, 3, 4, 5, 6, 7, 8]
sl = Solution()
check_linked_list(sl.reverseKGroup(get_linked_list(ls), 2), ls)
