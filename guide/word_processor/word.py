import sys

sys.stdin = open('word.in', 'r')
sys.stdout = open('word.out', 'w')

n, k = [int(i) for i in input().split()]
words = input().split()

l = len(words[0])
sys.stdout.write(words[0])
for i in range(1, n):
    if l + len(words[i]) > k:
        print()
        l = len(words[i])
    else:
        sys.stdout.write(' ')
        l += len(words[i])
    sys.stdout.write(words[i])

    
        