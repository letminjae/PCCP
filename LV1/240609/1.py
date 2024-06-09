# 달리기 경주

# 시간초과
# def solution(players, callings):
#     for call in callings:
#         i = players[players.index(call)]
#         players[i-1], players[i] = players[i], players[i-1]
#     return players

def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}
    for who in callings:
        idx = result[who]
        result[who] -= 1
        result[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))