students=[
    {"name": "小王", "score": 85},
    {"name": "小李", "score": 92},
    {"name": "小张", "score": 78},
]
def print_all(students):
    for s in students:
        print(f"{s['name']}: {s['score']}")
def average(students):
    total =0
    for s in students:
        total = total + s["score"]
    avg =total / len(students)
    return int(avg * 10 +0.5)/10
def add_student(students, name, score):
    students.append({"name": name, "score": score})
add_student(students, "小赵", 66)
print_all(students)
print(f"平均分: {average(students)}")
top = students[0]
for s in students:
    if s["score"]>top["score"]:
        top =s
print(f"最高分: {top['name']}（{top['score']} 分）")