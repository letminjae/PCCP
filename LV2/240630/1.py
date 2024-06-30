# 할인 행사

from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n
    print(check)

    for i in range(len(discount)-9):
        count = Counter(discount[i:i+10])
        print(count)
        if count == check:
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],
               [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
               ))