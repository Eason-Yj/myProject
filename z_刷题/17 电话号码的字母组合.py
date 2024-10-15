"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]


提示：
0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ls = d[digits[0]]
        for n in digits[1:]:
            new_ls = []
            for s in ls:
                new_ls.extend([s + _s for _s in d[n]])
            ls = new_ls
        return ls

    def letterCombinations2(self, digits: str) -> List[str]:
        lens = len(digits)
        if lens == 0:
            return []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ls = []
        curr_ls = []

        def process(index):
            print(index, lens, "curr_ls", curr_ls)
            if index < lens:
                num = digits[index]
                for s in d[num]:
                    curr_ls.append(s)
                    process(index + 1)
                    curr_ls.pop()
            else:
                ls.append(curr_ls.copy())

        process(0)

        return ls


if __name__ == '__main__':
    sl = Solution()
    print(sl.letterCombinations2("234"), "正解：", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
