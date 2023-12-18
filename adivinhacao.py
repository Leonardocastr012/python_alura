#Curso básico de python
def jogo_adivinhacao():
    from random import randint
    titulo = 'Bem vindo ao jogo de Adivinhação!'
    print('*'*len(titulo))
    print(titulo)
    print('*'*len(titulo))

    numero_secreto = randint(0,50)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade? ')
    print('(1) Fácil (2) Médio (3) Díficil')

    nível = int(input('Defina o nível: '))

    if nível == 1:
        total_de_tentativas = 20
    elif nível == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #while rodada <= total_de_tentativas :
    for rodada in range(1, total_de_tentativas +  1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute = int(input('Digite o número de 1 a 100: '))
        print(f'Você chutou {chute}')

        if chute < 1 or chute > 100:
            print('Você precisa digitar um número de 1 a 100!')
            continue #Sai desse bloco e volta para o início do loop

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Você acertou e fez {pontos}!')
            break #Quebra o laço
        else:
            if maior:
                print(f'Você errou! O número secreto é menor que {chute}')
            elif menor:
                print(f'Você errou! O número secreto é maior que {chute}')
        #rodada += 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print('Fim de jogo!')

if __name__ == '__main__':
    jogo_adivinhacao()