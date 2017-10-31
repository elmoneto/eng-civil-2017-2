#Exercício 7
#Faça um programa para calcular o valor da função f(x)=a 0 +a 1 x+a 2 x 2 +...+a n x n .
#São informações de entrada os valores de n (grau da função) e dos coeficientes a0 , a1 , ..., a n.
#Após estes dados serem informados, o usuário poderá digitar valores para x.
#O programa deve calcular e imprimir na tela o resultado da função.
#O programa se encerra quando o usuário informar 0 para o valor de x.

listaCoeficientes = []
x = 1

n = int(input("Informe o grau do polinômio: "))
   
for i in range(0,n+1):
   c = int(input("Informe o valor do coeficiente a" + str(i) + ": "))
   listaCoeficientes.append(c)

while(x != 0):
   x = int(input("Informe um valor para a varíavel x: "))
   
   if(x == 0):
      break
      
   result = 0
   for i in range(0,n+1):
      result = result + (listaCoeficientes[i] * x**i)
   print(result)

   

   

