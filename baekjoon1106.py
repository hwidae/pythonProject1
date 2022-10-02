# C, N = map(int, input().split())
# p_e = {}
# population = []
# for i in range(N):
#     b, a = map(int, input().split())
#     if a in p_e:
#         p_e[a] = min(p_e[a], b)
#     else :
#         p_e[a] = b
#         population.append(a)
# population.sort()
# dp = [0]*1001
# dp[0] = 0
# for i in population:
#         dp[i] = p_e[i]
# print(dp)
#
# for i in range(population[0]+1, 1001):
#     for j in population:
#         for k in population :
#             if (j+k) < i :
#                 dp[i] = min(dp[i-(j+k)]+dp[j+k], dp[i])
#
# print(dp)
# print(min(dp[C:]))


C, N = map(int, input().split())
p_e = {}
population = []
for i in range(N):
    b, a = map(int, input().split())
    if a in p_e:
        p_e[a] = min(p_e[a], b)
    else :
        p_e[a] = b
        population.append(a)
population.sort()
dp = [1000000]*(C+101)
dp[0] = 0
for i in population:
        dp[i] = p_e[i]

# for i in range(population[0], 1001, population[0]):
#     dp2[i] = dp2[i-population[0]]+dp2[population[0]]

for i in range(population[0]+1, C+101):
    for j in population:
        if j < i :
            dp[i] = min(dp[i-j]+dp[j],dp[i])
# print(dp)
# for i in range(population[0]+1, 1001):
#     for j in population:
#         if j < i and dp[i] != 0:
#             dp[i] = min(dp[i-j]+dp[j], dp[i])
#         elif j < i == 0:
#             tmp = dp[i-population[0]]+dp[population[0]]
#             dp[i] = min(dp[i-j]+dp[j], tmp)
print(min(dp[C:]))