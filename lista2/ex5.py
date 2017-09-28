#Exercício 5
#Ler 2 números do teclado. Se o segundo for diferente de zero, calcular e imprimir o quociente do primeiro pelo segundo. Caso contrário, imprimir a mensagem: “DIVISÃO POR ZERO”. 

num1 = float(input('Informe o primeiro número (dividendo): '))
num2 = float(input('Informe o segundo número (divisor): '))
if(num2 != 0):
   print('Resultado = ' + str(num1/num2))
else:
   print('Divisão por zero')
