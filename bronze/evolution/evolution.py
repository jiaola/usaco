import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    traits = []
    all_traits = set()
    N = int(input())
    for i in range(N):
        line = input().split()
        k = line[0]
        traits.append(line[1:])
        all_traits.update(line[1:])
    all_traits = list(all_traits)
    for i in range(len(all_traits)):
        for j in range(i+1, len(all_traits)):
            trait_i = all_traits[i]
            trait_j = all_traits[j]
            has_i = False
            has_j = False
            both = False
            for t in traits:
                if trait_i in t and trait_j in t:
                    both = True
                elif trait_i in t:
                    has_i = True
                elif trait_j in t:
                    has_j = True
            if has_i and has_j and both:
                print('no')
                return
    print('yes')


if __name__ == "__main__":
    main('evolution')
