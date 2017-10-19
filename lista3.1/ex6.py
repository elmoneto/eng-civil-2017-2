#Exercício 6
#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

qtdePares = 0
qtdeImpares = 0
for i in range(0,10):
   num = int(input('Informe um número: '))
   if num % 2 == 0:
      qtdePares+=1
   else:
      qtdeImpares+=1
print('Quantidade de números pares: ' + str(qtdePares))
print('Quantidade de números ímpares: ' + str(qtdeImpares))
