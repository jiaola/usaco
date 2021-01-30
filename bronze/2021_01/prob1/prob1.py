import sys


def main():
    a = {}
    s = list(input())
    for i in range(26):
        a[s[i]] = i
    s = list(input())
    ans = 1
    for i in range(1, len(s)):
        if a[s[i]] <= a[s[i-1]]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
