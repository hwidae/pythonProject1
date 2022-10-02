N = int(input())
RGB = [[0] * 3 for _ in range(N + 1)]
RGB[1][0], RGB[1][1], RGB[1][2] = map(int, input().split())
for i in range(2, N + 1):
    price = list(map(int, input().split()))
    RGB[i][0] = min((RGB[i - 1][1] + price[0]), (RGB[i - 1][2] + price[0]))
    RGB[i][1] = min((RGB[i - 1][0] + price[1]), (RGB[i - 1][2] + price[1]))
    RGB[i][2] = min((RGB[i - 1][0] + price[2]), (RGB[i - 1][1] + price[2]))

print(min(RGB[N][0], RGB[N][1], RGB[N][2]))