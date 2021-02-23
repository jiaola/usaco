import sys


def main():
    lst = list(input())
    n = len(lst)
    nl = nm = ns = 0
    for i in lst:
        if i == 'L':
            nl += 1
        elif i == 'M':
            nm += 1
        else:
            ns += 1
    lst_copy = 'L' * nl + 'M' * nm + 'S' * ns

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
    swap_cnt = 0
    for pair in [('L', 'M'), ('M', 'S'), ('S', 'L')]:
        swap_cnt += min(swaps[pair[0]][pair[1]], swaps[pair[1]][pair[0]])
    cycles = total - swap_cnt * 2
    print(cycles // 3 * 2 + swap_cnt)


if __name__ == '__main__':
    main()
