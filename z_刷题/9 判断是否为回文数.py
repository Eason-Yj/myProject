"""
回文数

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数
是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。


示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。


提示：

-231 <= x <= 231 - 1
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        思路：转换为字符串判断
        :param x:
        :return:
        """

        s_x = str(x)
        if s_x == s_x[::-1]:
            return True
        else:
            return False

    def isPalindrome2(self, x: int) -> bool:
        """
        思路：转换为字符串判断
        :param x:
        :return:
        """
        if 0 <= x < 10:
            return True
        elif x < 0 or x % 10 == 0:
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10
            if revertedNumber == x or x // 10 == revertedNumber:
                return True

        return False


if __name__ == '__main__':
    x1 = 0
    x2 = 2
    x3 = 10
    x4 = 11
    x5 = 101
    x6 = 101234

    print(Solution().isPalindrome2(x1))
    print(Solution().isPalindrome2(x2))
    print(Solution().isPalindrome2(x3))
    print(Solution().isPalindrome2(x4))
    print(Solution().isPalindrome2(x5))
    print(Solution().isPalindrome2(x6))
