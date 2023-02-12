answer = []


def is_relative_frame(build_frame, installed_frame):
    [x, y, a] = build_frame[:3]
    [x1, y1, a1] = installed_frame[:3]
    if build_frame == installed_frame:
        return False
    elif a and a1:
        return (x1 + 1 == x or x1 == x + 1) and y == y1
    elif a:
        return (x1 == x or x1 == x + 1) and (y == y1 or y == y1 + 1)
    elif a1:
        return (x1 == x or x1 + 1 == x) and (y + 1 == y1 or y == y1)
    return x1 == x and (y1 == y + 1 or y1 + 1 == y)


def inspect_install_pillar(build_frame):
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    if build_frame[1] == 0:
        return True
    # 아래 뭐 있으면 됨
    beams = list(filter(lambda f: f[2], relatives))
    pillars = list(filter(lambda f: not f[2], relatives))
    bottom_beams = list(filter(lambda f: f[1] == build_frame[1], beams))
    bottom_pillars = list(filter(lambda f: f[1] + 1 == build_frame[1], pillars))
    return bool(bottom_beams) or bool(bottom_pillars)


def inspect_install_beam(build_frame):
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    beams = list(filter(lambda f: f[2], relatives))
    pillars = list(filter(lambda f: not f[2], relatives))
    side_beams = list(filter(lambda f: f[2] == build_frame[2], beams))
    bottom_pillars = list(filter(lambda f: f[1] + 1 == build_frame[1], pillars))
    if bottom_pillars:
        return True
    elif side_beams:
        return len(side_beams) == 2
    return False


def inspect_install(build_frame):
    if build_frame[2]:
        return inspect_install_beam(build_frame)
    return inspect_install_pillar(build_frame)


def inspect_remove(build_frame):
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    answer.remove(build_frame[:3])
    inspections = list(filter(inspect_install, relatives))
    inspection = len(relatives) == len(inspections)
    answer.append(build_frame[:3])
    return inspection


def inspect(build_frame):
    [_, _, a, b] = build_frame
    if a and b:
        return inspect_install_beam(build_frame)
    elif a:
        return inspect_remove(build_frame)
    elif b:
        return inspect_install_pillar(build_frame)
    return inspect_remove(build_frame)


def remove(build_frame):
    inspection = inspect(build_frame)
    if inspection:
        answer.remove(build_frame[:3])


def install(build_frame):
    inspection = inspect(build_frame)
    if inspection:
        answer.append(build_frame[:3])


def build(build_frame):
    if build_frame[-1]:
        install(build_frame)
    else:
        remove(build_frame)


def solution(n, build_frame):
    list(map(build, build_frame))
    return sorted(answer, key=lambda f: (f[0], f[1], f[2]))


print(
    solution(
        5,
        [
            [0, 0, 0, 1],
            [2, 0, 0, 1],
            [4, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [2, 1, 1, 1],
            [3, 1, 1, 1],
            [2, 0, 0, 0],
            [1, 1, 1, 0],
            [2, 2, 0, 1],
        ],
    )
)
