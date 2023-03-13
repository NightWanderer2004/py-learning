# Napisz program proszący użytkownika o podanie dwóch liczb a, b i wypisujący ich sumę, różnicę, iloczyn, iloraz, √𝑎 + 𝑏 oraz 𝑎𝑏

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

sum = a + b
print("Suma: " + str(sum))

min = a - b
print("Różnica: " + str(min))

mul = a * b
print("Iloczyn: " + str(mul))

div = a / b
print("Iloraz: " + str(div))

root = (a ** 0.5) + (b ** 0.5)
print("√𝑎 + 𝑏: " + str(root))

ab = a ** b
print("𝑎𝑏: " + str(ab))
