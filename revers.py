from datetime import datetime
from random import randint

if __name__ == '__main__':
    list_nums = [randint(0, 1_000) for x in range(1_000)]
    print(f"[START]: {list_nums}'")
    print(f'[REVERS]: {list_nums[::-1]}')
