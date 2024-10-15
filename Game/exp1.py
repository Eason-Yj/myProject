import time

import numpy as np


def main():
    width = 15
    height = 15
    life = np.random.choice(["-", "+"], size=(width, height))
    num = 0
    while True:
        num += 1
        print(f"第{num}周期".center(50, "*"))
        num_life = np.empty((width, height), dtype=str)
        for i in range(width):
            x_start, x_end = i - 1, i + 2
            if i == 0:
                x_start = 0
            elif i == width - 1:
                x_end = width
            for j in range(height):
                y_start, y_end = j - 1, j + 2
                if j == 0:
                    y_start = 0
                elif j == height - 1:
                    y_end = height

                unique_count = np.unique(life[x_start:x_end, y_start:y_end], return_counts=True)[1]
                print(life[x_start:x_end, y_start:y_end])
                if len(unique_count) == 3:
                    count_live = unique_count[0] + unique_count[2]
                else:
                    count_live = unique_count[0]
                print(f"count_live:{count_live}")
                if life[i][j] in ["+", "="]:
                    count_live -= 1
                    if count_live < 2 or count_live > 3:
                        num_life[i][j] = "-"
                    else:
                        num_life[i][j] = "="
                else:
                    if count_live == 3:
                        num_life[i][j] = "+"
                    else:
                        num_life[i][j] = life[i][j]
                life = num_life
        print(life)
        time.sleep(1)


if __name__ == '__main__':
    main()
    # a = np.random.choice(["-", "+", "="], size=(10, 10))
    # print(a)
    # print(a[1:2])


from sklearn.linear_model import SGDClassifier

SGDClassifier().partial_fit()
