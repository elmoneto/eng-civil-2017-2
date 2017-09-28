#Exercício 4 (alternativa)
#Imprimir os múltiplos de 7 menores que 200.
#Sem usar o operador módulo

for i in range(7,201,7):
   print(i)
   
#O último número separado por vírgula no range define o tamanho do passo em cada "volta" do laço for
#Quando ele não é definido, o python assume que o passo é de tamanho 1
#Começando o laço for com o número 7 e somando 7 à variável i em cada passo, eu garanto que todos os "i" serão múltiplos de 7
#7-14-21-...-196
#E se eu quisesse todos os múltiplos de 3? Simples: for i in range(3,201,3)
      
