s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for alpha in alphabet:
    if alpha in s:
        print(s.index(alpha), end=' ')
    else:
        print(-1, end=' ')