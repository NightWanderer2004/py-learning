# Napisz program zwracający n-ty wyraz ciągu Fibonacciego

terms = int(input("Podaj ilość iteracij ciągu Fibonacci: "))


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fib(num - 2) + fib(num - 1))


for i in range(0, terms):
    print(fib(i + 1))
