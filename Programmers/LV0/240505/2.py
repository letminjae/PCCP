# 영어가 싫어요

def solution(numbers):
    number = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i, num in enumerate(number):
        numbers = numbers.replace(num, str(i))
    return int(numbers)

print(solution("onetwothreefourfivesixseveneightnine"))