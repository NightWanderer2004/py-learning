# Napisz konwerter jednostek temperatury, w którym użytkownik podaje wartość temperatury w stopniach Celsjusza, a program zwraca mu tą wartość w stopniach Kelwina oraz Fahrenheita.

def celsius_to_kelvin(celsius):
    return celsius + 273.15


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


cel = int(input("Enter temperature in Celsius:\n"))

print("Kelvin:", celsius_to_kelvin(cel))
print("Fahrenheit:", celsius_to_fahrenheit(cel))
