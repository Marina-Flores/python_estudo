import random

def jogar():
    print('***********************************')
    print('Bem vindo ao jogo de forca!')
    print('***********************************')

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = str(input('Digite uma letra: ')).strip().upper()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else: 
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Parabéns, você ganhou!')
    else:
        print('Infelizmente você perdeu!')

    print('Fim de jogo')


if(__name__ == '__main__'):
    jogar()