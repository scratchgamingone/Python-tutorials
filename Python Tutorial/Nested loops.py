#nested loop = A loop within another loop(Outer, inner)
#              outer loop:
#                inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = (input("Enter the # of symbols: "))

for x in range(rows):
  for y in range(columns):
    print(symbol, end =" ")
  print()