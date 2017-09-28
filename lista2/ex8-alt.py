#Exercício 8 (alternativa) - mostra todos os números negativos de uma vez só no final da execução
#Leia quatro valores reais, faça um programa que: 
#a) Imprima os valores negativos. 
#b) Calcule e imprima a média dos valores positivos. 

somatorio = 0 #variável que acumula o valor de cada valor positivo
qtdePositivos = 0 #variável que armazena a quantidade de valores positivos
negativos = '' #declaração de uma string vazia

num1 = float(input('Informe o 1o número: '))
if num1 < 0:
   negativos = negativos + ' ' + str(num1) #concatena o número atual com o que já existe na string
elif num1 > 0:
   somatorio = somatorio + num1
   qtdePositivos += 1

num2 = float(input('Informe o 2o número: '))
if num2 < 0:
   negativos = negativos + ' ' + str(num2)
elif num2 > 0:
   somatorio = somatorio + num2
   qtdePositivos += 1

num3 = float(input('Informe o 3o número: '))
if num3 < 0:
   negativos = negativos + ' ' + str(num3)
elif num3 > 0:
   somatorio = somatorio + num3
   qtdePositivos += 1

num4 = float(input('Informe o 4o número: '))
if num4 < 0:
   negativos = negativos + ' ' + str(num4)
elif num4 > 0:
   somatorio = somatorio + num4
   qtdePositivos += 1
   
print('Números negativos: ' + negativos)
if(qtdePositivos > 0): #se qtdePositivos for igual a zero, ocorre erro na operação abaixo
   print('Media dos números positivos: ' + str(somatorio/qtdePositivos))

#o operador + quando usado em cadeias de caracteres (strings) faz com que o início da segunda string seja ligado diretamente ao final da primeira
#Exemplo:
#texto1 = "Engenharia "
#texto2 = "Civil "
#texto3 = texto1 + texto2
#texto3 agora contém o texto "Engenharia Civil"
