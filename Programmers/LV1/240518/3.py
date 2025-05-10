# 하샤드 수

def solution(x):
    add = sum([int(i) for i in list(str(x))])
    return True if x % add == 0 else False