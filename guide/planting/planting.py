import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    graph = []
    for i in range(n):
        graph.append([])
    for i in range(n-1):
        a1, a2 = map(int, input().split())
        graph[a1 - 1].append(a2 - 1)
        graph[a2 - 1].append(a1 - 1)

    m = 0
    for i in graph:
        m = max(m, len(i))
    print(m+1)


if __name__ == "__main__":
    main('planting')
