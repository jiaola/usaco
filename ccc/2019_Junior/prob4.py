s = input()
h = 0
v = 0
for i in s:
    if i == 'H':
        h += 1
    else:
        v += 1
h %= 2
v %= 2
if h == 1 and v == 1:
    print("4 3")
    print("2 1")
elif h == 1:
    print("3 4")
    print("1 2")
elif v == 1:
    print("2 1")
    print("4 3")
else:
    print("1 2")
    print("3 4")


