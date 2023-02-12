answer = []


def is_relative_frame(build_frame, installed_frame):
    [x, y, a] = build_frame[:3]
    [x1, y1, a1] = installed_frame[:3]
    if a and a1:
        return (x1 + 1 == x or x1 == x + 1) and y == y1
    elif a:
        return (x1 == x or x1 == x + 1) and (y == y1 or y == y1 + 1)
    elif a1:
        return (x1 == x or x1 + 1 == x) and (y + 1 == y1 or y == y1)
    return x1 == x and (y1 == y + 1 or y1 + 1 == y)


def is_base_frame(build_frame, installed_frame):
    [x, y, a] = build_frame[:3]
    [x1, y1, a1] = installed_frame[:3]
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
    if not build_frame[2] and not build_frame[1]:
        return True
    elif len(bases) == len(relatives):
        return True
    return False


def has_base_pillars(build_frame):
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    bases = list(filter(lambda f: is_base_frame(build_frame, f), relatives))
    base_pillars = list(filter(lambda f: not f[2], bases))
    return bool(base_pillars)


def inspect_remove_beam(build_frame):
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    beams = list(filter(lambda f: f[2], relatives))
    has_pillar_beams = list(filter(has_base_pillars, beams))
    bases = list(filter(lambda f: is_base_frame(build_frame, f), relatives))
    base_pillars = list(filter(lambda f: not f[2], bases))
    base_beams = list(filter(lambda f: f[2] and has_base_pillars(f), bases))
    failed_beams = list(filter(lambda f: f not in base_beams and f not in has_pillar_beams, beams))
    if failed_beams:
        return False
    elif len(relatives) == len(base_beams) + len(base_pillars):
        return True
    return False


def inspect_install_pillar(build_frame):
    [_, y] = build_frame[:2]
    if not y:
        return True
    relatives = list(filter(lambda f: is_relative_frame(build_frame, f), answer))
    bases = list(filter(lambda f: is_base_frame(build_frame, f), relatives))
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
