# 1181 단어정렬

N = int(input())

arr = list(set([input() for _ in range(N)]))

arr.sort()
arr.sort(key=lambda x:len(x))

for word in arr:
    print(word)