"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。


提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        固定前面i，j值后，只需要判断第三个k值是否和上一个k值相同，来判断是否重复
        先将数组排序，如[0,1,2,2]，k=2，上一个k=2，则跳过
        :param nums:
        :return:
        """
        lens = len(nums)
        res = []
        nums = sorted(nums)
        prev_k = None
        for i in range(lens - 2):
            for j in range(i + 1, lens - 1):
                for k in range(j + 1, lens):
                    if prev_k != nums[k] and nums[i] + nums[j] + nums[k] == 0:
                        ls = [nums[i], nums[j], nums[k]]
                        prev_k = nums[k]
                        res.append(ls)
        # print("res_idx: ", res_idx)
        return res

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        """
        sum = nums[i] + nums[j] + nums[k]，固定i值后，
        当 sum<0 时，sum=0时的j值一定在当前j的右边，即j=j+1；
        当 sum>0 时，sum=0时的k值一定在当前k的左边，即k=k+1；
        :param nums:
        :return: [-1, 0, 1, 2, -1, -4]
        :return: [-4, -3, -2, -1, -1 , 0, 1, 2, 3] 正解 [-4 1 3] [-3 0 3] [-3 1 2] [-2 0 2] [-2 1 1] [-1 0 1]
        """
        lens = len(nums)

        res = []
        nums = sorted(nums)
        for i in range(lens - 1):
            left, right = i + 1, lens - 1
            first = nums[i]

            if i > 0 and first == nums[i - 1]:
                continue

            while left < right:
                second, third = nums[left], nums[right]
                if left > i + 1 and second == nums[left - 1]:
                    left += 1
                    continue
                _sum = first + second + third
                if _sum == 0:
                    res.append([first, second, third])
                    left += 1
                    right -= 1
                elif _sum > 0:
                    right -= 1
                else:
                    left += 1

        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        lens = len(nums)
        res = []
        nums = sorted(nums)
        for i in range(lens - 1):
            first = nums[i]
            k = lens - 1

            if i > 0 and first == nums[i - 1]:
                continue

            for j in range(i + 1, lens - 1):
                second, third = nums[j], nums[k]

                if j > i + 1 and second == nums[j - 1]:
                    continue
                while j < k and first + second + third > 0:
                    k -= 1
                    third = nums[k]

                if j == k:
                    break
                elif first + second + third == 0:
                    res.append([first, second, third])
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.threeSum2([-4, -3, -2, -1, -1, 0, 1, 2, 3]),
          "正解：[[-4 1 3] [-3 0 3] [-3 1 2] [-2 -1 3] [-2 0 2] [-1 -1 2] [-1 0 1]]")
    print(S.threeSum2([0, 1, 1]), "正解：", [])
    print(S.threeSum2([0, 0, 0]), "正解：", [0, 0, 0])
    print(S.threeSum2([-1, 0, 1, 2, -1, -4]), "正解：", [[-1, -1, 2], [-1, 0, 1]])
    print(S.threeSum2([-4, -1, -1, 0, 1, 2]), "正解：", [[-1, -1, 2], [-1, 0, 1]])
    print(S.threeSum2([-4, 2, 2]), "正解：", [[-4, 2, 2]])
    print(S.threeSum2([0, -1, 0, 1, 2]), "正解：", [[-1, 0, 1]])
    print(S.threeSum2([-4, 1, 1, 3]), "正解：", [[-4, 1, 3]])
    print(S.threeSum2([-1, -1, 0, 1]), "正解：", [[-1, 0, 1]])
    print(S.threeSum2([-1, -1, 0, 2]), "正解：", [[-1, -1, 2]])
    print(S.threeSum2([0, 0, 0, 1]), "正解：", [[0, 0, 0]])
