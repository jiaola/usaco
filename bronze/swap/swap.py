import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, k = [int(i) for i in input().split()]
    p = list()
    p.append([int(i) for i in input().split()])
    p.append([int(i) for i in input().split()])
    lst = []
    origin_lst = []
    for i in range(n):
        lst.append(i+1)
        origin_lst.append(i+1)
    for i in range(k):
        for a in p:
            l, m = a
            new_lst = lst[l-1:m][::-1]
            if l > 1:
                new_lst = lst[0:l-1] + new_lst
            if m < n:
                new_lst = new_lst + lst[m:]
            lst = new_lst
        if lst == origin_lst:
            break
    for i in range(k % (i+1)):
        for a in p:
            l, m = a
            new_lst = lst[l-1:m][::-1]
            if l > 1:
                new_lst = lst[0:l-1] + new_lst
            if m < n:
                new_lst = new_lst + lst[m:]
            lst = new_lst
    print('\n'.join([str(i) for i in lst]))


if __name__ == "__main__":
    main('swap')
