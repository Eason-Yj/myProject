"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "{}([]){[]}"
输出：true

"""

from typing import List, Optional


class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for curr_s in s:
            if curr_s in ['(', '{', '[']:
                stack.append(curr_s)
            elif stack and d[curr_s] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    # print(f"{a}:{a_value}", f"{b}:{b_value}", f"{c}:{c_value}", f"{d}:{d_value}")

    sl = Solution()
    #
    print(sl.isValid("()"), "正解：True")
    print(sl.isValid("()[]{}"), "正解：True")
    print(sl.isValid("(]"), "正解：False")
    print(sl.isValid("([)]"), "正解：False")
    print(sl.isValid("{}([]){[]}"), "正解：True")
    print(sl.isValid("]"), "正解：False")
    print(sl.isValid("[([]])"), "正解：False")
