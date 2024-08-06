import json

students = [
    {"Name": "Joel", "Note": 1},
    {"Name": "Jan", "Note": 2},
    {"Name": "Tim", "Note": 3}
]

students_json = json.dumps(students, ensure_ascii=False, indent=4)

print(students_json)

with open('students.json', 'w', encoding='utf-8') as file:
    file.write(students_json)
