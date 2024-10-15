from typing import List, Optional


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """

        :param nums1:
        :param nums2:
        :return:
        """
        lens1, lens2 = len(nums1), len(nums2)
        if lens1 == 0:
            res_ls = nums2
            all_lens = lens2
        elif lens2 == 0:
            res_ls = nums1
            all_lens = lens1
        else:
            res_ls = []
            curr_i = curr_j = 0
            all_lens = lens1 + lens2

            for i in range(lens1):
                curr_i = i
                if curr_j >= lens2:
                    curr_i = i - 1
                    break
                for j in range(curr_j, lens2):
                    if nums1[i] <= nums2[j]:
                        res_ls.append(nums1[i])
                        # print("res_ls1", res_ls)
                        break
                    else:
                        curr_j = j + 1
                        res_ls.append(nums2[j])
                        # print("res_ls3", res_ls)

            if curr_j >= lens2:  # 当num2里元素取完但num1里面没取完时
                res_ls = res_ls + nums1[curr_i:]
            elif curr_j < lens2:  # 当num1里元素取完但num2里没取完时
                res_ls = res_ls + nums2[curr_j:]

        median_idx = all_lens // 2
        median_idx_r = all_lens % 2

        # print(res_ls)

        if median_idx_r != 0:
            return res_ls[median_idx]

        return (res_ls[median_idx] + res_ls[median_idx - 1]) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


if __name__ == '__main__':
    ls1 = [-31, 12]
    ls2 = [-1, 2, 2, 3, 4, 5, 6]

    ls1 = [2]
    ls2 = []

    ls1.sort()
    ls2.sort()

    print(ls1)
    print(ls2)
    print(Solution().findMedianSortedArrays(ls1, ls2))
