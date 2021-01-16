# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

F = int(input('Qual é a temperatura em graus Farenheit: '))

C = 5 * ((F-32) / 9)

print('A temperatura em graus Celsius é: ', format(C, '.0f'))
