"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。


示例 1：
输入：s = "aa", p = "a"
输出：false

示例 2:
输入：s = "aa", p = "a*"
输出：true

示例 3：
输入：s = "ab", p = ".*"
输出：true

提示：

1 <= s.length <= 20
1 <= p.length <= 20
s 只包含从 a-z 的小写字母。
p 只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """

        :param s:
        :param p:
        :return:
        """


if __name__ == '__main__':
    s1 = "aab"
    p1 = "c*a*b"

    s2 = "abc"
    p2 = "a.."

    s3 = "abc"
    p3 = "a.d"

    s4 = "abcd"
    p4 = "a."

    s5 = "abb"
    p5 = ".*"

    s6 = "abc"
    p6 = "a*.cc"

    s7 = "abb"
    p7 = ".*d"

    s8 = "a"
    p8 = "ab*"

    s9 = "a"
    p9 = "ab*c**"

    s0 = "aaaab"
    p0 = "a*aab"

    # print(Solution().isMatch(s1, p1), True, "\n")
    # print(Solution().isMatch(s2, p2), True, "\n")
    # print(Solution().isMatch(s3, p3), False, "\n")
    # print(Solution().isMatch(s4, p4), False, "\n")
    # print(Solution().isMatch(s5, p5), True, "\n")
    # print(Solution().isMatch(s6, p6), False, "\n")
    # print(Solution().isMatch(s7, p7), False, "\n")
    # print(Solution().isMatch(s8, p8), True, "\n")
    # print(Solution().isMatch(s9, p9), True, "\n")
    # print(Solution().isMatch(s0, p0), True, "\n")

    # 挑战失败
