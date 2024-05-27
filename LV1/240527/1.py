# 최소 직사각형

def solution(sizes):
    big = 0
    small = 0
    for i in sizes:
        if i[0] > i[1]:
            if (big < i[0]): big = i[0]
            if (small < i[1]): small = i[1]
        else:
            if (big < i[1]): big = i[1]
            if (small < i[0]): small = i[0]
    return big * small