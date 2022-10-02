N = int(input())
dp = [0]*(N+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = dp[1]+dp[3] // dp[2]+dp[2] // dp[3]+dp[1]
dp[5] = dp[4]+dp[1] // dp[1]+dp[4]