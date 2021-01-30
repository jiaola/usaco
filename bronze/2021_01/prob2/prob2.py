import sys


def main():
    odd = 0
    even = 0
    n = int(input())
    nums = [int(i) for i in input().split()]
    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        ans = odd * 2 + 1
    elif even == odd:
        ans = odd * 2
    else:
        m = (odd - even) // 3
        r = (odd - even) % 3
        ans = (even + m) * 2
        if r == 1:
            ans -= 1
        elif r == 2:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
