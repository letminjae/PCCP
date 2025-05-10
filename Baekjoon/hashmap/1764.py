# 1764 듣보잡

N, M = map(int, input().split())

A = set(input() for _ in range(N))
B = set(input() for _ in range(M))

sorted_list = sorted(A-(A-B))
print(len(sorted_list))
for word in sorted_list:
    print(word)