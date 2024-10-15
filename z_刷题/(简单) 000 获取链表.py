from typing import List, Optional, Union


class ListNodeBase:
    def __init__(self, value, next_node):
        """

        :param value:
        :param next_node:
        """
        self.val = value
        self.next = next_node


class ListNode(ListNodeBase):

    def __init__(self, value: int = 1, next_node: ListNodeBase = None):
        """
        链表的节点
        :param value:
        :param next_node:
        """
        super().__init__(value, next_node)
        self.val = value
        self.next = next_node


def get_linked_list_v1(array: Union[list, set], method: int = 1) -> Optional[ListNode]:
    """
    方法一：递归方式 每轮从列表中取出第一个元素作为本轮节点的val值
    :param method:
    :param array:
    :return:
    """

    def run(ls: Union[list, set]) -> ListNode:

        if len(ls) == 1:
            return ListNode(value=ls[0])
        else:
            val = ls.pop(0)
            return ListNode(value=val, next_node=run(ls))

    if not array:
        return None

    return run(array)


def get_linked_list_v2(ls: Union[list, set]):
    """
    方法二：递归方式 每轮从列表中对应索引位取出元素作为本轮节点的val值
    :param ls:
    :return:
    """
    lens = len(ls)
    if lens == 0:
        return None

    def run(_ls: Union[list, set], idx=0) -> ListNode:
        if idx >= lens - 1:
            return ListNode(value=ls[idx])
        else:
            val = ls[idx]
            idx += 1
            return ListNode(value=val, next_node=run(ls, idx))

    return run(ls)


def get_linked_list_v3(ls: Union[list, set]):
    if not ls:
        return None

    head = ListNode(ls[0])
    curr_node = head
    for val in ls[1:]:
        curr_node.next = ListNode(val)
        curr_node = curr_node.next
    return head


def check_linked_list(lk: ListNode, target: list = None):
    res_ls = []
    while lk:
        res_ls.append(lk.val)
        lk = lk.next

    print(f"{res_ls}; 正解：{target}")


if __name__ == '__main__':
    exp_ls = [1, 2, 3, 4, 5]
    check_linked_list(get_linked_list_v1(exp_ls.copy()), exp_ls)
    check_linked_list(get_linked_list_v2(exp_ls.copy()), exp_ls)
    check_linked_list(get_linked_list_v3(exp_ls.copy()), exp_ls)

    exp_ls = []
    check_linked_list(get_linked_list_v1(exp_ls.copy()), exp_ls)
    check_linked_list(get_linked_list_v2(exp_ls.copy()), exp_ls)
    check_linked_list(get_linked_list_v3(exp_ls.copy()), exp_ls)
