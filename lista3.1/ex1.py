#Exercício 1
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

num = -1
while num < 0 or num > 10:
   num = int(input('Informe um número entre 0 e 10: '))
   if num > 0 and num < 10:
      break
   print('O número é invalido')
print('O número informado foi: ' + str(num))
