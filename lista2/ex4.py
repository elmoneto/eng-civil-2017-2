#Exercício 4
# Leia a velocidade máxima permitida em uma avenida e a velocidade com que o motorista estava dirigindo nela. Calcule a multa que uma pessoa vai receber, sabendo que são pagos: 
#a) 50 reais se o motorista ultrapassar em até 10 km/h a velocidade permitida; 
#b) 100 reais, se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida; 
#c) 200 reais, se estiver acima de 31 km/h da velocidade permitida. 

vmax = int(input('Informe a velocidade máxima permitida na avenida: '))
vmotor = int(input('Informe a velocidade do motorista na avenida: '))
dif = vmotor - vmax
if dif > 0: #significa que ele vai pagar multa (falta verificar quanto)
   if(dif <= 10):
      print('Valor da multa: R$ 50,00.')
   elif(dif >= 11 and dif <= 30):
      print('Valor da multa: R$ 100,00.')
   elif(dif >= 31):
      print('Valor da multa: R$ 200,00. Vai abrindo a carteira.')
else: #significa que ele não vai pagar multa
   print('Motorista dentro do limite de velocidade.')
