import time
import threading
import numpy as np
from concurrent.futures import ThreadPoolExecutor


# 多线程方法实现：
def printExp(row, row2, idx):
    idx += 1
    print(idx)
    time.sleep(1)


# 简单方法
for i in range(1, 3):
    t = threading.Thread(target=printExp, args=(i,))
    t.start()


def threadPool():
    # 可控制最大线程数方法
    data = np.random.randint(1, 1000, size=(100, 3))

    with ThreadPoolExecutor(max_workers=5) as executor:
        idx = 0
        for row in data:
            executor.submit(printExp, row=row, row2=100, idx=idx)
            print(2)


threadPool()
