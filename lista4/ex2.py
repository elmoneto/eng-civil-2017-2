#Exercício 2
#Sejam A e B duas listas contendo 10 elementos inteiros (podem ser definidos diretamente no código do programa). O programa deve:
#1. Calcular a soma dos elementos de A.
#2. Calcular a soma dos elementos de B.
#3. Criar a lista C, que é a soma das listas A e B.
#4. Obter a lista D, subtraindo B de A.
#5. Obter o produto escalar de A por B, isto é, A[0]*B[0] + A[1]*B[1] + .......+ A[N-1]*B[N-1].

listaA = [-1,0,3,6,9,2,4,6,5,7]
listaB = [0,3,0,7,11,0,4,10,1,1]
somaListaA = 0
somaListaB = 0
listaC = []
listaD = []
prodEscalar = 0

#Soma dos elementos da lista A
for i in listaA:
   somaListaA = somaListaA + i
print('Soma dos elementos da lista A: ' + str(somaListaA))

#Soma dos elementos da lista B
for i in listaB:
   somaListaB = somaListaB + i
print('Soma dos elementos da lista B: ' + str(somaListaB))

#Lista C com soma de A[n] + B[n]
for i in range(0,10):
   listaC.append(listaA[i] + listaB[i])
print('\nSoma da lista A com lista B')
print(listaC)

#Lista D com subtração de A[n] * B[n]
for i in range(0,10):
   listaD.append(listaB[i] - listaA[i])
print('\nDiferença da lista B menos a lista A')
print(listaD)

#Produto Escalar
for i in range(0,10):
   prodEscalar = prodEscalar + (listaA[i] * listaB[i])
print('\nProduto escalar: ' + str(prodEscalar))
