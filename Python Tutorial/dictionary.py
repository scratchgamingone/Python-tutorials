# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplictates
capitals = { "USA": "Washington D.C.",
             "India" : "New Delhi",
             "China" : "Beijing",
             "Russia" : "Moscow"}

#print(dir(capitals))
#print(hep(capitals))
#print(capitals.get("Japan))

if capitals.get("Russia"):
    print(" That capital exists")
else:
    print(" That capital doesn't exist")