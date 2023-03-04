def in_range(n, x, y):
    return (0 <= x < n) and (0 <= y < n)


def build_valid(grid, frame_type, x, y):
    # 1. 기둥
    if frame_type == 0:
        # 1-1) 기둥이 바닥에 붙어있다면 OK
        if y == 0:
            return True
        # 1-2) 기둥 끝에 [ㅡ, |, ㅡ] 셋 중 하나와 인접해있다면 OK
        else:
            dxs, dys, frames = [-1, 0, 0], [0, -1, 0], [1, 0, 1]
            for dx, dy, frame in zip(dxs, dys, frames):
                nx, ny = x + dx, y + dy
                if in_range(len(grid), nx, ny) and grid[nx][ny][frame] == 1:
                    return True

    # 2. 보
    elif frame_type == 1:
        # 보 끝에 [왼쪽 |, 오른쪽 |, "양옆" ㅡ]이 있는지 확인
        dxs, dys = [0, 1], [-1, -1]
        for dx, dy in zip(dxs, dys):  # 왼쪽 |, 오른쪽 |
            nx, ny = x + dx, y + dy
            if in_range(len(grid), nx, ny) and grid[nx][ny][0] == 1:
                return True
        if (in_range(len(grid), x - 1, y) and in_range(len(grid), x + 1, y)) and (
                grid[x - 1][y][1] == 1 and grid[x + 1][y][1] == 1):  # 양옆 ㅡ
            return True

    return False


def get_result(grid):
    result = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y][0] == 1:
                result.append([x, y, 0])
            if grid[x][y][1] == 1:
                result.append([x, y, 1])
    return result


def solution(n, build_frame):
    grid = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]  # [0, 0] -> idx: 0(기둥), idx: 1(보)

    for cmd in build_frame:
        x, y = cmd[0], cmd[1]
        # 설치
        if cmd[3] == 1:
            if build_valid(grid, cmd[2], x, y):
                grid[x][y][cmd[2]] = 1
        # # 삭제
        else:
            # 일단 삭제
            grid[x][y][cmd[2]] = 0

            # 인접한 모든 기둥/보
            # 삭제한 frame이 기둥/보냐에 따라 인접한 좌표 및 frame 종류가 달라지므로 따로 처리
            if cmd[2] == 0:
                dxs, dys = [-1, -1, 0, 0, 0, 0], [1, 0, 1, 1, -1, 0]
                frames = [1, 1, 0, 1, 0, 1]
            elif cmd[2] == 1:
                dxs = [-1, 0, 0, 1, 1, 1]
                dys = [0, 0, -1, 0, 0, -1]
                frames = [1, 0, 0, 0, 1, 0]

            for dx, dy, frame in zip(dxs, dys, frames):
                nx, ny = x + dx, y + dy
                # 인접한 기둥/보가 현재 frame을 삭제하더라도 유효한지 검사
                # 하나라도 유효하지 않으면
                # 현재 frame은 삭제하면 안되므로 원위치
                if in_range(len(grid), nx, ny) and grid[nx][ny][frame] == 1:
                    if not build_valid(grid, frame, nx, ny):
                        grid[x][y][cmd[2]] = 1
                        break

    return get_result(grid)
