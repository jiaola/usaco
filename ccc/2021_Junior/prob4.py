import sys


def main(pname):
    lst = list(input())
    n = len(lst)
    lst_copy = lst.copy()
    lst_copy.sort()

    swaps = {
        "L": {"M": 0, "S": 0},
        "M": {"L": 0, "S": 0},
        "S": {"L": 0, "M": 0}
    }
    total = 0
    for i in range(n):
        if lst_copy[i] != lst[i]:
            swaps[lst_copy[i]][lst[i]] += 1
            total += 1
    swap_lm = min(swaps["L"]["M"], swaps["M"]["L"])
    swap_ms = min(swaps["M"]["S"], swaps["S"]["M"])
    swap_sl = min(swaps["L"]["S"], swaps["S"]["L"])
    sc = swap_lm + swap_ms + swap_sl
    cycles = total - sc * 2
    print(cycles // 3 * 2 + sc)


if __name__ == '__main__':
    main('prob4')
