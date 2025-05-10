# 단어 변환

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque([(begin, 0)])

    while q:
        current, count = q.popleft()
        if current == target:
            return count
        for word in words:
            # 한글자만 다른 단어 탐색
            if sum([x != y for x, y in zip(current, word)]) == 1:
                q.append((word, count+1))
                words.remove(word) # visit 했기에, 다시 방문하지 않도록 삭제
    return 0

solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"] ) # 4