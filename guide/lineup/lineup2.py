import sys
import itertools


def check(lineup, graph, cows):
    for i in range(len(lineup)):
        cow_name = lineup[i]
        cow_index = cows.index(cow_name)
        prev_next = []
        if i > 0:
            prev = lineup[i-1]
            prev_index = cows.index(prev)
            prev_next.append(prev_index)
        if i < 7:
            nxt = lineup[i+1]
            nxt_index = cows.index(nxt)
            prev_next.append(nxt_index)
        for j in graph[cow_index]:
            if j not in prev_next:
                return False
    return True


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

    perms = list(itertools.permutations(cows, 8))
    perms.sort()

    for i in perms:
        if check(i, graph, cows):
            for j in i:
                print(j)
            return


if __name__ == "__main__":
    main('lineup')
