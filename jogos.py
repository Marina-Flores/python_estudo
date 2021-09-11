import forca
import jogo_adivinhacao

def escolha_jogo():
    print('***********************************')
    print('******* Escolha o seu jogo *******')
    print('***********************************')

    print('(1) Forca - (2) Adivinhação')
    jogo_escolhido = int(input('Digite o número do jogo: '))

    if(jogo_escolhido == 1):
        print('Jogando forca')
        forca.jogar()
    elif(jogo_escolhido == 2): 
        print('Jogando adivinhação')
        jogo_adivinhacao.jogar()


if(__name__ == '__main__'):
    escolha_jogo()