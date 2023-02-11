answer = []


def is_relative_frame(build_frame, installed_frame):
    [x, y, a, _] = build_frame
    [x1, y1, a1] = installed_frame
    if a and a1:
        return (x1 + 1 == x or x1 == x + 1) and y == y1
    elif a:
        return (x1 == x or x1 == x + 1) and (y == y1 or y == y1 + 1)
    elif a1:
        return (x1 == x or x1 + 1 == x) and (y + 1 == y1 or y == y1)
    return x1 == x and (y1 == y + 1 or y1 + 1 == y)


def is_base_frame(build_frame, installed_frame):
    [x, y, a, _] = build_frame
    [x1, y1, a1] = installed_frame
    if a and a1:
        return y == y1 and (x + 1 == x1 or x1 + 1 == x)
    elif a:
        return y1 + 1 == y and (x + 1 == x1 or x1 == x)
    elif a1:
        return y1 == y and (x1 + 1 == x or x1 == x)
    return y1 + 1 == y


def inspect_remove_pillar(build_frame):
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    bases = list(filter(lambda f: is_base_frame(build_frame, f), relatives))
    if len(bases) == len(relatives):
        return True
    return False


def inspect_remove_beam(build_frame):
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    bases = list(filter(lambda f: is_base_frame(build_frame, f), relatives))
    if len(bases) == len(relatives):
        return True
    return False


def inspect_install_pillar(build_frame):
    [_, y, _, _] = build_frame
    if not y:
        return True
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    bases = list(filter(lambda f: is_base_frame(build_frame, f), relatives))
    print(bases, build_frame)
    if bases:
        return True
    return False


def inspect_install_beam(build_frame):
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    bases = list(filter(lambda f: is_base_frame(build_frame, f), relatives))
    base_pillar = list(filter(lambda f: not f[2], bases))
    base_beam = list(filter(lambda f: f[2], bases))
    if bases and (base_pillar or len(base_beam) == 2):
        return True
    return False


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


def solution(n, build_frame):
    list(map(build, build_frame))
    return sorted(answer, key=lambda f: (f[0], f[1], f[2]))


print(
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
)

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
