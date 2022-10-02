N = int(input())

dp = [0] * (N+1)

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(1,N+1):
    for j in range(1,int(i**1/2)+1):
        if i > j*j :
            dp[i] =
print(dp)
print(dp[N])