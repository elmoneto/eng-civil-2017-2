#Exercício 7
#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário.

numTabuada = int(input('Informe o número da tabuada: '))
valorInicial = int(input('Informe o valor inicial: '))
valorFinal = int(input('Informe o valor final: '))
for i in range(valorInicial, valorFinal+1):
   print(str(numTabuada) + ' x ' + str(i) + ' = ' + str(numTabuada*i))
