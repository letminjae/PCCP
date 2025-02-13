# 뉴스 클러스터링

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    # 다중 집합
    A, B = [], []
    for i in range(len(str1)-1):
        str = str1[i:i+2]
        if str.isalpha():
            A.append(str)
    for i in range(len(str2)-1):
        str = str2[i:i+2]
        if str.isalpha():
            B.append(str)

    # 자카드 유사도
    if len(A) == 0 and len(B) == 0:
        return 65536
    else:
        # 다중 합집합
        a_tmp = A.copy()
        a_result = A.copy()
        for word in B:
            if word not in a_tmp:
                a_result.append(word)
            else:
                a_tmp.remove(word)
        
        # 다중 교집합
        result = []
        for word in B:
            if word in A:
                A.remove(word)
                result.append(word)
        
        answer = len(result) / len(a_result)
    
    return int(answer*65536)

print(solution('FRANCE','french'))