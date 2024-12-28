#while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while  name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
else:
    print(f"Hello {name}")