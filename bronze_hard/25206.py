# 25206 너의 평점은

score = {
"A+":4.5,
"A0":4.0,
"B+":3.5,
"B0":3.0,
"C+":2.5,
"C0":2.0,
"D+":1.5,
"D0":1.0,
"F":0.0,
}

grade_sum = 0
credit_sum = 0

for _ in range(20):
    name, credit, grade = input().split()
    credit = float(credit)
    if grade == "P":
        continue
    else:
        grade_sum += credit * float(score[grade])
        credit_sum += credit

average = grade_sum / credit_sum
print(f'{average:.6f}')