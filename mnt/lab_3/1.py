# Stosując metodę eliminacji Gaussa oraz metodę Cramera rozwiązać podany układ równań liniowych w analogiczny sposób jak w przykładzie 1 i przykładzie 2:
# 10𝑥1 + 40𝑥2 + 70𝑥3 = 300
# 20𝑥1 + 50𝑥2 + 80𝑥3 = 360
# 30𝑥1 + 60𝑥2 + 80𝑥3 = 390
# Rozwiązanie: x1 = 1, x2 = 2, x3 = 3.
# Uwaga: Obliczenia należy przeprowadzić odręcznie i wysłać kopie jako załącznik do sprawozdania.

# Tworzymy macierz z równań
A = [[10, 40, 70],
     [20, 50, 80],
     [30, 60, 80]]

# Tworzymy wektor wyników
B = [300, 360, 390]


def print_Gauss(A, B):
    # Wykonujemy operacje na macierzy, tak aby otrzymać macierz trójkątną górną
    for i in range(len(A)):
        # Zapobiegamy dzieleniu przez zero
        if A[i][i] == 0:
            print("Dzielenie przez zero!")
            break
        for j in range(i+1, len(A)):
            # Współczynnik, który anuluje wartość elementu pod przekątną
            wsp = A[j][i] / A[i][i]
            for k in range(i, len(A)):
                A[j][k] = A[j][k] - wsp * A[i][k]
            # Odpowiednio zmieniamy wartości wektora wyników
            B[j] = B[j] - wsp * B[i]

    # Wyliczamy wartości niewiadomych
    X = [0 for i in range(len(A))]
    for i in range(len(A)-1, -1, -1):
        suma = 0
        for j in range(i+1, len(A)):
            suma += A[i][j] * X[j]
        X[i] = (B[i] - suma) / A[i][i]

    # Wyświetlamy wyniki
    print(f"x1 = {X[0]}, x2 = {X[1]}, x3 = {X[2]}")


def print_Cramer(A, B):
    # Funkcja zwracająca wartość wyznacznika macierzy
    def det(M):
        if len(M) == 1:
            return M[0][0]
        elif len(M) == 2:
            return M[0][0]*M[1][1] - M[0][1]*M[1][0]
        else:
            suma = 0
            for j in range(len(M)):
                wsp = (-1) ** j
                suma += wsp * M[0][j] * \
                    det([M[i][0:j]+M[i][j+1:] for i in range(1, len(M))])
            return suma

    # Wyliczamy wartości niewiadomych
    X = []
    for i in range(len(A)):
        # Tworzymy nową macierz i zastępujemy kolumnę i-tego indeksu wektorem wyników
        temp = [[A[j][k] if k != i else B[j]
                for k in range(len(A))] for j in range(len(A))]
        # Wyznaczamy wyznacznik macierzy
        d = det(temp)
        # Wyznaczamy wartość i-tej niewiadomej
        X.append(d / det(A))

    # Wyświetlamy wyniki
    print(f"x1 = {X[0]}, x2 = {X[1]}, x3 = {X[2]}")


print("Metoda Gaussa:")
print_Gauss(A, B)
print("Metoda Cramera:")
print_Cramer(A, B)
