print('Esse programa verifica se um numero é positivo,negativo ou igual a zero.')
um = int(input('Digite um numero: '))

if um> 0:
    print(um,'é positivo.')
elif um < 0:
    print(um,'é negativo.')
elif um == 0:
    print(um,'é igual a zero.')

input('Pressione enter.')