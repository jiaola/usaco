n = int(input())
for i in range(n):
    s = input()
    cnt = 1
    for j in range(1, len(s)):
        if s[j] == s[j-1]:
            cnt += 1
        else:
            print(cnt, s[j-1], end=' ')
            cnt = 1
    print(cnt, s[-1])

