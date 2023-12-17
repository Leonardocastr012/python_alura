from forca import jogo_forca #importou as funções
from advinhacao import jogo_adivinhacao
#caso importe o arquivo python sem ter função vai aparecer todo o código no terminal
def jogo():
    titulo = '********Escolha seu jogo!********'
    print('*'*len(titulo))
    print(titulo)
    print('*'*len(titulo))

    print('(1) Forca (2) Adivinhação')

    jogo= int(input('Qual jogo? '))

    if jogo == 1:
        jogo_forca()
    elif jogo == 2:
        jogo_adivinhacao()


jogo()