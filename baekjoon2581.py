def findnmb(n):
    if n == 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else :
            continue
    return True
# print(findnmb(17))

M = int(input())
N = int(input())
A = []
for i in range(M, N + 1):
    if findnmb(i):
        A.append(i)

if len(A) == 0:
    print(-1)

else:
    print(sum(A))
    print(min(A))
    print(A)