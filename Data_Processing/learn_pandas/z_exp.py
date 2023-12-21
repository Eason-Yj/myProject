import time
import numba as nb

num = 500000

time1 = time.time()


@nb.njit(parallel=True)
def f_circulate1(num):
    res_list = []
    res = 0
    for i in nb.prange(num):
        if i == 0 or i == 1:
            res_list.append(1)
        else:
            res = res_list[i - 1] + res_list[i - 2]
            res_list.append(res)
    return res_list


f_circulate1(num)
time2 = time.time()
print(f"time1: {round(time2 - time1, 6)}")
# ==========================================================
time3 = time.time()


@nb.njit
def f_circulate(num):
    res_list = []
    res = 0
    for i in range(num):
        if i == 0 or i == 1:
            res_list.append(1)
        else:
            res = res_list[i - 1] + res_list[i - 2]
            res_list.append(res)
    return res_list


f_circulate(num)
time4 = time.time()
print(f"time2: {round(time4 - time3, 6)}")
