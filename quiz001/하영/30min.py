N, M, R = map(int, input().split())
dist_info = []

for i in range(M):
    dist_info.append(list(map(int, input().split())))

fuel = list(map(int, input().split()))
route = list(map(int, input().split()))

# 연료가 왜 8이 나올 수 있는지 아무리 읽어봐도
# 이거 쌉소리아냐?!?!? 하고 합리적 의심하다가
# 30분 만에서야 이해했습니다.. ㅠㅠㅠㅠㅠㅠㅠ