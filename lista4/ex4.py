#Exercício 4
#Escreva um programa que leia o número de elementos e os valores (inteiros) de uma lista. O programa deve mostrar o número de valores pares existentes no vetor.

lista = []
qtdePares = 0

numElementos = int(input('Informe o número de elementos da lista: '))

for i in range(0,numElementos):
   lista.append(int(input('Informe um número: ')))
   
for i in lista:
   if i % 2 == 0:
      qtdePares += 1

print('Quantidade de números pares: ' + str(qtdePares))
