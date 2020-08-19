import sys

def main():
    sys.stdin = open('mixmilk.in', 'r')
    sys.stdout = open('mixmilk.out', 'w')

    def mix(bf, mf, bt, mt):
        if mf + mt >= bt: 
            mf = mf + mt - bt 
            mt = bt 
        else:
            mt = mf + mt
            mf = 0    
        return mf, mt

    b1, m1 = [int(i) for i in input().split()]
    b2, m2 = [int(i) for i in input().split()]
    b3, m3 = [int(i) for i in input().split()]
    c = 0
    while True:
        m1, m2 = mix(b1, m1, b2, m2)  
        c += 1
        if c == 100:
            break   
        m2, m3 = mix(b2, m2, b3, m3) 
        c += 1
        if c == 100:
            break         
        m3, m1 = mix(b3, m3, b1, m1) 
        c += 1
        if c == 100:
            break   

    print(m1)
    print(m2)
    print(m3)

if __name__ == "__main__":
    main()
