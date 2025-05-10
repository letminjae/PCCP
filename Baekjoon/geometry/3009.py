# 3009 네 번째 점

x_arr = []
y_arr = []
x4 = 0
y4 = 0

for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

for i in range(3):
    if x_arr.count(x_arr[i]) == 1:
        x4 = x_arr[i]
    if y_arr.count(y_arr[i]) == 1:
        y4 = y_arr[i]

print(x4, y4)