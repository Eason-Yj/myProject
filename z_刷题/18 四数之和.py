"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

提示：
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lens = len(nums)
        res_ls = []
        if lens < 4:
            return res_ls
        nums = sorted(nums)
        for a in range(lens - 3):
            a_value = nums[a]
            if a_value + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            elif a > 0 and nums[a - 1] == a_value:
                continue
            for b in range(a + 1, lens - 2):
                b_value = nums[b]
                sum_ab = a_value + b_value
                if sum_ab + nums[b + 1] + nums[b + 2] > target:
                    break
                elif b > a + 1 and nums[b - 1] == b_value:
                    continue
                c, d = b + 1, lens - 1
                while c < d:
                    c_value, d_value = nums[c], nums[d]
                    _sum = sum_ab + c_value + d_value
                    if c > b + 1 and nums[c - 1] == c_value:
                        c += 1
                        continue
                    if _sum == target:
                        res_ls.append([a_value, b_value, c_value, d_value])
                        c, d = c + 1, d - 1
                    elif _sum > target:
                        d -= 1
                    else:
                        c += 1
        return res_ls


if __name__ == '__main__':
    # print(f"{a}:{a_value}", f"{b}:{b_value}", f"{c}:{c_value}", f"{d}:{d_value}")

    sl = Solution()
    print(sl.fourSum([1, 0, -1, 0, -2, 2], 0), "正解：", [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    print(sl.fourSum([2, 2, 2, 2, 2], 8), "正解：", [[2, 2, 2, 2, 2]])
    print(sl.fourSum([-2, -1, -1, 1, 1, 2, 2], 0), "正解：", [[-2, -1, 1, 2], [-1, -1, 1, 1]])
    # print(sl.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11), "正解：", [[-5, -4, -3, 1]])
    print(sl.fourSum([-5, -4, -3, -2, 1, 3, 3, 5], -11), "正解：", [[-5, -4, -3, 1]])
