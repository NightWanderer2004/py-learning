h = int(input("Podaj wysokość: "))

for i in range(1, h+1):
    row = ""
    for j in range(i):
        row += str(i*(j+1)) + " "
    print(row)
