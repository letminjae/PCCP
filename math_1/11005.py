# 11005 진법 변환 2

N, B = map(int,input().split())
answer = ''
string_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    answer += str(string_str[N % B])
    N //= B

print(answer[::-1])