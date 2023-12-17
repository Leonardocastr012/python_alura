arquivo = open('frutas.txt', 'w')
arquivo.write('melancia\n')
arquivo.close()

fruta = str(input('Digite uma fruta: '))
fruta = fruta + '\n'
arquivo = open('frutas.txt', 'a')
arquivo.write(fruta)
arquivo.close()