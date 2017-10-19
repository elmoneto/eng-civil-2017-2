#Exercício 2
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = 'eu'
senha = 'eu'

while usuario == senha:
   usuario = input('Informe o seu nome de usuário: ')
   senha = input('Informe a sua senha: ')
   if(usuario != senha):
      break
   print('Nome de usuário e senha não podem ser iguais.')
print('Nome de usuário e senha válidos.')
   

