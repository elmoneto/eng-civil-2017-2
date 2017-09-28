#Exercício 1
#Modifique o algoritmo que lê dois números reais e um caractere dentre: '+', '-', '*' ou '/'. O algoritmo deverá ficar calculando (em loop) até que o usuário digite 'q' na operação

op = '+'
while (op != 'q'):
   op = input('Informe a operacao desejada (+ - * /): ')
   if( op != 'q'):
      num1 = float(input('Informe o primeiro numero: '))
      num2 = float(input('Informe o segundo numero: '))
      if(op == '+'):
         print('Resultado = ' + str(num1+num2))
      elif(op == '-'):
         print('Resultado = ' + str(num1-num2))
      elif(op == '*'):
         print('Resultado = ' + str(num1*num2))
      elif(op == '/'):
         if(num2 != 0):
            print('Resultado = ' + str(num1/num2))
         else:
            print('Divisão por zero')
      else:
         print("Operação desconhecida")
   else:
      print('Programa encerrado')
        
       


