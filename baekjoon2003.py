N, M = map(int, input().split())
A = list(map(int,input().split()))
print(A)

i = 0
now = 0
total = 0
cnt = 0
while now < N and i < N :
    total += A[i]
    i += 1
    if total > M :
        total = 0
        now += 1
        i = now
    elif total == M :
        total = 0
        cnt += 1
        now += 1
        i = now
print(cnt)