'''
@create_time: 2026/3/25 下午2:10
@Author: GeChao
@File: 多进程示例.py
'''
"""
from time import time, sleep

'''多进程'''
def calculate(n):
    sleep(1)
    return f"calculate complete of {n}"


if __name__ == '__main__':
    start = time()
    result = [calculate(i) for i in range(2)]
    end = time()
    # Elapsed time: 2.00s
    print(f"take time: {end - start:.2f}s")
"""

'''进程池'''
from time import time, sleep
from concurrent.futures import ProcessPoolExecutor


def calculate(n):
    sleep(1)
    return f"calculate complete of {n}"


if __name__ == '__main__':
    start = time()
    with ProcessPoolExecutor() as executor:
        result = executor.map(calculate, range(10))

    end = time()
    # Elapsed time: 2.00s
    print(f"take time: {end - start:.2f}s")
