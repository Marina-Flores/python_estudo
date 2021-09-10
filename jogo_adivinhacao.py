import random

print('***********************************')
print('Bem vindo ao jogo de adivinhação!')
print('***********************************')

numero_secreto = 12
total_tentativas = 3
tentativa_atual = 1

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
        print('Parabéns! Você acertou')
        break
    else:
        if(maior):
           print('Número digitado maior que o número secreto.')
        elif(menor):
          print('Número digitado menor que o número secreto.')

print('Fim de jogo!')
