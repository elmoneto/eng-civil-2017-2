#Exercício 3
#Escreva um programa que identifique se o número digitado pelo usuário é par ou impar.

numero = int(input('Informe um número inteiro: '))
if numero % 2 == 0:
   print('O número ' + str(numero) + ' é par.')
else:
   print('O numero ' + str(numero) + ' é ímpar.')
   
#Operador % retorna o resto da divisão, não o quociente
#12 % 5 = 2
#7 % 4 = 3
#8 % 2 = 0
