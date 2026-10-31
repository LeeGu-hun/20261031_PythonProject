from tkinter import simpledialog

month = simpledialog.askinteger(title="당신이 태어난 달은?", prompt="월: ")
result = ''
if month == 12:
    result = "겨울"
elif month <= 11 and month>=9:
    result = "가을"
elif month <= 8 and month>=6:
    result = "여름"
elif month <= 3 and month>=5:
    result = "봄"
else:
    result = "겨울"
print(result)

grade = "학점 \"A\" "
print(grade)
score = simpledialog.askinteger(title="점수 입력", prompt="점수를 입력하세요")
print(score)

# 중첩 if :: 좋은 코드는 아님
if score >= 90:
    grade = "A"
    if score % 10 > 5:
        grade = "+"
    elif score % 10 <= 5 :
        grade = "-"
elif score >= 80:
    grade = "B"
    if score % 10 > 5:
        grade = "+"
    elif score % 10 <= 5 :
        grade = "-"




