#Dada uma seqüência de n números reais, determinar os números que compõem a seqüência e o número de vezes que cada um deles ocorre na mesma.
#Exemplo: n = 8
#Seqüência: -1.7, 3.0, 0.0, 1.5, 0.0, -1.7, 2.3, -1,7
#Saída:
#-1.7 ocorre 3 vezes
#3.0 ocorre 1 vez
#0.0 ocorre 2 vezes
#1.5 ocorre 1 vez
#2.3 ocorre 1 vez

lista = []
listaContabilizados = [] #armazena quais números que já foram contabilizados em rodadas anteriores
n = int(input('Informe o número de elementos da lista: '))

for i in range(0,n):
   lista.append(float(input('Informe um número: ')))

for i in range(0,n):
   if(lista[i] in listaContabilizados):
      continue #se número já foi contabilizado antes, pula para a próxima posição
   cont = 1
   for j in range(i+1,n):
      if(lista[i] == lista[j]):
         cont += 1
   listaContabilizados.append(lista[i]) #no final da contagem de aparições do número, o adiciona à lista de contabilizados
   print(str(lista[i]) + ' ocorre ' + str(cont) + 'x')
   
   
