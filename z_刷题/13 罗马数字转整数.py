"""
七个不同的符号代表罗马数字，其值如下：

符号	值
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。
如果该值以 4 或 9 开头，使用 减法形式，表示从以下符号中减去一个符号，例如 4 是 5 (V) 减 1 (I): IV ，9 是 10 (X) 减 1 (I)：IX。仅使用以下减法形式：4 (IV)，9 (IX)，40 (XL)，90 (XC)，400 (CD) 和 900 (CM)。
只有 10 的次方（I, X, C, M）最多可以连续附加 3 次以代表 10 的倍数。你不能多次附加 5 (V)，50 (L) 或 500 (D)。如果需要将符号附加4次，请使用 减法形式。
给定一个整数，将其转换为罗马数字。

示例 1：
输入：num = 3749
输出： "MMMDCCXLIX"
解释：
    3000 = MMM 由于 1000 (M) + 1000 (M) + 1000 (M)
     700 = DCC 由于 500 (D) + 100 (C) + 100 (C)
      40 = XL 由于 50 (L) 减 10 (X)
       9 = IX 由于 10 (X) 减 1 (I)
    注意：49 不是 50 (L) 减 1 (I) 因为转换是基于小数位

示例 2：
输入：num = 58
输出："LVIII"
解释：
    50 = L
     8 = VIII

示例 3：
输入：num = 1994
输出："MCMXCIV"
解释：
1000 = M
 900 = CM
  90 = XC
   4 = IV




"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        依次从罗马数字和值得对应表中取出一个罗马数字，判断该罗马数字是否为字符串中的头一个或头两个字符(对应4，9，40...等情况)，若是则累加到结果值
        :param s:
        :return:
        """
        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        res = 0
        for n, roman_n in VALUE_SYMBOLS:
            start_idx = len(roman_n)
            start_s = s[:start_idx]
            while start_s == roman_n:
                s = s[start_idx:]
                start_s = s[:start_idx]
                res += n

        return res

    def romanToInt2(self, s: str) -> int:
        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        res = 0
        for n, roman_n in VALUE_SYMBOLS:
            start_idx = len(roman_n)
            while s.startswith(roman_n):
                s = s[start_idx:]
                res += n

        return res

    def romanToInt3(self, s: str) -> int:
        """
        依次从罗马数字中取出一个字符，并获取其对应的数值，判断该字符的值是否比下一个字符的值大，若大则累加，若小则累减(对应4，9，40...情况)
        :param s:
        :return:
        """
        SYMBOL_VALUES = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        res = 0
        lens = len(s)
        for idx, roman_s in enumerate(s):
            val = SYMBOL_VALUES[roman_s]

            if idx < lens - 1 and val < SYMBOL_VALUES[s[idx + 1]]:
                res -= val
            else:
                res += val

        return res


if __name__ == '__main__':
    print(Solution().romanToInt2("MMMDCCXLIX"), 3749)
    print(Solution().romanToInt2("IX"), 9)
    print(Solution().romanToInt2("LVIII"), 58)
    print(Solution().romanToInt2("MCMXCIV"), 1994)
    print(Solution().romanToInt2("MMMMMCMXCIX"), 5999)
