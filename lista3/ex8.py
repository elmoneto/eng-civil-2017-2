#Exercício 8
#Ler um número e escrever se ele "é primo" ou "não é primo". Obs.: Números primos são divisíveis somente por 1 e por ele mesmo.

multiplos = 0
number = int(input("Informe o numero: "))
for i in range(1,number+1):
   if(number % i == 0):
      multiplos += 1
if(multiplos <= 2):
   print("O numero é primo")
else:
   print("O numero não é primo")
      
