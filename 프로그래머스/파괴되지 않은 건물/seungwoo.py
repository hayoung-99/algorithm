buildingMap = {}


def getBoardKeys(r1, c1, r2, c2):
    return ["-".join(map(str, [x, y])) for x in range(r1, r2 + 1) for y in range(c1, c2 + 1)]


def init(board):
    for r, b1 in enumerate(board):
        for c, b2 in enumerate(b1):
            key = "-".join((map(str, [r, c])))
            buildingMap[key] = b2


def singleEffect(key, value, skillType):
    buildingMap[key] = buildingMap[key] + value * (1 if skillType == 2 else -1)


def skillEffect(skill):
    [skillType, r1, c1, r2, c2, degree] = skill
    keys = getBoardKeys(r1, c1, r2, c2)
    list(map(lambda k: singleEffect(k, degree, skillType), keys))


def solution(board, skill):
    init(board)
    list(map(skillEffect, skill))
    answer = len(list(filter(lambda x: x >= 1, buildingMap.values())))
    return answer


x = solution(
    [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
    [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]],
)

print(x)
