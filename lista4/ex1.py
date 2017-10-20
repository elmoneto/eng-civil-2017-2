#Faça um programa que leia o tamanho de uma lista, os elementos da lista, e por fim, um código. Se o código for 1, mostrar o vetor na ordem direta, se o código for 2, mostrar o vetor na ordem inversa.

lista = []
tamanhoLista = int(input('Informe o tamanho da lista: '))

for i in range (0, tamanhoLista):
   num = int(input('Informe um número: '))
   lista.append(num)

opcao = input('Deseja ver a lista em ordem direta(1) ou inversa(2)? ')
if(opcao == '1'):
   print(lista)
elif(opcao == '2'):
   lista.reverse()
   print(lista)
else:
   print('Opção inválida')

