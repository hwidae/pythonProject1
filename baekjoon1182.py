N, S = map(int, input().split())
nmb_list = list(map(int, input().split()))
cnt = 0
while len(nmb_list) > 0:
    sum_nmb = sum(nmb_list)
    print(sum_nmb)
    if sum_nmb == S:
        cnt += 1
    for i in range(len(nmb_list)-1):
        sum_nmb -= nmb_list[i]
        print("sum_nmb:",sum_nmb)
        if sum_nmb == S:
            cnt += 1
    nmb_list.pop()
    print("nmb_list :",nmb_list)

print("cnt :",cnt)