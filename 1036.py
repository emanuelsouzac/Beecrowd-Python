valores = input()

valores = valores.split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = (b**2) - 4*a*c

if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    r1 = (-b + delta**0.5) / (2 * a)
    r2 = (-b - delta**0.5) / (2 * a)
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}') # Uso da f-string disponível a partir do Python 3.6