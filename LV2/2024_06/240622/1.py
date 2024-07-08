# 구명보트

def solution(people, limit):
    answer = 0
    x = 0 # people의 첫번째
    y = len(people) - 1 # people의 끝번째
    people.sort()
    
    while x < y:
        if people[y] + people[x] <= limit:
            x += 1
            answer += 1
        y -= 1
    return len(people) - answer

print(solution([70, 50, 80, 50],100))