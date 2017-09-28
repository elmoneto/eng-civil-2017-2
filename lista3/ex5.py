#Exercício 5
#Calcular o fatorial de um número qualquer. Ex.: 5! = 5*4*3*2*1

produtorio = 1
number = int(input("Informe o numero para calcular o fatorial: "))
for i in range(1,number+1):
   produtorio = produtorio*i
print("O fatorial de " + str(number) + " é " + str(produtorio))
