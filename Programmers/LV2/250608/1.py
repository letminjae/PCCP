# LV2 : 서버 증설 횟수

def solution(players, m, k):
    answer = 0
    size = len(players)
    servers = [0] * size
    
    def server_expand(needed_server, start_time):
        for i in range(k):
            if start_time + i < size:
                servers[start_time + i] += needed_server
    
    for time, player in enumerate(players):
        if player >= m:
            needed_server = (player // m) - servers[time]
            if needed_server > 0:
                server_expand(needed_server, time)
                answer += needed_server
    
    return answer
  
solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5)

# players : 시간마다 게임 접속한 사람 수
# m : 서버 1대가 감당가능한 사람 수
# k : 서버 1대를 운영할 수 있는 지속시간