# 1253

a,b = input().split()
a = int(a)
b = int(b)

def main(a, b):
  if a <= b:
    for i in range(a, b+1):
      print(i)
  else:
    for i in range(b, a+1):
      print(i)
      
main(a, b)