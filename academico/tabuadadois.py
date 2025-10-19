print('Digite -1 para sair')
while True:
    numero = int(input('Número para a tabuada:'))
    if numero == -1:
        break 
    print('Tabuada de multiplicaçao de' , numero)
    for i in range(1, 10 + 1):
     ct = ct + 1
     print(i , 'x' , numero , '=', i * numero)
