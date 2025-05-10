# 둘만의 암호

def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alphabet = alphabet.replace(i, "")

    for char in s:
        answer += alphabet[(alphabet.find(char) + index) % len(alphabet)]
   
    return answer