import sys

# dict = {
#     'MI': {
#         'FL': 5
#     },
#     'FL': {
#         'MI': 2
#     }
# }
#
# MI, FL <-> FL, MI  = 5 * 2 = 10

# dict = {
#     'MIFL': 5,
#     'FLMI': 2
# }
#
#

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    city_state = {}
    for i in range(n):
        city, state = input().split()
        cs = city[:2] + state
        if cs not in city_state:
            city_state[cs] = 0
        city_state[cs] += 1
    ans = 0
    for cs1 in city_state:
        if cs1[2:] == cs1[:2]:
            continue
        cs2 = cs1[2:] + cs1[:2]
        if cs2 in city_state:
            ans += city_state[cs1] * city_state[cs2]
    print(ans // 2)


if __name__ == "__main__":
    main('citystate')
