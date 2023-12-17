#Formatação de strings
a = 100.5
b = 29.25
c = 4
d = 5
e = 2010

print(f'R$ {a:.2f}') #Indica as casas decimais do float/ f é para float
print(f'R$ {b:10.2f}') #vai ficar com 10 espaços para a variável
print(f'R$ {b:^10.2f}')#A variável vai ficar centralizado
print(f'R$ {b:>10.2f}|')#A variável vai ficar a direita
print(f'R$ {b:<10.2f}|')#A variável vai ficar a esquerda
print(f'{c:05}') #Preenche com 0 os espaços que faltam
print(f'{c:7d}') # d é para int
print(f'{c:02}/{d:02}/{e}')
print(f'{c:02}',f'{d:02}',f'{e}', sep='/') #entre os valores separados por vírgula ele coloca o elemento escrito(formato de string)

#https://docs.python.org/3/library/string.html#formatexamples

#Arredondar
print(round(b))
#Deixar o valor positivo
y = -10
print(abs(y))

#Como armazenaqr elementos não deixando os duplicados

'''E agora? Será que o Python não oferece alguma coleção onde não podem existir elementos duplicados? Claro que existe uma coleção com esse propósito e ela se chama set.'''
colecao = {11122233344, 22233344455, 33344455566}
'''Repare que usamos {} chaves para declarar os elementos iniciais. Pouca diferença comparando com as sequências, não?'''
#Adicionando elementos no set
'''Para adicionar um elemento a um set devemos chamar a função add (ao invés da append):'''
colecao.add(44455566677) #vai adicionar pois não existe ainda
'''E se usarmos um CPF que já existe? Não deve funcionar, certo? Vamos testar,e ver que o set vai ignorá-lo:'''
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!
#set não possui um índice
#É importante notar que o set não é uma sequência, pois não tem um índice. O código abaixo não funciona:
'''Isso mesmo, não tem índice. E como não temos um índice não sabemos em qual ordem vem os valores quando imprimimos um set de dentro de um laço for:'''
for cpf in colecao:
     print(cpf)
print('Repare que os elementos foram listados fora da ordem de inserção. Isso acontece porque o set não é ordenado.')
'''
RESUMINDO
Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.
Respire fundo e fique tranquilo pois o set será abordado ainda com mais detalhe em outros cursos. Vamos continuar?
'''
#Como limpar o terminal
import os
os.system("cls")

# List Comprehensions

#Normal
frutas = ["maçã", "banana", "laranja", "melancia"]
lista = []
for fruta in frutas:
    lista.append(fruta.upper())
#LC
lista = [fruta.upper() for fruta in lista]

#Pesquisa
'''O recurso List Comprehension também permite utilizar condições para o preenchimento da lista. Considere o objetivo de
 inicializar uma lista com os números pares a partir de uma lista de números inteiros qualquer, 
por exemplo, os números 1,3,4,5,7,8,9. Para descobrir se um número é par, usamos a condição numero%2 == 0, 
que verifica se o resto de uma divisão por 2 é zero. O código abaixo usa um loop para inicializar a lista de pares.'''
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)
#Pesquise como o podemos usar o List Comprehension para fazer o mesmo que o código acima.
pares2 = [n for n in inteiros if n%2 == 0]
print(pares2)