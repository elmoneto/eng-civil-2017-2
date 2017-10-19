#Exercício 8
#Ler um número e escrever se ele "é primo" ou "não é primo". Obs.: Números primos são divisíveis somente por 1 e por ele mesmo.

divisores = 0
number = int(input("Informe o numero: "))
for i in range(1,number+1):
   if(number % i == 0):
      divisores += 1
if(divisores <= 2):
   print("O numero é primo")
else:
   print("O numero não é primo")
      
