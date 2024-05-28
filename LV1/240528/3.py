# 비밀지도

def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    
    for i in range(n):
        # 이진수 정제
        map1.append(bin(arr1[i])[2:])
        map2.append(bin(arr2[i])[2:])
        map1[i] = ('0' * (n - len(map1[i]))) + map1[i]
        map2[i] = ('0' * (n - len(map2[i]))) + map2[i]

        print(f'map1 = {map1}, map2 = {map2}')

        # 비밀지도 만들기
        tmp = ''
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                tmp += '#'
            elif map1[i][j] == '0' and map2[i][j] == '0':
                tmp += ' '
        answer.append(tmp)
                
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))