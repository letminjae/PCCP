# 마법의 엘리베이터

def solution(storey):
    count = 0
    
    while storey > 0:
        digit = storey % 10

        if digit < 5: # 1~4 일 때는 빼는게 유리
            count += digit
        elif digit > 5: # 6~9 일 때는 올리는게 유리
            count += (10 - digit)
            storey += 10
        else: # 5일 때는 다음 숫자보고 결정
            if (storey // 10) % 10 >= 5: # 5이상이면 자릿수 올림
                storey += 10
            count += 5
        
        storey //= 10

    return count

solution(2554) # 16