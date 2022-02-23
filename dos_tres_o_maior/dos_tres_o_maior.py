print('Esse programa recebe 3 entradas numericas e diz qual o maior. ')
um = int(input('Digite um numero: '))
dois = int(input('Digite outro numero: '))
tres = int(input('Digite um terceiro numero: '))

if um > dois and um >tres:
    print(um,'é o maior')
elif dois > um and dois > tres:
    print(dois,'é o maior')
elif tres > dois and tres > um:
    print(tres,'é o maior')


if um < dois and um <tres:
    print(um,'é o menor')
elif dois < um and dois < tres:
    print(dois,'é o menor')
elif tres < dois and tres < um:
    print(tres,'é o menor')

input('Pressione enter pra sair')
