#Exercício 2
#Ler o ano de nascimento de uma pessoa. Considerando que a pessoa faz aniversário dia 1 de Janeiro, calcular e mostrar sua idade. Verificar também se esta pessoa já pode votar (16 anos ou mais) e se ela já pode tirar carteira de motorista (18 anos ou mais).

anoNasc = int(input('Informe o ano de seu nascimento: '))
idade = 2017 - anoNasc
print('Sua idade: ' + str(idade) + ' anos')
if idade >= 16:
   print('Você tem idade suficiente para votar.')
else:
   print('Você não tem idade suficiente para votar.')
if idade >= 18:
   print('Você tem idade suficiente para dirigir. (Se beber, não dirija.)')
else:
   print('Você não tem idade suficiente para dirigir.')

