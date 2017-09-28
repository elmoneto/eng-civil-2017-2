#Exercício 8
#Leia quatro valores reais, faça um programa que: 
#a) Imprima os valores negativos. 
#b) Calcule e imprima a média dos valores positivos. 

somatorio = 0 #variável que acumula o valor de cada valor positivo
qtdePositivos = 0 #variável que armazena a quantidade de valores positivos

num1 = float(input('Informe o 1o número: '))
if num1 < 0:
   print('O número é negativo.')
elif num1 > 0:
   somatorio = somatorio + num1 #o número > zero? então soma número ao valor que já estava em somatorio e atribui a soma de volta à variável
   qtdePositivos += 1 #aumenta em uma unidade a quantidade de números positivos

num2 = float(input('Informe o 2o número: '))
if num2 < 0:
   print('O número é negativo.')
elif num2 > 0:
   somatorio = somatorio + num2
   qtdePositivos += 1

num3 = float(input('Informe o 3o número: '))
if num3 < 0:
   print('O número é negativo.')
elif num3 > 0:
   somatorio = somatorio + num3
   qtdePositivos += 1

num4 = float(input('Informe o 4o número: '))
if num4 < 0:
   print('O número é negativo.')
elif num4 > 0:
   somatorio = somatorio + num4
   qtdePositivos += 1

if(qtdePositivos > 0):
   print('Media dos números positivos: ' + str(somatorio/qtdePositivos))
