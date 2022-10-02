import sys
input = sys.stdin.readline
member, N, M = map(int, input().split())
R = 1
def nextround():
    global R, member
    R += 1
    member = member // 2

while member > 1:
    if N % 2 == 0 and M % 2 != 0:
        if N - 1 == M :
            break
        else :
            nextround()
            N = N // 2
            M = (M + 1) // 2
    elif N % 2 != 0 and M % 2 == 0:
        if M - 1 == N :
            break
        else :
            nextround()
            M = M // 2
            N = (N + 1) // 2
    elif N % 2 == 0 and M % 2 == 0:
        nextround()
        N = N // 2
        M = M // 2
    else :
        nextround()
        N = (N + 1) // 2
        M = (M + 1) // 2

print(R)
