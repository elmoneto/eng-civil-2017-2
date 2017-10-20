#Faça um programa que, primeiramente, leia um vetor com 15 posições. Em seguida, o programa deve calcular e imprimir na tela:
#1. O maior elemento do vetor e em que posição esse elemento se encontra;
#2. O menor elemento do vetor e em que posição esse elemento se encontra.

lista = []
maior = -1000000
menor = 1000000
posMaior = 0
posMenor = 0

for i in range(0,15):
   lista.append(int(input('Informe um número: ')))

for i in range(0,15):
   if(lista[i]>maior):
      maior = lista[i]
      posMaior = i
   if(lista[i]<menor):
      menor = lista[i]
      posMenor = i

print('Menor número é ' + str(menor) + ' na posição ' + str(posMenor))
print('Maior número é ' + str(maior) + ' na posição ' + str(posMaior))

      
