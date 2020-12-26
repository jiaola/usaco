import sys
from copy import deepcopy


def check_finished(current, stopped, direction):
    n = len(stopped)
    for i in range(n):
        if stopped[i]:
            continue
        for j in range(n):
            if direction[i] == direction[j]:
                continue
            if direction[i] == 'E':
                if current[i][0] < current[j][0]:
                    return False
            else:
                if current[i][1] < current[j][1]:
                    return False
    return True


def stop(start, current, direction, stopped, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if stopped[i]:
                continue
            if current[i] == current[j] and not stopped[j]:
                continue
            if direction[i] == direction[j]:
                if direction[i] == 'E' and start[i][1] == start[j][1]:
                    if current[i][0] == start[j][0]:
                        stopped[i] = True
                elif direction[i] == 'N' and start[i][0] == start[j][0]:
                    if current[i][1] == start[j][1]:
                        stopped[i] = True
            else:
                if direction[i] == 'E':
                    if current[i][0] == current[j][0] and start[j][1] <= current[i][1] <= current[j][1]:
                        stopped[i] = True
                else:
                    if current[i][1] == current[j][1] and start[j][0] <= current[i][0] <= current[j][0]:
                        stopped[i] = True
    return stopped


def move(start, current, direction, stopped, n):
    min_time = 10 ** 10
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if stopped[i]:
                continue
            if direction[i] == direction[j]:
                if direction[i] == 'E' and current[i][1] == current[j][1]:
                    t = start[j][1] - current[i][1]
                    if 0 < t < min_time:
                        min_time = t
                if direction[i] == 'N' and current[i][0] == current[j][0]:
                    t = start[j][0] - current[i][0]
                    if 0 < t < min_time:
                        min_time = t
            else:
                if direction[i] == 'E':
                    if current[i][1] < start[j][1] or start[i][0] > current[j][0]:
                        continue
                    t = current[j][0] - current[i][0]
                    if t + current[j][1] < current[i][1]:
                        continue
                    if 0 < t < min_time:
                        min_time = t
                else:
                    if start[i][1] > current[j][1] or current[i][0] < start[j][0]:
                        continue
                    t = current[j][1] - current[i][1]
                    if t + current[j][0] < current[i][0]:
                        continue
                    if 0 < t < min_time:
                        min_time = t
    return min_time


def main(pname):
    # sys.stdin = open(pname + '.in', 'r')

    n = int(input())
    direction = []
    start = []
    for i in range(n):
        d, x, y = input().split()
        x = int(x)
        y = int(y)
        direction.append(d)
        start.append([x, y])

    current = deepcopy(start)
    stopped = [False] * n

    while True:
        min_time = move(start, current, direction, stopped, n)
        for i in range(n):
            if stopped[i]:
                continue
            if direction[i] == 'E':
                current[i][0] += min_time
            else:
                current[i][1] += min_time
        stopped = stop(start, current, direction, stopped, n)
        if check_finished(current, stopped, direction):
            break

    for i in range(n):
        if not stopped[i]:
            print('Infinity')
        else:
            if direction[i] == 'E':
                print(current[i][0] - start[i][0])
            else:
                print(current[i][1] - start[i][1])


if __name__ == '__main__':
    main('rut')