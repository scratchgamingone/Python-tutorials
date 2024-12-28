# for loops = execute a block of code for a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1,11):
    print(x)
print("---------------------")

for x in range(1,11, 3 ):
    print(x)
print("---------------------")
for x in reversed(range(1,11)):
    print(x)
print("---------------------")

print("Happy NEW YEAR!")

print("---------------------")

credit_card = "1234-5678-9012-3456"

for card_number in credit_card:
    print(card_number)

print("---------------------")

for counter in range(1,21):
    if counter == 13:
        continue
    else:
        print(counter)