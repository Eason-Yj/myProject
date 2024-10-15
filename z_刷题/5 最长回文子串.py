class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        :param s:
        :return:
        """
        lens = len(s)
        if lens < 2:
            return s

        max_s = ""

        for i in range(lens):
            for j in range(i, lens):
                curr_s = s[i:j + 1]
                if curr_s == curr_s[::-1]:
                    max_s = curr_s if len(curr_s) > len(max_s) else max_s
        print(max_s)
        print(len(max_s))
        return max_s

    def longestPalindrome2(self, s: str) -> str:
        """

        :param s:
        :return:
        """
        lens = len(s)
        max_lens = 0
        max_s = ""

        if lens < 2:
            return s
        for i in range(lens):
            # 情况一
            left, right = i, i
            while left >= 0 and right < lens and s[left] == s[right]:
                left -= 1
                right += 1
            curr_s1 = s[left + 1:right]
            curr_s1_lens = len(curr_s1)
            max_lens, max_s = (curr_s1_lens, curr_s1) if curr_s1_lens > max_lens else (max_lens, max_s)

            # 情况二
            left, right = i, i + 1
            while left >= 0 and right < lens and s[left] == s[right]:
                left -= 1
                right += 1
            curr_s2 = s[left + 1:right]
            curr_s2_lens = len(curr_s2)
            max_lens, max_s = (curr_s2_lens, curr_s2) if curr_s2_lens > max_lens else (max_lens, max_s)

        # print(max_s)
        # print(max_lens)
        return max_s


if __name__ == '__main__':
    _s = "acbabcde"
    Solution().longestPalindrome(_s)
    Solution().longestPalindrome2(_s)
