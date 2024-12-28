
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "fish", "turkey"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
print("----------------------")

print(groceries)
print(groceries[1][0])
print("----------------------")
for collection in groceries:
    print(collection)
