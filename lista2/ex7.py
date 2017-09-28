#Exercício 7
#Faça um algoritmo que leia 3 números inteiros e imprima o menor deles. 

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

menor = num1;
if(num2 < menor):
   menor = num2
if(num3 < menor):
   menor = num3
   
print('O menor número é ' + str(menor))
