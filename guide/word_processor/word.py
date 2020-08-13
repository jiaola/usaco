with open('word.in', 'r') as input:
    n, k = [int(i) for i in input.readline().strip().split()]
    words = input.readline().strip().split()

with open('word.out', 'w') as output:
    l = len(words[0])
    output.write(words[0])
    for i in range(1, n):
        if l + len(words[i]) > k:
            output.write('\n')
            l = len(words[i])
        else:
            output.write(' ')
            l += len(words[i])
        output.write(words[i])

    
        