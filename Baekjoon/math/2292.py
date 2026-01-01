# 2292 벌집

N = int(input())

bee = 1
count = 1

while N > bee:
    bee += 6 * count
    count += 1
print(count)