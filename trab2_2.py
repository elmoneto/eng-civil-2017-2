#Trabalho 2.2
#1. Informar nota mínima para aprovação, quantidade de avaliações e peso para cada uma delas
#2. Informar a quantidade de alunos
#3. Informar nome do aluno e sua nota em cada uma das avaliações
#4. Imprimir nome, média e status (aprov/reprov) de cada aluno

notaMinima = float(input("Informe a nota mínima para aprovação: "))
qtdeAvaliacoes = int(input("Informe a quantidade de avaliações: "))
listaPesos = []
somaPesos = 0

#DEFINICAO DE NUMERO DE ALUNOS; E DE QUANTIDADE E PESO DE AVALIAÇÕES
for i in range(0,qtdeAvaliacoes):
   peso = float(input("Informe o peso da " + str(i+1) + "a avaliacao: "))
   listaPesos.append(peso)
   somaPesos = somaPesos + peso
qtdeAlunos = int(input("Informe a quantidade de alunos: "))
listaNomes = []
listaMedias = []

#ENTRADA DE NOMES E NOTAS DE ALUNOS
for i in range(0,qtdeAlunos):
   somaNotas = 0
   nomeAluno = input("Nome do aluno: ")
   listaNomes.append(nomeAluno)
   for j in range(0,qtdeAvaliacoes):
      nota = float(input("Nota da " + str(j+1) + "a avaliação do aluno " + nomeAluno + ": "))
      somaNotas = somaNotas + (nota * listaPesos[j])
   media = somaNotas / somaPesos
   listaMedias.append(media)

#IMPRESSAO
for i in range(0,qtdeAlunos):
   print("Aluno: " + listaNomes[i])
   print("Media: " + str(listaMedias[i]))
   if(listaMedias[i] >= notaMinima):
      print("Aprovado")
   else:
      print("Reprovado")
    
     
