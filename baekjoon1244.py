N = int(input())
switch = list(map(int, input().split()))
students = int(input())


def turn(n):
    if n == 0:
        n = 1
    else:
        n = 0
    return n


for _ in range(students):

    S, card = map(int, input().split())
    if S == 1:
        for k in range(N):
            if (k+1) % card == 0:
                switch[k]=turn(switch[k])

    if S == 2:
        i = 0
        while card - 1 - i >= 0 and card + i -1 < N:
            if switch[card - 1 - i] == switch[card - 1 + i]:
                i += 1
            else:
                break

        for k in range(i) :
            switch[card-1-k] = turn(switch[card-1-k])
            switch[card - 1 + k] = switch[card-1-k]
cnt = 0
while cnt < len(switch):
    print(switch[cnt], end=" ")
    if cnt % 20 == 19:
        print()
    cnt += 1