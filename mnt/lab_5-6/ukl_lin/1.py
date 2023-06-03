def iteracja_prosta(A, b, x, iterations):
    n = len(x)
    for k in range(iterations):
        x_new = x.copy()
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x[j]
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new
    return x

# Dane wejściowe
A = [[4, -2, 1], [-2, 4, -2], [1, -2, 4]]
b = [11, -16, 17]
x = [0, 0, 0]  # Początkowe przybliżenie rozwiązania
iterations = 100  # Liczba iteracji

# Wywołanie funkcji do rozwiązania układu równań
solution = iteracja_prosta(A, b, x, iterations)

# Wyświetlenie wyniku
print("Rozwiązanie:")
print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])