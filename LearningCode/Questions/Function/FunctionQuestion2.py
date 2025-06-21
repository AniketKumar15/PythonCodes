c = float(input("Enter celsius value: "))

def celsiusToFahrenheit(celsius):
    f = (celsius * 9/5) + 32
    return f

res = celsiusToFahrenheit(c)
print(f"{c}°C = {round(res, 2)}°F")