#Exercício 3
#Faça um programa que leia 10 números e, ao final da execução, diga qual foi o maior número digitado

maior = -99999999 #valor bem baixo para garantir que o primeiro número digitado pelo usuário vai ser maior
for i in range(1,11):
   number = int(input("Informe o " + str(i) + "o numero: "))
   if (number > maior):
      maior = number
print("O maior numero é " + str(maior))
   
