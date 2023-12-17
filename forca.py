def titulo():
    titulo = '***Bem vindo ao jogo da Forca!***'
    print('*' * len(titulo))
    print(titulo)
    print('*' * len(titulo))

def gerando_palavra_secreta(nome_arquivo='frutas.txt'):# Puxando as palavras do arquivo txte usei parâmetro opcional
    from random import randint
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    lista_frutas = []
    for linha in arquivo:
        linha_formatada = linha.strip('\n')
        lista_frutas.append(linha_formatada)
    arquivo.close()
    pos = randint(0, len(lista_frutas))

    palavra_secreta = lista_frutas[pos].lower()
    return palavra_secreta #vai retornsr o valor pois ele vai ser chamado numa variável lá na função principal

def inicializa_letras_acertadas(palavra_secreta): #palavra_secreta é o parâmetro aqui
    return ['_' for letra in palavra_secreta]  # Vai ser adaptável


def verificador_de_letra(chute, palavra_secreta, letras_acertadas):#tem que passar os parâmetros para funcionar
    for pos, letra in enumerate(palavra_secreta):  # Vai pecorrer a palavra
        if chute == letra:  # Vai verificar se tem a letra na palavra
            letras_acertadas[pos] = chute  # Vai substuir na lista a letra na posição que o usuário acertar

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def formacao_da_palavra_secreta(letras_acertadas):
    for i in range(0, len(letras_acertadas)):  # Vai imprimir cada elemento da lista
        print(f'{letras_acertadas[i]}', end='')
    print()  # vai quebrar o end= para não grudar com a próxima linha


def imprime_palavra_perdedor(palavra_secreta):
    print('Puxa, você perdeu!')
    print(f'A palavra era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def jogo_forca():

    titulo()
    palavra_secreta = gerando_palavra_secreta('palavras.txt') #Aqui o parâmetro não é obrigatório é opcional
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    while not enforcou and not acertou: #True and True
        chute = str(input('Qual a letra? ')).strip().lower() #Vai tirar os espaços e vai ter as letras minúsculas
        
        if chute in palavra_secreta: #Caso tenha a letra
            #Responsável por encontrar a letra e posição dela
            verificador_de_letra(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print(f'Ops, você errou! Faltam {6 - erros} tentativas!')
        #desenhor da forca
        desenha_forca(erros)
        # Responsável por printar na tela as letras ou underlines
        formacao_da_palavra_secreta(letras_acertadas)

        #Encerramento do jogo
        if erros == 6:
            imprime_palavra_perdedor(palavra_secreta)
            enforcou = True  # condição de parada
        elif '_' not in letras_acertadas: #Pois quando não tiver mais '_' vai ter completado a palavra
            imprime_mensagem_vencedor()
            acertou = True


if __name__ == '__main__':
    jogo_forca()
