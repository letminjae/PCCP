# 모음사전

# DFS

vowels = ['A', 'E', 'I', 'O', 'U']
idx = -1
answer = 0
   
def solution(word):
    def dfs(cnt, s):
        global answer, idx
        if cnt <= 5:
            idx += 1
            if s == word:
                answer = idx
        else:
            return
        for i in range(5):
            dfs(cnt + 1, s+vowels[i])
    dfs(0,'')
    return answer