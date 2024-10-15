"""
从一个数组中找出和(积)等于目标值的两个数，并返回这两个数的索引
"""
from typing import List


# 暴利搜索
class Solution1:
    "时间复杂度为O^2"
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# print(Solution1().twoSum(nums=[2, 7, 2, 11, 15], target=17))


# 构建hash表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, i_val in enumerate(nums):
            if target - i_val in hashtable:
                return [i, hashtable[target - i_val]]
            else:
                hashtable[i_val] = i
        return []


print(Solution().twoSum(nums=[2, 7, 2, 11, 15], target=17))
print(Solution().twoSum(nums=[0, 0], target=0))
print(Solution().twoSum(nums=[2, 7, 2, 11, 15], target=4))
print(Solution().twoSum(nums=[3, 7, 2, 11, 15], target=13))
print(Solution().twoSum(nums=[2, 7, 3, 11, 15], target=10))
