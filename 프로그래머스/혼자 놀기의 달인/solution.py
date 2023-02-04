def case(start, cards):
    open_cards = []

    def pick(cur):
        nex = cards[cur - 1]
        if nex == cur:
            open_cards.append(nex)
            return
        if nex in open_cards:
            return
        open_cards.append(nex)
        return pick(nex)

    pick(start)
    return "-".join(list(map(str, sorted(open_cards))))


def solution(cards):
    cases = map(lambda s: case(s, cards), cards)
    largest = sorted(list(set(cases)), key=lambda c: -len(c.split("-")))
    if len(largest) < 2:
        return 0
    answer = len(largest[0].split("-")) * len(largest[1].split("-"))
    print(answer)
    return answer
