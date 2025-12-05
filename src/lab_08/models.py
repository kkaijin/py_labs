from datetime import datetime, date
from dataclasses import dataclass

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            # (по-хорошему, тут должен быть raise ValueError(...))
            raise ValueError
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        b = datetime.strptime(self.birthdate, "%Y/%m/%d").date()
        today = date.today()
        year = 1
        if today.day < b.day and today.month >= b.month:
            year = 0
        return today.year - b.year - year

    def to_dict(self) -> dict:
        # TODO: проверить полноценность полей
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        # TODO: реализовать десереализацию из словаря

        return cls(fio=d["fio"],
                   birthdate=d["birthdate"],
                   group=d["group"],
                   gpa=float(d["gpa"]))

    def __str__(self):
        # TODO: f"{}, {}, {}"
        return f"Студент: {self.fio}, Группа: {self.group}, gpa: {self.gpa}"
    
if __name__ == '__main__':
    student1 = Student("IvanovII", '1999/11/05', 'se-01', 4.3)
    
    dic = {'fio': 'smirnovII', 'birthdate': '1925/12/20', 'group': 'gte-23', 'gpa': '3.2'}
    Student.from_dict(dic)
    print(student1.age())
    print(student1.to_dict())
    print(student1.__str__())