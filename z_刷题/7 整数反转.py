"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0


提示：

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        """

        :param x:
        :return:
        """
        c = 1
        if x < 0:
            s_x = str(-x)
            c = -1
        else:
            s_x = str(x)
        res = int(s_x[::-1]) * c
        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        else:
            return 0

    def reverse2(self, x: int) -> int:
        """

        :param x:
        :return:
        """
        c = 1
        if x < 0:
            x = -x
            c = -1

        new_x = 0
        while x >= 1:
            curr = x % 10
            x = x // 10
            new_x = new_x * 10 + curr

        new_x = new_x * c
        if -2 ** 31 <= new_x <= 2 ** 31 - 1:
            return new_x
        else:
            return 0


if __name__ == '__main__':
    x = -123

    print(Solution().reverse2(x))
