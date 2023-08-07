class Student:
    def __init__(self, name, age, s_id):
        self.__student_id = s_id
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age


s1 = Student('Karo', 18, 1001)

print(s1.name)