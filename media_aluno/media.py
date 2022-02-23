print('Esse programa calcula a media de notas de uma aluno.')
um = input('Primeiro bimestre: ')
dois = input('Segundo bimestre: ')
tres = input('Terceiro bimestre: ')
quatro = input('Quarto bimestre: ')
media = (int(um)+int(dois)+int(tres)+int(quatro))/4
print('A media é',media,'\n')
if media < 6:
    print('--Foi reprovado--\n')
else:
    print('--Foi aprovado!--')

input('pressione enter pra sair')