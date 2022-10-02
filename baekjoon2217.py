N = int(input())
rope_list = []
weight_list = []
for i in range(N):
    rope_list.append(int(input()))
    # 가장 작은 로프*N = 물체무게가되게 (1 ≤ N ≤ 100,000)
    # 가장작은 무게의 로프를 사용하지않아도 됨 10**4까지 입력될수있음
    # 가장작은무게의 로프*N, 그다음 무게의 로프*(N-1), .... , 최대무게의 로프*1 중에서 최대값
rope_list.sort()
for i in range(1,N+1):
    a = rope_list.pop()
    weight_list.append(i*a)
print(max(weight_list))