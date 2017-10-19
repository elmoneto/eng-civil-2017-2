#Exercício 5
#Altere o programa anterior para mostrar no final a soma dos números.

soma = 0
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
for i in range(num1+1,num2):
   soma = soma + i
print('Soma = ' + str(soma))
