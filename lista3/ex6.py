#Exercício 6
#Calcular a média de idade de uma turma de alunos. O programa imprimirá a média quando o usuário digitar uma idade igual a zero.

numAlunos = 0
somatorio = 0.
idade = -1
while(idade != 0):
   idade = int(input("Informe a idade do aluno ou 0 para encerrar: "))
   if(idade != 0):
      somatorio += idade
      numAlunos += 1
print("Média de idade da turma: " + str(somatorio/numAlunos))
