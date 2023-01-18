def solution(n, k, enemy):
    my_soldier = int(n)
    sum_func = lambda i: (i, sum(enemy[:i]))
    acc_enemy = list(map(sum_func, range(len(enemy))))
    sorted_acc_enemy = sorted(acc_enemy, key=lambda a: (a[1] - my_soldier, a[0]))
    filter_func = lambda a: a[1] - my_soldier >= 0
    filtered_acc_enemy = list(filter(filter_func, sorted_acc_enemy))
    if not filtered_acc_enemy:
        return len(enemy)
    non_skill_index, non_skill_enemy = filtered_acc_enemy[0]
    if not k:
        return non_skill_index
    print(non_skill_index, non_skill_enemy)
    answer = 0
    return answer
