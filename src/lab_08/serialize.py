import json
from src.lab_08.models import Student

students = [
    Student(fio="bdfyjd А.А.", birthdate="2003/04/13", group="су-3", gpa=4.0),
    Student(fio="иванов Б.Б.",   birthdate="2009/12/12", group="су-4", gpa=3.0),
    Student(fio="андреев В.В.", birthdate="2008/03/30", group="су-1", gpa=4.3),
    Student(fio="трешкин Г.Г.", birthdate="2006/08/11", group="су-2", gpa=5.0),
    Student(fio="сирнов Д.Д.", birthdate="2008/10/12", group="су-4", gpa=2.4)
]
def students_to_json(students, path):
    # data = dict.fromkeys(students, 'student')
    # data = {f'students_{i+1}': students[i] for i in range(len(students))}
    data = [s.to_dict() for s in students]
    # json.dumps(data, ensure_ascii=False, indent=2)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    with open(path, 'r', encoding="utf-8") as json_file:
        data_json = json.load(json_file)
    # data_dict = json.loads(data_json)
    # data = [i for i in data_dict.values()]
    return [Student.from_dict(d) for d in data_json]

if __name__ == '__main__':
    to = students_to_json(students,'data/lab_08/students_output.json')
    fromt = students_from_json('data/lab_08/students_input.json')
    for i in fromt:
        print(i)
