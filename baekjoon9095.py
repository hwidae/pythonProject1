import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    n = int(input())
    dp = [0]*(11)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if n >= 4:
        for i in range(4,11):
            dp[i] = dp[i-3] + + dp[i - 2] + dp[i - 1]
    print(dp[n])