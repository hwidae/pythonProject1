import math
N = int(input())
for i in range(N) :
    xa, ya, ra, xb, yb, rb = map(int, input().split())
    if xa == xb and ya == yb and ra == rb :
        print('-1')
    elif math.sqrt((xa-xb)**2+(ya-yb)**2) == (ra+rb) :
        print('1')
    elif math.sqrt((xa-xb)**2+(ya-yb)**2) == abs(ra-rb) :
        print('1')
    elif abs(ra-rb) < math.sqrt((xa-xb)**2+(ya-yb)**2) < (ra+rb) :
        print('2')
    else :
        print('0')