def jogo_forca():
    titulo = '***Bem vindo ao jogo da Forca!***'
    print('*'*len(titulo))
    print(titulo)
    print('*'*len(titulo))
    #Puxando as palavras da lista
    from random import randint
    arquivo = open('frutas.txt', 'r', encoding='utf-8')
    lista_frutas = []
    for linha in arquivo:
        linha_formatada = linha.strip('\n')
        lista_frutas.append(linha_formatada)
    arquivo.close()
    pos = randint(0, len(lista_frutas))

    palavra_secreta = lista_frutas[pos].lower()

    letras_acertadas = ['_' for letra in palavra_secreta] #Vai ser adaptável

    enforcou = False
    acertou = False
    erros = 0
    while not enforcou and not acertou: #True and True
        chute = str(input('Qual a letra? ')).strip().lower() #Vai tirar os espaços e vai ter as letras minúsculas
        if chute in palavra_secreta: #Caso tenha a letra
            #Responsável por encontrar a letra e posição dela
            for pos, letra in enumerate(palavra_secreta): #Vai pecorrer a palavra
                if chute == letra: #Vai verificar se tem a letra na palavra
                    letras_acertadas[pos] = chute #Vai substuir na lista a letra na posição que o usuário acertar
        else:
            erros += 1
            print(f'Ops, você errou! Faltam {len(palavra_secreta) - erros} tentativas!')
        # Responsável por printar na tela as letras ou underlines
        for i in range(0, len(letras_acertadas)):  # Vai imprimir cada elemento da lista
            print(f'{letras_acertadas[i]}', end='')
        print()  # vai quebrar o end= para não grudar com a próxima linha
        #Encerramento do jogo
        if erros == 6:
            print('Você perdeu!')
            enforcou = True  # condição de parada
        elif '_' not in letras_acertadas: #Pois quando não tiver mais '_' vai ter completado a palavra
            print('Você acertou!')
            acertou = True

    print('Fim de jogo!')

if __name__ == '__main__':
    jogo_forca()

#letras_faltando = str(letras_acertadas.count('_'))
