# ### 10进制转换其他进制
class Solution:
    def convertToBase7(self, num: int) -> str:
        divisor = abs(num)
        result = str()
        while True:
            if divisor < 7:
                result = str(divisor) + result
                break
            remainder = divisor % 7
            divisor = divisor // 7
            result = str(remainder) + result
        if num < 0:
            result = "-%s" % result

        return result


class Solution2:
    def convertToBase7(self, num: int) -> str:
        def tobase7(num):
            if num < 7:
                return str(num)
            divisor = num // 7
            remainder = num % 7
            res = tobase7(divisor) + str(remainder)
            return res

        num_ = abs(num)
        res = tobase7(num_)
        if num < 0:
            res = "-%s" % res
        return res


class Solution3:
    def convertToBase7(self, num: int, base=2) -> str:
        def toBase(num):
            if num < base:
                return str(num)
            remainder = num % base
            divisor = num // base
            res = toBase(divisor) + str(remainder)

            return res

        result = toBase(abs(num))
        if num < 0:
            return "-" + result
        return result


test = Solution().convertToBase7(num=101)
print("test", test)
test2 = Solution2().convertToBase7(num=101)
print("test2", test2)
test3 = Solution3().convertToBase7(num=101, base=7)
print("test3", test3)
