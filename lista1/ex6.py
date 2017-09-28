#Exercício 6
#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Informe o tamanho do lado do quadrado: '))
area = lado * lado
dobro = area * 2
print('Área do quadrado: ' + str(area) + ' u.a.')
print('Dobro da área: ' + str(dobro) + ' u.a.')
