N = int(input())
room = [[0]*N for _ in range(N)]
cntHorizon = 0
cntVertical = 0
for i in range(N):
    room[i] = input()

for i in range(N):
    cnt1 = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt1 += 1
        else:
            cnt1 = 0
        if cnt1 == 2:
            cntHorizon += 1

for i in range(N):
    cnt1 = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt1 += 1
        else:
            cnt1 = 0
        if cnt1 == 2:
            cntVertical += 1



print(cntHorizon, cntVertical)