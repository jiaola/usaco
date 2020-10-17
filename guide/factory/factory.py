import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())

    graph = []
    for i in range(n):
        graph.append([])
    for i in range(n-1):
        s1, s2 = map(int, input().split())
        graph[s1 - 1].append(s2 - 1)

    sinks = [i for i in range(n) if len(graph[i]) == 0]
    if len(sinks) == 1:
        print(sinks[0]+1)
    else:
        print(-1)


if __name__ == "__main__":
    main('factory')
