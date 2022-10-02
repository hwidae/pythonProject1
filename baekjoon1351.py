from collections import defaultdict
def f(a):
    if B[a] != 0 :
        return B[a]
    B[a] = f(a//p) + f(a//q)
    return B[a]

n, p, q = map(int, input().split())
B = defaultdict(int)
B[0] = 1
print(f(n))

# for i in range(1,n+1):
#     output = B[int(i//p)] + B[int(i//q)]
#     B[i] = output
