# 2566 최댓값

A = []

for _ in range(9):
    A.append(list(map(int, input().split())))

max_number = 0
idx_i = 0
idx_j = 0

for i in range(9):
    for j in range(9):
        if max_number < A[i][j]:
            max_number = A[i][j]
            idx_i = i
            idx_j = j

print(max_number)
print(f'{idx_i+1} {idx_j+1}')