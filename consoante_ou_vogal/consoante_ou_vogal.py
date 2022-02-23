import time
print('Esse programa verifica se a entrada é uma vogal ou consoante.')
loop = True
while loop:
    letra = input('--Digite uma letra: ')
    linha = '-'*100
    if letra.isdigit():
        print(linha,'\n')
        print('Só letras\n')
        print(linha)

    elif len(letra) > 1 and not letra.isdigit():
        print(linha)
        print('Digite só uma letra')
        print('\n')




    elif letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        print('\n')
        print(linha)
        print('--É consoante')
        print('\n')

    else:
        print('\n')
        print(linha)
        print('--É vogal')
        print('\n')
    print('\n')
    continua = input('Deseja continuar?: ')
    print('\n')
    if continua == 'nao' or continua == 'Nao' or continua == "não" or continua == "Não":
        print('Encerrando...')
        time.sleep(4)
        input('Pressione Enter pra sair.')
        loop = False
