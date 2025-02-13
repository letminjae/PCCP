# 의상

def solution(clothes):
    d = {}
    for name, wear in clothes:
        if wear in d.keys():
            d[wear] += [name]
        else:
            d[wear] = [name]
        print(d)
        
    answer = 1
    for key, value in d.items():
        answer *= (len(value) + 1)
    # 아무것도 입지 않는 경우가 있으니 -1 한다
    return answer - 1

print(solution([["yellow_hat","headgear"],["blue_sunglasses","eyewear"],["green_turban","headgear"]]))