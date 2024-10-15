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
    def intToRoman(self, num: int) -> str:
        str_num = str(num)
        digit = len(str_num)  # 数位
        num_map_1 = {1: "I", 2: "X", 3: "C", 4: "M"}
        num_map_5 = {1: "V", 2: "L", 3: "D"}
        res = ""

        for curr_num in str_num:
            curr_num = int(curr_num)

            if curr_num == 4:
                res += num_map_1[digit] + num_map_5[digit]
            elif curr_num == 9:
                res += num_map_1[digit] + num_map_1[digit + 1]
            elif curr_num < 4:
                res += num_map_1[digit] * curr_num
            else:
                if curr_num == 5 and digit == 4:
                    res += "M" * 5
                else:
                    count = curr_num - 5
                    res += num_map_5[digit] + num_map_1[digit] * count
            digit -= 1
        return res

    def intToRoman2(self, num: int) -> str:
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
        res = ""
        for n, roman_n in VALUE_SYMBOLS:
            while num >= n:
                num -= n
                res += roman_n

        return res


if __name__ == '__main__':
    print(Solution().intToRoman(3749), "MMMDCCXLIX")
    print(Solution().intToRoman2(3749), "MMMDCCXLIX")
    print(Solution().intToRoman(9), "IX")
    print(Solution().intToRoman2(9), "IX")
    print(Solution().intToRoman(58), "LVIII")
    print(Solution().intToRoman2(58), "LVIII")
    print(Solution().intToRoman(1994), "MCMXCIV")
    print(Solution().intToRoman2(1994), "MCMXCIV")
    print(Solution().intToRoman(5999), "MMMMMCMXCIX")
    print(Solution().intToRoman2(5999), "MMMMMCMXCIX")
