#Exercício 2
#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por código:
#1, 2, 3, 4 -> voto para os respectivos candidatos;
#5 -> voto nulo;
#6 -> voto branco.
#O algoritmo deve contar o total de votos para cada candidato e o total de votos brancos e nulos.
#Para finalizar a votação, o mesário deverá informar o valor 0 (zero)

voto = 1 #comeca com qualquer valor != 0 para garantir que o laço seja executado pelo menos uma vez
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
nulos = 0
brancos = 0

while(voto != 0):
   voto = int(input("Informe o número do candidato, 5 (voto nulo), 6 (voto branco) ou 0 para fechar: "))
   if(voto !=0):
      if(voto == 1):
         cont1=cont1+1
      elif(voto == 2):
         cont2=cont2+1
      elif(voto == 3):
         cont3=cont3+1
      elif(voto == 4):
         cont4=cont4+1
      elif(voto == 5):
         nulos=nulos+1
      elif(voto == 6):
         brancos=brancos+1
      else:
         print("Opção inválida")
   else:
      print("Encerrando a entrada de dados...")
      
print("Total de votos no candidato 1: " + str(cont1))
print("Total de votos no candidato 2: " + str(cont2))
print("Total de votos no candidato 3: " + str(cont3))
print("Total de votos no candidato 4: " + str(cont4))
print("Total de votos nulos: " + str(nulos))
print("Total de votos brancos: " + str(brancos))
print("Total de votos: " + str(cont1+cont2+cont3+cont4+nulos+brancos))

