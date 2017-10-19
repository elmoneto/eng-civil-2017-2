#Exercício 8
#Faça um programa que leia n e mostre os n termos e o valor da soma da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

n = int(input('Informe o valor de n: '))
termos = '1/1'
num = 1
den = 1
for i in range (1, n):
   num = num + 1
   den = den + 2
   termos = termos + ' + ' + str(num) + '/' + str(den)
print(termos)
