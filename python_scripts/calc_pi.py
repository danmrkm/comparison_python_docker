#!/bin/env python3

import time
import sys
from datetime import datetime


if __name__ == "__main__":

    NUM_LOOP = 100000000
    WORK_DIR = "/var/work"

    args = sys.argv

    pi = 0
    start = time.time()

    # 円周率を計算
    for i in range(1, NUM_LOOP):

        if i % 2 == 0:
            b = -1
        else:
            b = 1

        pi += (4 / (2 * i - 1)) * b

    # 計算にかかった時間を取得
    end = time.time()
    elapsed = end - start

    print(pi)
    print("time:{0}".format(elapsed) + " sec")

    nowtime = datetime.now().strftime("%Y%m%d%H%M%S")

    # 結果をファイルに書き込む
    with open(WORK_DIR + "/result_" + args[1] + "_" + nowtime + ".txt", mode="w") as f:
        f.write(str(elapsed))
