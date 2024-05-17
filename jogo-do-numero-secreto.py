from random import randint
print('Boas vindas ao jogo do número secreto')
numero = 10
numeroSecreto = randint(1,numero)
tentativas = 1
print(numeroSecreto)
chute = int(input('Digite um numero de 1 a {}: '.format(numero)))
while chute == numeroSecreto: 
     numeroSecreto 
if chute != numeroSecreto:
     print('Voce errou o numero secreto era: {}' .format(numeroSecreto))
elif chute > numeroSecreto:
     print('O número secreto é menor que {}'.format(chute))
else:
     print('O número secreto é maior que {}'.format(chute))
