# 이웃한 칸

def solution(board, h, w):
    answer = 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    target = board[h][w]

    for i in range(4):
        h_direction = h + dy[i]
        w_direction = w + dx[i]

        if len(board) > h_direction >= 0 and len(board[0]) > w_direction >= 0 :
            if board[h_direction][w_direction] == target:
                answer += 1

    return answer

print(solution([["blue", "red", "orange", "red"], 
                ["red", "red", "blue", "orange"], 
                ["blue", "orange", "red", "red"], 
                ["orange", "orange", "red", "blue"]],1,1))