def match(cell1, cell2, cell3, cell4):
    if cell1 != '0' and cell1 == cell2 == cell3 == cell4:
        return True
    return False


def boardify(board):
    for y in range(len(board[0])):
        cells = []
        for x in range(len(board)):
            if board[x][y] != '0':
                cells.append(board[x][y])
                
        result = ['0' for _ in range(len(board) - len(cells))] + cells
        for x in range(len(board)):
            board[x][y] = result[x]
            

def solution(m, n, board):
    for i, row in enumerate(board):
        board[i] = list(row)
    
    answer = 0
    while True:
        pos = set()
        for x in range(1, len(board)):
            for y in range(1, len(board[0])):
                if match(board[x][y], board[x-1][y], board[x][y-1], board[x-1][y-1]):
                    pos.update([(x, y), (x-1, y), (x, y-1), (x-1, y-1)])
                    
        # 지워진 셀은 '0'으로 설정
        for x, y in pos:
            board[x][y] = '0'
                    
        if not pos:
            break
        
        answer += len(pos)
        boardify(board)
    
    return answer