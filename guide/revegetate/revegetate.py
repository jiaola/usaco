import sys


def main(pname):
    sys.stdin = open('revegetate.in', 'r')
    sys.stdout = open('revegetate.out', 'w')

    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append([])
    for i in range(m):
        pasture1, pasture2 = map(int, input().split())
        graph[pasture1 - 1].append(pasture2 - 1)
        graph[pasture2 - 1].append(pasture1 - 1)

    l = [0] * n
    for i in range(n):
        seeds = [1, 2, 3, 4]
        for j in graph[i]:
            if l[j] > 0 and l[j] in seeds:
                seeds.remove(l[j])
        l[i] = seeds[0]
    print(''.join([str(i) for i in l]))


if __name__ == "__main__":
    main('revegetate')
