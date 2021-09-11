import random
from typing import NewType 

print('***********************************')
print('Bem vindo ao jogo de adivinhação!')
print('***********************************')

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontuacao = 1000

print('Qual o nível de dificuldade você deseja? ')
print('(1) - Fácil (2) - Médio (3) - Difícil')

nivel = int(input('Digite o nível: '))

if (nivel == 1):
    total_tentativas = 20
elif (nivel == 2):
    total_tentativas = 10
elif (nivel == 3): 
    total_tentativas = 5
else:
    print('Número inválido, iniciaremos com o nível fácil')
    total_tentativas = 20
    
for tentativa_atual in range(1, total_tentativas + 1):
    print(f'Tentativa {tentativa_atual} de {total_tentativas}')
    numero_usuario = int(input('Digite um número qualquer entre 1 e 100: '))

    if(numero_usuario < 1 or numero_usuario > 100):
        print('Você deve digitar um número entre 1 e 100')
        continue

    acertou = numero_usuario == numero_secreto
    maior = numero_usuario > numero_secreto
    menor = numero_usuario < numero_secreto

    if(acertou):
        print(f'Parabéns! Você acertou e fez {pontuacao} pontos.')
        break
    else:
        if(maior):
           print('Número digitado maior que o número secreto.')
           pontuacao -= numero_usuario - numero_secreto
           print(pontuacao)
        elif(menor):
          print('Número digitado menor que o número secreto.')
          pontuacao -= numero_secreto - numero_usuario
          print(pontuacao)
print('Fim de jogo!')
