#Exercício 6
#Ler dois números e um caractere dentre: '+', '-', '*' ou '/'. Após isto, calcular o resultado da operação desejada, respectivamente: soma, subtração, multiplicação ou divisão. 

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
op = input('Informe a operação (+ - * /): ')
if(op == '+'):
   print('Resultado = ' + str(num1 + num2))
elif(op == '-'):
   print('Resultado = ' + str(num1 - num2))
elif(op == '*'):
   print('Resultado = ' + str(num1 * num2))
elif(op == '/'):
   if(num2 !=0):
      print('Resultado = ' + str(num1 / num2))
   else:
      print('Divisão por zero.')
else:
   print('Operacao desconhecida')
 
