#Exercício 5 (alternativa)
##Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

#Importação da biblioteca math do Python
#Facilita construção de operações matemáticas
#Fornece o número pi com várias casas decimais de precisão
import math

raio = float(input('Informe o raio do círculo: '))
area = math.pi * raio * raio #math.pi será substituído por 3.14159...
print('A área do círculo é ' + str(area) + ' u.a.')
