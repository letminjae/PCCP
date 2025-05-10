# 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for number in numbers:
        # 짝수일 때 항상 2진수는 0으로 끝남
        if number % 2 == 0:
            answer.append(number + 1)
        # 홀수일 때 : 가장 오른쪽 0을 1로 변경, 바로 뒤 1을 0으로 변경 -> 비트 2개 변경 ✅
        else:
          # 10진수 -> 2진수로 변환
          binary = list('0' + bin(number)[2:])
          # 오른쪽에서 가장 가까운 0의 위치
          index = ''.join(binary).rfind('0')
          binary[index] = '1' # 0 -> 1
          binary[index + 1] = '0' # 그 다음 비트를 0으로 변경
          # 다시 10진수 변환
          answer.append(int(''.join(binary), 2))

    return answer

solution([2,7]) # [3,11]