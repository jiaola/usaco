import sys


def add(i, lineup, graph):
    if i not in lineup:
        lineup.append(i)
        for j in graph[i]:
            lineup = add(j, lineup, graph)
    return lineup


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    cows = sorted(['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue'])
    n = int(input())
    graph = []
    for i in range(8):
        graph.append([])
    for i in range(n):
        tokens = input().split()
        c1 = cows.index(tokens[0])
        c2 = cows.index(tokens[-1])
        graph[c1].append(c2)
        graph[c2].append(c1)

    starter = []
    for i in range(8):
        if len(graph[i]) < 2:
            starter.append(i)

    starter.sort()
    lineup = []
    for i in starter:
        lineup = add(i, lineup, graph)

    for i in lineup:
        print(cows[i])


if __name__ == "__main__":
    main('lineup')
