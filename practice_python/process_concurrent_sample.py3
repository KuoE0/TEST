#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Filename: process_concurrent_sample.py3
# Author:   KuoE0 <kuoe0.tw@gmail.com>
#
# Copyright (C) 2016
#
# Distributed under terms of the MIT license.

"""

"""

from concurrent.futures import ProcessPoolExecutor
import time
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return n, False
    return n, True

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        task_list = []
        for p in PRIMES:
            t = executor.submit(is_prime, p)
            t.add_done_callback(lambda f: print(
                "{0}: {1}".format(*f.result())))
            task_list.append(t)
