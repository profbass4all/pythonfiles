class Vehicle():
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def displayInfo(self):
        return f'The name of this vehicle is {self.name} and was made in the year {self.year}'
    
    def max_speed(self):
        print('My max_speed is 24km/hr')

volvo = Vehicle('volvo', '2003')

#volvo.max_speed()

class BMW(Vehicle):
    def max_speed(self):
        print('My max speed is 5000km/hr')
bmw = BMW('bmw2024', 2024)
def carDetails(obj):
    obj.max_speed()

#carDetails(bmw)
#carDetails(volvo)

for x in (volvo, bmw):
    x.max_speed()

def volume(a, b = 0, c = 0):
    if(b > 0 and c > 0):
        return a*b*c
    elif(b > 0):
        return a * b *a
    else:
        return a*a*a
    
vol_3 = volume(2,3,4)
print('volume of a 3sides:', vol_3 )

vol_2 = volume(2, 3)
print('volume of a 2sides:', vol_2 )

vol_1 = volume(2)
print('volume of a 1side:', vol_1 )

class Student:
    def __init__(self, name, grade, department):
        self.name = name
        self.__grade = grade
        self.__department = department
    def show(self):
        print(f'My name is {self.name} and I am in grade {self.__grade} in {self.__department} department')
    def set_grade(self, num):
        self.__grade = num
    def get_grade(self):
        return self.__grade
Aisha = Student('aisha', 12, 'science')
A = Student('aisha', 12, 'science')
B = Student('aisha', 12, 'science')
print(id(A))
print(id(B))
Aisha.set_grade(56)

print(Aisha.get_grade())
Aisha.show()