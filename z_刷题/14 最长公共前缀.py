"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 1
        prev_prefix = ""
        prefix = strs[0][0]
        is_true = True
        while is_true:
            for s in strs[1:]:
                if prefix != s[:idx]:
                    is_true = False
                    break
                else:
                    prev_prefix = prefix
                    idx += 1
                    prefix = s[:idx]
        return prev_prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        prefix = ""
        is_break = False
        for idx, curr_s in enumerate(strs[0]):
            for s in strs[1:]:
                if idx >= len(s) or curr_s != s[idx]:
                    is_break = True
                    break
            if is_break:
                break
            else:
                prefix += curr_s

        return prefix

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        """
        原理和方法二相同
        :param strs:
        :return:
        """
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix2(["flower", "flow", "flight"]), "fl")
    print(Solution().longestCommonPrefix2(["dog", "racecar", "car"]), "")
    print(Solution().longestCommonPrefix2(["dog", "d", "damg"]), "d")
    print(Solution().longestCommonPrefix2(["dog", "racecar", "car"]), "")
