# 코드업 1254 : 알파벳 출력하기

a, b = input().split()
a = ord(a)
b = ord(b)

def main(a, b):
  for i in range(a, b+1):
    print(chr(i), end=' ')
  
main(a, b)