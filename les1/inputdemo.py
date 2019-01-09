# -*- coding : utf-8 -*-

import psutil


if __name__ == '__main__':
    l = psutil.pids()
    for m in l:
        p = psutil.Process(m)
        print(p.name())
        