def play_game(enemy, idx, k, soldiers):
    global answer

    if idx == 0:
        answer = 0

    if idx < len(enemy):
        # step 1) 무적권 쓰기
        if k > 0:
            play_game(enemy, idx + 1, k - 1, soldiers)

        # step 2) 병사가 enemy[idx] 이상이면 병사 소모
        if enemy[idx] <= soldiers:
            play_game(enemy, idx + 1, k, soldiers - enemy[idx])

        # step 3) 병사도 적고 무적권도 없는 경우
        if (k == 0) and (enemy[idx] > soldiers):
            if answer < idx:
                answer = idx

    else:
        answer = len(enemy)


def solution(n, k, enemy):
    play_game(enemy, 0, k, n)

    print(answer)

    return answer