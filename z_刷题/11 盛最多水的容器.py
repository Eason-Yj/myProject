"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49

示例 2：
输入：height = [1,1]
输出：1
"""
from typing import List
import time


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        """

        :param height:
        :return:
        """

        lens = len(height)
        max_area = 0
        for l in range(lens - 1):
            height_l = height[l]
            if height_l * (lens - l - 1) < max_area:
                continue
            for r in range(l + 1, lens):
                wide = r - l
                height_r = height[r]
                h = min(height_l, height_r)
                area = h * wide
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea2(self, height: List[int]) -> int:
        """

        :param height:
        :return:
        """

        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            l_h, r_h = height[l], height[r]
            max_h = min(l_h, r_h)
            wide = r - l
            area = max_h * wide
            if area > max_area:
                max_area = area

            if l_h > r_h:
                r -= 1
            else:
                l += 1
        return max_area


if __name__ == '__main__':
    ls1 = [1, 2, 2, 2, 5, 4, 33, 3, 7, 1, 8, 6]

    ls2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 7, 9, 2, 1, 7, 1, 1, 12, 9,
           1, 1, 2, 1, 1, 1, 6, 2, 5, 4, 8, 3, 7, 9, 2, 1, 7, 1, 1, 12, 9, 1, 1, 2, 1, 1, 12, 9, 1, 1, 2, 1, 1, 19, 6,
           2, 5, 4, 8, 3, 7, 9, 2, 1, 7, 1, 1, 12, 9, 1, 1, 2, 1, 1, 12, 9, 1, 1, 2, 1, 1, 19, 6, 2, 5, 4, 8, 3, 7, 9]

    res1_1 = Solution().maxArea1(ls1)
    res1_2 = Solution().maxArea2(ls1)
    res2_1 = Solution().maxArea1(ls2)
    res2_2 = Solution().maxArea2(ls2)

    t1 = time.time()
    print(f"res1:{res1_1}")
    print(f"res1:{res1_2}")
    print(f"res2:{res2_1}")
    print(f"res2:{res2_2}")
    # 挑战失败

    # res1 = Solution().maxArea([1, 1, 1, 1, 1, 1])
    # print(res1)
    """
    max_l:0, max_r:10
    max_l:0, max_r:96
    res1:80===80
    res2:1824===1862
    3.814697265625e-06s

    max_l:1, max_r:11
    max_l:33, max_r:96
    res1:80===80
    res2:1197===1862

    max_l:0, max_r:10
    max_l:0, max_r:96
    res1:80===80
    res2:1824===1862
    """
