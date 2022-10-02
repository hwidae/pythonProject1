import math
M, N = map(int, input().split())
prime_nmb = []
for i in range(M,N+1):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            break
        prime_nmb.append(i)
for i in set(prime_nmb):
    print(i)
