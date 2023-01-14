# start -> end 가는 최소 거리
def get_min_dist(start, end):
    min_dist = dist_info[start][end]

    if start == end:
        return 0

    for i in range(M):
        if (i != start) and (i != end):
            temp = dist_info[start][i] + dist_info[i][end]

            if min_dist > temp:
                min_dist = temp

    return min_dist


def get_min_fuel():



N, M, R = map(int, input().split())
dist_info = []

for i in range(M):
    dist_info.append(list(map(int, input().split())))

fuel = list(map(int, input().split()))

# 순회 정보 저장 -> for문 돌면서 구역 개수 저장
route = list(map(int, input().split()))
area_dict = {}
for i in route:
    if i not in area_dict.keys():
        area_dict[i] = 1
    else:
        area_dict[i] += 1

min_fuel = min(fuel)  # fuel 중 최솟값

# 모든 경로의 dist 합 구하기
sum_dist = 0
for idx, area in enumerate(route):
    if idx == 0:
        prev_area = 1

    else:
        prev_area = route[idx - 1]

    dist = get_min_dist(prev_area - 1, area - 1)

    sum_dist += dist

used_fuel = sum_dist + min_fuel
if used_fuel <= R:
    print("0 ", used_fuel)

# 투 포인터를 이용한 동료가 순회할 경로 구하기
else:
    for start in range(1, N):
        for end in range(i, N):
            area_num = end - start
