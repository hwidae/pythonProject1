N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
N_dic = {}
for i in N_list:
    N_dic[i] = None
for i in M_list:
    if i in N_dic :
        print('1')
    else :
        print('0')