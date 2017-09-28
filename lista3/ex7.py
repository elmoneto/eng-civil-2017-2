#Exercício 7
#Ler 10 valores, um de cada vez, e contar quantos deles estão no intervalo [10,50] e quantos deles estão fora deste intervalo, imprimindo, ao final, estas informações.

qtdeDentro = 0
qtdeFora = 0

for i in range(0,10):
   number = int(input("Informe um numero: "))
   if(number >= 10 and number <= 50):
      qtdeDentro += 1
   else:
      qtdeFora += 1
      
print("Quantidade de numeros dentro do intervalo [10,50]: " + str(qtdeDentro))
print("Quantidade de numeros fora do intervalo [10,50]: " + str(qtdeFora))
