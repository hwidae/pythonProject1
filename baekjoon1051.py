N, M = map(int, input().split())
square_list = [[0 for i in range(M)] for i in range(N)]
searchedList = [1]
searchNmb = 1
for i in range(N):
    data_list = []
    data_list = str(input())
    for j in range(M):
        square_list[i][j] = int(data_list[j])
print(square_list)
while searchNmb <= min(N,M):
    for i in range(N-searchNmb):
        for j in range(M-searchNmb):
            if square_list[i][j] == square_list[i][j+searchNmb] and square_list[i][j+searchNmb] == square_list[i+searchNmb][j] and square_list[i+searchNmb][j] == square_list[i+searchNmb][j+searchNmb]:
                searchedList.append((searchNmb+1)**2)
                break
        if (searchNmb+1)**2 in searchedList:
            break
    searchNmb += 1

print(searchedList)
print(max(searchedList))