# banned id 패턴과 일치하는 모든 user id 찾기
def is_matched(pattern, user_id):
    # 1. 두 문자열의 길이 비교
    if len(pattern) != len(user_id):
        return False
    
    # 2. 문자열 순회
    for i in range(len(pattern)):
        if pattern[i] == "*":
            continue
        elif pattern[i] != user_id[i]:
            return False
    
    return True

def solution(user_id, banned_id):
    
    # 재귀로 모든 경우의 수 구하기
    def dfs(banned_id_index):
        
        # banned id 다 돌았으면 answer에 tuple 형태로 저장
        if banned_id_index == len(banned_id):
            temp_list = []
            
            for i in range(len(visited)):
                if visited[i] == True:
                    temp_list.append(user_id[i])
            
            answer.add(tuple(temp_list))
            return
        
        # 현재 패턴과 일치하는 user_id 찾기
        for i in range(len(user_id)):
            
            # 이미 방문(사용)했는지 and 조건에 맞는지
            if not visited[i] and is_matched(banned_id[banned_id_index], user_id[i]):
                visited[i] = True
                dfs(banned_id_index + 1)
                visited[i] = False
    
    answer = set()
    visited = [False] * len(user_id)
    
    dfs(0)
    
    return len(answer)
    
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])