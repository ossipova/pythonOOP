# Home work 1
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Hello my mane is {self.fullname}, my age {self.age} and I'm {self.is_married}")


someone_person = Person('Jack', 30, 'not married')
someone_person.introduce_myself()


class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        return print(f'Average mark is {sum(self.marks.values()) // len(self.marks.values())}')


student = Student('Maria', 20, 'married', {'Math': 3, 'Chemistry': 5, 'English': 2})
print(
    f"Hello my mane is {student.fullname}, my age {student.age} and I'm {student.is_married} my marks {student.marks}")
student.average_mark()

class Teacher(Person):
    salary = 120000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
    def full_salary (self):
        if self.experience > 3:
            new_salary = (self.salary + (self.salary / 100 * 5) * (self.experience))
            return print('Salary in year = ',new_salary)
teacher = Teacher('Marina Pevrovna', 45, 'married', 8)
print(f"Hello my mane is {teacher.fullname}, my age {teacher.age} and I'm {teacher.is_married} my experience {teacher.experience} years")
teacher.full_salary()





            


        
        
