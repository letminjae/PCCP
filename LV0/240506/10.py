# 외계어 사전

def solution(spell, dic):
    spell.sort()
    for str in dic:
        if spell == sorted(list(str)): return 1
    return 2

print(solution(["p", "o", "s"],["sod", "eocd", "qixm", "adio", "soo"]))

# function solution(spell, dic) {
#     spell = spell.sort().join("")
#     return dic.map(a => a.split("").sort().join("")).find(a => a===spell) !== undefined ? 1 : 2
# }