# 10798 세로읽기

A = []
answer = []

for _ in range(5):
    A.append(list(input()))

max_len = max(len(row) for row in A)

for i in range(5):
    while len(A[i]) < max_len:
        A[i].append(" ")

for i in range(max_len):
    for j in range(5):
        answer.append(A[j][i])

answer = ''.join(answer).replace(" ", "")
print(answer)