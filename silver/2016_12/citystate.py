import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    city_state = {}
    for i in range(n):
        city, state = input().split()
        if city[:2] not in city_state:
            city_state[city[:2]] = {}
        if state not in city_state[city[:2]]:
            city_state[city[:2]][state] = 0
        city_state[city[:2]][state] += 1
    ans = 0
    for city in city_state:
        for state in city_state[city]:
            if city == state:
                continue
            if state in city_state:
                if city in city_state[state]:
                    ans += city_state[city][state] * city_state[state][city]
    print(ans // 2)


if __name__ == "__main__":
    main('citystate')
