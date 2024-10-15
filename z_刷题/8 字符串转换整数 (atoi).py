"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。

函数 myAtoi(string s) 的算法如下：

空格：读入字符串并丢弃无用的前导空格（" "）
符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
返回整数作为最终结果。

示例 1：
输入：s = "42"
输出：42

示例 2：
输入：s = " -042"
输出：-42

示例 3：
输入：s = "1337c0d3"
输出：1337

示例 4：
输入：s = "0-1"
输出：0

示例 5：
输入：s = "words and 987"
输出：0


提示：
0 <= s.length <= 200
s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成
"""


class Solution:

    def myAtoi(self, s: str) -> int:
        """

        :param s:
        :return:
        """

        new_x = ""
        c = 1
        is_start = True

        for i in s:
            if i.isdigit():
                new_x = new_x + i
                is_start = False
            elif i == "-" and is_start:
                c = -1
                is_start = False
            elif i == "+" and is_start:
                is_start = False
            elif i.isspace() and is_start:
                continue
            else:
                break

        new_x = int(float(new_x) * c) if new_x else 0
        if new_x < -2 ** 31:
            new_x = -2 ** 31
        elif new_x > 2 ** 31 - 1:
            new_x = 2 ** 31 - 1
        return new_x


if __name__ == '__main__':
    s1 = " -042"
    s2 = "1-2"
    s3 = "words and 987"
    s4 = "+-1337c0d3"
    s5 = "+3.1415"
    s6 = "-+12"
    s7 = "   +0 123"

    print(Solution().myAtoi(s1))
    print(Solution().myAtoi(s2))
    print(Solution().myAtoi(s3))
    print(Solution().myAtoi(s4))
    print(Solution().myAtoi(s5))
    print(Solution().myAtoi(s6))
    print(Solution().myAtoi(s7))
