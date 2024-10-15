"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。



示例 1：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
示例 2：

输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    def threeSumClosest0(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        nums = sorted(nums)
        res_sum = nums[0] + nums[1] + nums[-1]
        diff = _prev_diff = target - res_sum if target > res_sum else res_sum - target
        for i in range(lens - 1):
            first = nums[i]
            for j in range(i + 1, lens - 1):
                second = nums[j]
                prev_diff = _prev_diff
                for k in range(j + 1, lens):
                    curr_sum = first + second + nums[k]
                    curr_diff = target - curr_sum if target > curr_sum else curr_sum - target
                    if curr_diff < diff:
                        res_sum, diff = curr_sum, curr_diff
                    elif curr_diff > prev_diff:
                        break
                    prev_diff = curr_diff

        return res_sum

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        nums = sorted(nums)
        res_sum = nums[0] + nums[1] + nums[-1]
        diff = target - res_sum if target > res_sum else res_sum - target

        for i in range(lens - 1):
            first = nums[i]
            j, k = i + 1, lens - 1
            while j < k:
                curr_sum = first + nums[j] + nums[k]

                if target < curr_sum:
                    curr_diff = curr_sum - target
                    k -= 1
                elif target > curr_sum:
                    curr_diff = target - curr_sum
                    j += 1
                else:
                    return curr_sum

                if curr_diff < diff:
                    res_sum, diff = curr_sum, curr_diff

        return res_sum


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-2, -1, 0, 1, 4], 0), "正解：0")
    print(s.threeSumClosest([-4, -1, 1, 2], 1), "正解：2")
    print(s.threeSumClosest([-1, 0, 1, 2], 1), "正解：1")
    print(s.threeSumClosest([0, 0, 0, 0], 1), "正解：0")

    ls = [-981, -968, -959, -943, -942, -941, -882, -854, 2, 3, 4, 5]
    print(s.threeSumClosest(ls, -2805), "正解：-2805")
    print(s.threeSumClosest([-1000, -1000, -1000], 10000), "正解：-3000")
    "-981 -942 -882"
