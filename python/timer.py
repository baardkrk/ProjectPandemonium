from timeit import timeit
from typing import List


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True


def for_loop(n: int):
    s = []
    for i in range(n):
        if is_prime(i):
            s.append(i)
    return s


def get_primes(i: int, n: int, s: List[int]) -> List[int]:
    if i >= n:
        return s
    if is_prime(i):
        s.append(i)
    return get_primes(i+1, n, s)


def recursive_non_thread(n: int):
    s = []
    i = 0
    return get_primes(i, n, s)


def comprehension(n: int):
    return [s for s in range(n) if is_prime(s)]


def timed():
    for_loop_seconds = round(timeit('for_loop(100)', setup='from __main__ import for_loop, is_prime'), 3)
    recursive_seconds = round(timeit('recursive_non_thread(100)', setup='from __main__ import recursive_non_thread, is_prime, get_primes'), 3)
    comprehension_seconds = round(timeit('comprehension(100)', setup='from __main__ import comprehension, is_prime'), 3)

    print(f'For loop: {for_loop_seconds}\nRecursive: {recursive_seconds}\nList comprehension: {comprehension_seconds}')


def test():
    print(comprehension(100))
    print(for_loop(100))
    print(recursive_non_thread(100))


if __name__ == '__main__':
    timed()
    #test()
