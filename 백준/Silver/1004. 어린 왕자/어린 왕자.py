import math

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    planet_pos = []
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        planet_pos.append((cx, cy, r))

    # 행성 안에 출발점/도착점이 있는 경우의 행성 set 구하기
    planets_include_start = set()
    planets_include_end = set()

    planet_idx = 0
    for x, y, r in planet_pos:
        if math.pow(x1 - x, 2) + math.pow(y1 - y, 2) < math.pow(r, 2):
            planets_include_start.add(planet_idx)

        if math.pow(x2 - x, 2) + math.pow(y2 - y, 2) < math.pow(r, 2):
            planets_include_end.add(planet_idx)

        planet_idx += 1

    answer = planets_include_end.union(planets_include_start) - planets_include_end.intersection(planets_include_start)
    print(len(list(answer)))
