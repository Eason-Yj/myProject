"""
质数
"""
import math
import time


class Prime():
    """
    质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
    """

    def __init__(self, start_num=2, end_num=3):  # type:(int, int)->None
        self.__start_num = start_num
        self.__end_num = end_num
        self.prime_list = []
        self.composite_list = []
        self.factor_list = []

    def isPrime(self, num):
        """
        判断某数是否为质数,不是则返回所有的因子
        :param num:
        :return:
        """
        factor_list = []
        min_factor = 2
        max_factor = num // 2

        for i in range(min_factor, max_factor + 1):
            if num % i == 0:
                factor_list.append(i)
        self.factor_list = factor_list

        if len(factor_list) != 0:
            return False
        else:
            return True

    def get_prime_list(self):
        """
        获取一个数值范围内的所有
        Returns
        -------

        """
        prime_list = []
        if self.composite_list:
            prime_list = list(range(self.__start_num, self.__end_num + 1))
            for num in self.composite_list:
                prime_list.remove(num)
        else:
            for num in range(self.__start_num, self.__end_num + 1):
                if self.isPrime(num):
                    prime_list.append(num)

        self.prime_list = prime_list
        return prime_list

    def get_composite_list(self):
        """
        获取一个数值范围内的所有合数
        Returns
        -------

        """
        composite_list = []
        if self.prime_list:
            composite_list = list(range(self.__start_num, self.__end_num + 1))
            for num in self.prime_list:
                composite_list.remove(num)
        else:
            for num in range(self.__start_num, self.__end_num + 1):
                print(num, self.isPrime(num))
                if not self.isPrime(num):
                    composite_list.append(num)

        self.composite_list = composite_list
        return composite_list

    def Eratosthenes(self, end_num):
        """
        埃拉托斯特尼筛法
        把不大于 sqrt(n) 的所有素数的倍数剔除，剩下的就是n以内的所有素数
        :param num:
        :return:
        """
        all_lst = list(range(2, end_num + 1))

        for i in range(2, int(math.sqrt(end_num)) + 1):
            if self.isPrime(i):
                multiple = i
                while True:
                    multiple += i
                    if multiple <= end_num:
                        if multiple in all_lst:
                            all_lst.remove(multiple)
                    else:
                        break
        return all_lst


if __name__ == '__main__':
    time1 = time.time()
    prime = Prime(end_num=10000)
    prime.get_prime_list()
    print(prime.prime_list)
    time2 = time.time()
    print(prime.Eratosthenes(10000))
    time3 = time.time()

    print(time2 - time1)
    print(time3 - time2)
