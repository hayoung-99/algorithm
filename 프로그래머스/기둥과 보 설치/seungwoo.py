world = {}
answer = []


def is_relative_frame(build_frame, installed_frame):
    [x, y, a, _] = build_frame
    [x1, y1, a1, _] = installed_frame
    if a and a1:
        return (x1 == x or x1 == x + 1) and y == y1
    elif a:
        return (x1 == x or x1 == x + 1) and (y == y1 or y == y1 + 1)
    elif a1:
        return (x1 == x or x1 == x + 1) and (y + 1 == y1 or y == y1)
    return x1 == x and (y1 == y + 1 or y1 + 1 == y)


def inspect_remove_pillar(build_frame):
    [x, y, _, _] = build_frame
    relatives = list(filter(is_relative_frame, answer))


def inspect_remove_beam(build_frame):
    [x, y, _, _] = build_frame
    relatives = list(filter(is_relative_frame, answer))


def inspect_install_pillar(build_frame):
    [x, y, _, _] = build_frame
    if not y:
        answer.append(build_frame[:3])
    relatives = list(filter(is_relative_frame, answer))


def inspect_install_beam(build_frame):
    [x, y, _, _] = build_frame
    relatives = list(filter(is_relative_frame, answer))


def inspect(build_frame):
    [_, _, a, b] = build_frame
    if a and b:
        return inspect_install_beam(build_frame)
    elif a:
        return inspect_remove_beam(build_frame)
    elif b:
        return inspect_install_pillar(build_frame)
    return inspect_remove_pillar(build_frame)


def remove(build_frame):
    if inspect(build_frame):
        answer.remove(build_frame[:3])


def install(build_frame):
    if inspect(build_frame):
        answer.append(build_frame[:3])


def build(build_frame):
    if build_frame[-1]:
        install(build_frame)
    else:
        remove(build_frame)


def build_earth(n):
    grind = lambda i: world.update({f"{i}-0": 1.0})
    list(map(grind, range(n + 1)))


def solution(n, build_frame):
    build_earth(n)
    list(map(build, build_frame))
    return answer


solution(
    5,
    [
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [2, 1, 0, 1],
        [2, 2, 1, 1],
        [5, 0, 0, 1],
        [5, 1, 0, 1],
        [4, 2, 1, 1],
        [3, 2, 1, 1],
    ],
)

print(world)
