"""
题目描述：

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"

"""


class Solution:

    def convert(self, s: str, numRows: int) -> str:
        """
        结题思路：纯数学方式
        第一行和最后一行的字符位置满足：n * 2 * (numRows-1) + num_row; 其中n为轮数(间隔数),num_row为当前字符所在行数
        其他行的字符位置满足：n * 2 * (numRows-1) + num_row 和 (n+1) * 2 * (numRows-1) - (num_row-2)
        :param s:
        :param numRows:
        :return:
        """
        if numRows == 1:  # 只有1行时就不用递增又递减了
            return s

        # res_dict = {_i: "" for _i in range(1, numRows + 1)}
        res = ""
        lens = len(s)
        interval = 2 * (numRows - 1)  # 间隔
        interval_num = lens // interval + 1  # 总的间隔数

        for num_row in range(1, numRows + 1):
            for i in range(interval_num):
                if num_row in (1, numRows):
                    s_id = i * interval + num_row
                    if s_id > lens:
                        continue
                    # res_dict[num_row] += s[s_id - 1]  # 因为索引从0开始，需要-1
                    res += s[s_id - 1]
                else:
                    s_id = i * interval + num_row
                    if s_id > lens:
                        continue
                    # res_dict[num_row] += s[s_id - 1] # 因为索引从0开始，需要-1
                    res += s[s_id - 1]
                    s_id = (i + 1) * interval - (num_row - 2)
                    if s_id > lens:
                        continue
                    # res_dict[num_row] += s[s_id - 1] # 因为索引从0开始，需要-1
                    res += s[s_id - 1]
        # print(res)
        return res

    def convert2(self, s: str, numRows: int) -> str:
        """
        思路：随着字符的索引增加，每个元素所处的行数先从 第1行 递增到 第numRows行 再递减到 第1行，如此反复直到最后一个元素
        :param s:
        :param numRows:
        :return:
        """
        lens = len(s)
        curr_n = 1
        res_dict = {_i: "" for _i in range(1, numRows + 1)}

        if numRows == 1:  # 只有1行时就不用递增又递减了
            return s
        else:
            is_ascending = True

        for i in range(lens):
            res_dict[curr_n] += s[i]

            if curr_n == numRows:
                is_ascending = False
            elif curr_n == 1:
                is_ascending = True
            if is_ascending:
                curr_n += 1
            else:
                curr_n -= 1

        res = "".join(list(res_dict.values()))

        # print(res_dict)
        # print(res)
        return res


if __name__ == '__main__':
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    res1 = "PAHNAPLSIIGYIR"

    s2 = "PAYPALISHIRING"
    numRows2 = 4
    res2 = "PINALSIGYAHRPI"

    Solution().convert(s2, numRows2)
