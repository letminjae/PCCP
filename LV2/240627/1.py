# 귤 고르기

def solution(k, tangerine):
    answer = 0
    d = {}
    for i in tangerine:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

    for i in d:
        if k <= 0:
            return answer
        k -= d[i]
        answer += 1

    return answer

# 콜렉션 사용
import collections
def solution1(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        print(v)
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer
       
print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))