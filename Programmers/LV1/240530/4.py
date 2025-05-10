# 기사단원의 무기

# 시간초과
# def solution(number, limit, power):
#     measure = []
#     for i in range(1, number + 1):
#         count = 0
#         for j in range(1, number+1):
#             if i % j == 0:
#                 count += 1
#         measure.append(count)

#     for i in range(len(measure)):
#         if measure[i] > limit:
#             measure[i] = power

#     return sum(measure)

# 시간초과 개선
def solution(number, limit, power):
    measure = []
    # 약수
    for i in range(1, number+1):
        count = 0
        print(f'i={i}')
        for j in range(1, int(i**(1/2)) +1):
            print(f'j={j}')
            if i % j == 0:
                count += 1
                # j의 제곱이 i가 아니라면 = 더블!
                if j**2 != i:
                    count += 1
            print(f'count={count}')
            if count > limit:
                count = power
                break
        measure.append(count)

    return sum(measure)
   
           
print(solution(10, 3, 2))