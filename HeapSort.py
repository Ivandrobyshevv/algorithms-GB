from datetime import datetime
from random import randint
from typing import List


def heapsort(alist: List[int]) -> None:
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)


def parent(i: int) -> float:
    return (i - 1) // 2


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def build_max_heap(alist: List[int]) -> None:
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1


def max_heapify(alist: list, index: int, size: int):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)


def start(list_nums: List[int]):
    heapsort(list_nums)
    print('Sorted list: ', end='')
    print(list_nums)


if __name__ == '__main__':
    list_nums = [randint(0, 1_000) for x in range(1_000)]
    start_time = datetime.now()
    start(list_nums)
    print(datetime.now() - start_time)
