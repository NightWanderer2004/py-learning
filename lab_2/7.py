# (FizzBuzz) Napisz program, w którym użytkownik podaje kilka razy liczby całkowitą. Jeśli użytkownik poda liczbę podzielną przez 3, to wypisz na ekranie słowo „Fizz”, natomiast gdy poda liczbę podzielną przez 5, wypisz słowo „Buzz”. W przypadku liczb podzielnych zarówno przez 3 i 5, wypisz słowo „FizzBuzz”

a = int(input("Podaj liczbę: "))

if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
