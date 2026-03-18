#15 - Área do Círculo Crie um programa que solicite ao usuário o raio de um círculo e
#calcule a sua circunferência. (utilize o math.pi):

import math

raio = float(input("Digite o raio: "))

resultado = raio**2 * (math.pi)

print(f"A area do circulo é: {resultado}")
