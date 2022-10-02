dp = [0] * (10**6+1)
dp[0] = 0
dp[1] = 1

N = int(input())
if N > 1 :
    for i in range(2,N+1):
        dp[i] = (dp[i-1] + dp[i-2])%10**9
else :
    for i in range(2,abs(N)+1):
        dp[i] = dp[i-2] - dp[i-1]
        if dp[i] < 0 :
            dp[i] = dp[i]*(-1)%10**9
            dp[i] *= -1
        else:
            dp[i] %= 10**9

if dp[abs(N)] > 0 :
    print('1')
elif dp[abs(N)] == 0:
    print('0')
else :
    print('-1')
print((abs(dp[abs(N)])))







# def fib_abs(n) :
#     if n == 0:
#         return 0
#     elif abs(n) == 1:
#         return 1
#     elif n > 1 :
#         return fib_abs(n-1) + fib_abs(n-2)
#     else :
#         return fib_abs(n+2) - fib_abs(n+1)
#
# N = int(input())
# if fib_abs(N) > 0 :
#     print('1')
# elif fib_abs(N) == 0:
#     print('0')
# else :
#     print('-1')
# print((abs(fib_abs(N))%1000000000))
