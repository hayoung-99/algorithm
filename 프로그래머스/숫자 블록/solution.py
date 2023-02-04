def solution(begin, end):
    block_table = {1: 0}

    def block(num):
        counts = int(end / num)
        list(map(lambda q: block_table.update({q * num: num}), range(2, counts + 1)))

    list(map(block, range(1, end + 1)))
    answer = list(
        map(lambda i: i[1], filter(lambda i: i[0] >= begin, block_table.items()))
    )
    return answer


print(solution(1, 10))
