# 경주로 건설 - 카카오 인턴 코딩테스트 문제

from heapq import heappop, heappush # 최소비용경로는 힙큐를 사용하는것이 유리
from sys import maxsize # 최소비용을 구하기 위해 초기값은 maxsize 사용

def solution(board):
    N = len(board)
    # 최소 비용이 드는 board
    min_cost_board = [[[maxsize] * N for _ in range(N)] for _ in range(4)] # 3차원 리스트를 만들어 방향에 따른 최소비용을 알아야함
    for i in range(4):
        min_cost_board[i][0][0] = 0 # 네 방향의 출발점 비용은 0으로 초기화, 3차원 인덱싱은 [방향][행][열]

    # BFS
    heap = [(0,0,0,0), (0,0,0,2)] # (이동비용, 출발지점, 출발방향(0 or 2)- 남쪽이나 동쪽으로만 갈수 있다)
    
    while heap:
        cost, x, y, d = heappop(heap)

        # 4방향 이동 - 동:0 서:1 남:2 북:3
        for dx, dy, dd in ((1,0,0),(-1,0,1),(0,1,2),(0,-1,3)): # dd가 방향이다
            nx, ny = x + dx, y + dy

            # 경계 / 벽일 때 - 경로 계산 하지 않음
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx]: continue

            # 현재경로(d)와 새로운경로(dd)가 같으면 100, 이나면 코너(600)
            new_cost = cost + (100 if d == dd else 600)

            # 최소비용 갱신
            if min_cost_board[dd][ny][nx] > new_cost:
                min_cost_board[dd][ny][nx] = new_cost
                heappush(heap, (new_cost, nx, ny, dd))
    
    return min(min_cost_board[0][N-1][N-1], min_cost_board[1][N-1][N-1], min_cost_board[2][N-1][N-1], min_cost_board[3][N-1][N-1])


solution([[0,0,0],[0,0,0],[0,0,0]]) # 900