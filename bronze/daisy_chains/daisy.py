
def main(pname):
    n = int(input())
    lst = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            p = lst[i:j]
            total = sum(p)
            if total % len(p) != 0:
                continue
            avg = int(total / len(p))
            if avg in p:
                count += 1
    print(count)


if __name__ == '__main__':
    main('daisy')