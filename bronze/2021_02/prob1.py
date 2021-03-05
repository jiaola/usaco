import sys

zodiac = {
    "Ox": 0,
    "Tiger": 1,
    "Rabbit": 2,
    "Dragon": 3,
    "Snake": 4,
    "Horse": 5,
    "Goat": 6,
    "Monkey": 7,
    "Rooster": 8,
    "Dog": 9,
    "Pig": 10,
    "Rat": 11
}

birth_year = {
    "Bessie": 0
}

birth_zodiac = {
    "Bessie": "Ox"
}


# Essie was born in previous Dragon year from Bessie
def get_year(dir, current, last):
    if dir == 'previous':
        if zodiac[current] > zodiac[last]:
            return -(12 - zodiac[current] + zodiac[last])
        elif zodiac[current] == zodiac[last]:
            return -12
        else:
            return -(zodiac[last] - zodiac[current])
    else:
        if zodiac[current] > zodiac[last]:
            return zodiac[current] - zodiac[last]
        elif zodiac[current] == zodiac[last]:
            return 12
        else:
            return 12 - zodiac[last] + zodiac[current]


def main(pname):
    # sys.stdin = open(pname + '.in', 'r')
    N = int(input())

    for i in range(N):
        line = input().split()
        n1 = line[0]
        n2 = line[-1]
        birth_zodiac[n1] = line[4]
        year = get_year(line[3], line[4], birth_zodiac[n2])
        birth_year[n1] = birth_year[n2] + year
        if line[0] == 'Elsie':
            print(abs(birth_year['Elsie']))
            break


if __name__ == "__main__":
    main('prob1')
