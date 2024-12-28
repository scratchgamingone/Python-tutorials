#while loop = execute some code WHILE some condition remains true

food = input("Enter a food you like(q to quit): ")

while not food ==  "q" :
    print(f"You like {food}  ")
    food = input("Enter another food you like (q to quit): ")

print("bye")W