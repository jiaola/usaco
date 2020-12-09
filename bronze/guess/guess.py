import sys


def most_animals(d, l):
    m = 0
    for key, val in d.items():
        count = sum([val[i] for i in l])
        if count > m:
            m = count
            k = key
    return k


def most_two(at):
    n = len(at)
    max_pair = 0
    pair = ()
    left = None
    for i in range(n):
        for j in range(i+1, n):
            common = []
            for k in range(len(at[i])):
                common.append(at[i][k] * at[j][k])
            count = sum(common)
            if count > max_pair:
                pair = (i, j)
                left = common
                max_pair = count
    return left, pair


def most(at, lst, exclude):
    n = len(at)
    max_pair = 0
    most_idx = -1
    left = lst
    for i in range(n):
        if i in exclude:
            continue
        common = []
        for k in range(len(lst)):
            common.append(lst[k] * at[i][k])
        count = sum(common)
        if count > max_pair:
            max_pair = count
            left = common
            most_idx = i
    return left, most_idx


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    animals = []
    animal_traits = []
    traits = []
    n = int(input())
    for i in range(n):
        line = input().split()
        animal_traits.append(line[2:])
        traits.extend(line[2:])
    traits = list(set(traits))
    at = []
    for i in range(n):
        lst = [0] * len(traits)
        for j in range(len(traits)):
            if traits[j] in animal_traits[i]:
                lst[j] = 1
        at.append(lst)
    left, pair = most_two(at)
    print(sum(left)+1)

    # find the most


    # max_steps = 0
    # for first in chs:
    #     steps = 1
    #     chs_copy = chs.copy()
    #     v = chs_copy.pop(ch)
    #     answer = [i for i in range(n) if v[i] == 1]
    #     while len(answer) > 1:
    #         ch = most_animals(chs_copy, answer)
    #         v = chs_copy.pop(ch)
    #         answer = [i for i in answer if v[i] == 1]
    #         steps += 1
    #     max_steps = max(max_steps, steps)
    # print(max_steps)


if __name__ == "__main__":
    main('guess')
