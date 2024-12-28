# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Samuel Fei"
age = 25
gpa= 3.5
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print (gpa)

age = float(age)
print(age)

age = str(age)
print(age)
print(type(age))

age = str(age)
age+= "1"
print(age)

name = bool(name)
print(name)