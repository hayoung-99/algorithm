def get_group(group, open_list, box):
    # 다음에 열 박스가 이미 열렸다면
    if box in open_list:
        return open_list

    open_list.append(box)
    next_idx = box[1] - 1
    # open_list.append(group[next_idx])
    return get_group(group, open_list, group[next_idx])


def solution(cards):
    all_cards = [(i + 1, n) for i, n in enumerate(cards)]
    groups = []
    while len(all_cards) != 0:
        temp = get_group(all_cards, [], all_cards[0])

    temp2 = set(all_cards) - set(temp)
    print(temp2)
