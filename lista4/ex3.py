#Exercício 3
#Faça um programa que leia um vetor com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

lista = []
qtdeNegativos = 0
somaPositivos = 0

for i in range(0,10):
   lista.append(int(input('Informe um número: ')))

for i in lista:
   if i < 0:
      qtdeNegativos += 1
   else:
      somaPositivos = somaPositivos + i

print('Quantidade de números negativos: ' + str(qtdeNegativos))
print('Soma dos números positivos: ' + str(somaPositivos))
