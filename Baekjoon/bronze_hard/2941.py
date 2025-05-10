# 2941 크로아티아 알파벳

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

str = input()

for cro in croatia:
    if cro in str:
        str = str.replace(cro, " ")

print(len(str))