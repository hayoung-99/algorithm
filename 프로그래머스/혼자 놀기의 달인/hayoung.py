def get_group(group, open_list, box):
    # 다음에 열 박스가 이미 열렸다면: 그룹(리스트)를 return
    if box in open_list:
        return open_list

    # 다음에 열 박스가 아직 있다면: 그룹(리스트)에 추가하고 재귀
    open_list.append(box)
    next_idx = box[1]

    for i in range(len(group)):
        if group[i][0] == next_idx:
            next_box = group[i]
            return get_group(group, open_list, next_box)


def solution(cards):
    # all_cards = 남은 상자 리스트.
    # all_cards에서 get_group 재귀 함수를 통해 구한 그룹을 빼주면서(set 이용) 업데이트 <- 남은 상자가 없을 때까지
    # 구한 그룹들은 길이를 따로 리스트(len_groups)에 저장
    all_cards = [(i + 1, n) for i, n in enumerate(cards)]
    len_groups = []
    while len(all_cards) != 0:
        group = get_group(all_cards, [], all_cards[0])
        len_groups.append(len(group))
        all_cards = list(set(all_cards) - set(group))

    # 최댓값을 알기 위해 내림차순 정렬
    len_groups.sort(reverse=True)

    # 그룹이 1개: 0 return
    if len(len_groups) == 1:
        return 0

    # 그룹이 여러 개: 최댓값 2개를 곱한 값을 return
    return len_groups[0] * len_groups[1]
