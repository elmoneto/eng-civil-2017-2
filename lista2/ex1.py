#Exercício 1
#Ler 3 números do teclado e verificar se o primeiro é maior que a soma dos outros dois. 

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

if(num1 > num2 + num3):
   print('O número ' + str(num1) + ' é maior do que a soma de ' + str(num2) + ' e ' + str(num3))
else:
   print('O número ' + str(num1) + ' não é maior do que a soma de ' + str(num2) + ' e ' + str(num3))

