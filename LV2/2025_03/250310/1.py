def solution(m, n, board):
    board = [list(row) for row in board] # 문자열 리스트를 2차원 리스트로 변환

    while True:
        deleted_block = set()
        # 없어지는 블록 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != " " and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    deleted_block.update({(i,j), (i+1,j), (i,j+1), (i+1,j+1)})

        if not deleted_block:
            break
        
        # 블록 삭제하기
        for i, j in deleted_block:
            board[i][j] = " "

        # 중력 적용
        for j in range(n):
            #블록 모으기
            stack = [board[i][j] for i in range(m) if board[i][j] != " "]
            for i in range(m - len(stack)):
                board[i][j] = " " # 빈 공간 채우기
            for i in range(len(stack)):
                board[m - len(stack)+ i][j] = stack[i] # 블록 떨어짐

    print(board)
        
    return sum(row.count(" ") for row in board)