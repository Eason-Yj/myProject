def root_two_square(n: int, target: int = 2):
    """
    遍历搜索 根号target的解
    :param target:
    :param n: n需要小于16
    :return:
    """
    num = 1.0
    curr_num = num
    prev_square = num
    float_digit_num = 1
    _num = 0

    while True:
        _num += 1
        square = curr_num ** 2
        if square < target:
            if prev_square < target:
                curr_digit = 1
            else:
                float_digit_num += 1
                curr_digit = 0.1
        elif square > target:
            if prev_square < target:
                curr_digit = -1
            else:
                float_digit_num += 1
                curr_digit = -0.1
        else:
            return curr_num

        num = float(curr_num)
        prev_square = float(num) ** 2
        curr_num += curr_digit / (10 ** float_digit_num)
        # print("num:", num, curr_num, "curr_digit:", curr_digit, float_digit_num)

        if float_digit_num >= n:
            print(f"迭代次数:{_num}")
            break

    return num


n = 16
print(root_two_square(n), "正解：1.4142135623730951")
print(1.41421356237309503 ** 2)

print(2 / 128)