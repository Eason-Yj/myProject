"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

"""

from typing import List, Optional, Union


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
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        每轮遍历每个链表的当前节点的值，将值最小的那个a链表的当前节点添加到新链表b中,同时a链表的当前节点变为下一个节点
        测试案例约3000ms
        :param lists:
        :return:
        """

        if not lists:
            return None

        new_lik = ListNode()
        curr_node = new_lik
        num_list = len(lists)

        while any(lists):
            curr_min_lik_idx = None
            for i in range(num_list):
                if lists[i] is None:
                    continue
                elif (curr_min_lik_idx is None) or (lists[i].val <= lists[curr_min_lik_idx].val):
                    curr_min_lik_idx = i

            curr_node.next = lists[curr_min_lik_idx]
            lists[curr_min_lik_idx] = lists[curr_min_lik_idx].next
            curr_node = curr_node.next

        return new_lik.next

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        和上述方法原理一致，使用递归实现
        :param lists:
        :return:
        """
        if not lists:
            return None
        if any(lists):
            curr_min_idx = None
            for i, linked in enumerate(lists):
                if linked is None:
                    continue
                elif curr_min_idx is None or linked.val < lists[curr_min_idx].val:
                    curr_min_idx = i
            curr_min = lists[curr_min_idx].val
            lists[curr_min_idx] = lists[curr_min_idx].next
            return ListNode(curr_min, self.mergeKLists2(lists))
        else:
            return None

    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        依次合并，第一个链表先和第二个链表合并，合并的结果再和第二个链表合并，直到合并完所有链表，递归实现
        :param lists:
        :return:
        """
        if not lists:
            return None

        def merge2Lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if list1 is None:
                return list2
            elif list2 is None:
                return list1
            elif list1.val <= list2.val:
                return ListNode(list1.val, merge2Lists(list1.next, list2))
            else:
                return ListNode(list2.val, merge2Lists(list1, list2.next))

        base_lik = lists[0]
        for _lik in lists[1:]:
            base_lik = merge2Lists(base_lik, _lik)
        return base_lik

    def mergeKLists4(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        依次合并，第一个链表先和第二个链表合并，合并的结果再和第二个链表合并，直到合并完所有链表，遍历实现
        测试案例约1500ms
        :param lists:
        :return:
        """
        if not lists:
            return None

        def merge2Lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            return_lik = ListNode()
            curr_lik = return_lik
            while list1 and list2:
                if list1.val <= list2.val:
                    curr_lik.next = list1
                    list1 = list1.next
                else:
                    curr_lik.next = list2
                    list2 = list2.next
                curr_lik = curr_lik.next
            curr_lik.next = list1 if list1 else list2
            return return_lik.next

        base_lik = lists[0]
        for _lik in lists[1:]:
            base_lik = merge2Lists(base_lik, _lik)
        return base_lik

    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """

        :param list1:
        :param list2:
        :return:
        """
        return_lik = ListNode()
        curr_lik = return_lik
        while list1 and list2:
            if list1.val <= list2.val:
                curr_lik.next = list1
                list1 = list1.next
            else:
                curr_lik.next = list2
                list2 = list2.next
            curr_lik = curr_lik.next
        curr_lik.next = list1 if list1 else list2
        return return_lik.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        两两合并，每两个链表进行合并生成 K/2或(K/2+1) 个新的链表，再两两合并，直到生成一个链表为止。
        测试案例约51ms
        :param lists:
        :return:
        """
        if not lists:
            return None

        lens = len(lists)

        if lens <= 1:
            return lists[0]
        else:
            j = lens - 1
            new_ls = []
            for i in range(lens):
                if i > j:
                    break
                elif i == j:
                    new_ls.append(lists[i])
                else:
                    new_ls.append(self.merge2Lists(lists[i], lists[j]))
                    j -= 1
            return self.mergeKLists(new_ls)


if __name__ == '__main__':
    sl = Solution()
    lst = [[1], [1, 4, 5], [2, 3, 3]]
    lik = get_links_list(lst)
    check_links_list(sl.mergeKLists(lik), [1, 1, 2, 3, 3, 4, 5])

    lst = [[], [1, 1, 5], [2, 3, 3]]
    lik = get_links_list(lst)
    check_links_list(sl.mergeKLists(lik), [1, 1, 2, 3, 3, 5])

    lst = [[], [], []]
    lik = get_links_list(lst)
    check_links_list(sl.mergeKLists(lik), [])

    lst = []
    lik = get_links_list(lst)
    check_links_list(sl.mergeKLists(lik), [])

    lst = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lik = get_links_list(lst)
    check_links_list(sl.mergeKLists(lik), [1, 1, 2, 3, 4, 4, 5, 6])
