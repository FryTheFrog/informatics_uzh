#!/usr/bin/env python3

import os

def get_average_grade(path):

    if not os.path.exists(path):
        return None

    with open(path, "r") as f:
        num = 0
        sum = 0
        for l in f.readlines():
            if l.startswith("#"):
                continue

            idx = l.find(":")
            if idx > 0:
                l2 = l[idx+1:]
                f = float(l2)
                sum += f
                num += 1

        if sum == 0:
            return 0.0
        else:
            return sum/num

