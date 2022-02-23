#sem muita experiencia por aqui
#notas
um = 1
cinco = 5
dez = 10
cinquenta = 50
cem = 100


print(' '*5,'-'*50,'Bem vindo ao caixa eletronico.','-'*50)
print('\n\n')
print('Qual o valor do saque?')
print('\n\n')

saque = int(input('Valor minimo de 10 reais e o máximo de 600 reais: '))

if saque == 1:
    print('Receba uma nota de um real.')
if saque > 1 and saque <5:
    print('Receba',saque,'notas de um real.')

if saque == 5:
    print('Receba uma nota de 5 reais.')

if saque > 5 and saque <10:
    print('Receba uma nota de 5 reais e',saque-5,'notas de um real')

if saque == 10:
    print('Receba uma nota de  10 reais.')

if saque >10 and saque < 50:
    
    if saque > 10 and saque <20:
        val = saque - 10
        print('Receba uma nota de 10 reais e',val,'notas de um real.')
            
    if saque == 20:
        print('Receba 2 notas de 10 reais.')
    
    if saque > 20 and saque < 30:
        val = saque - 20
        print('Receba 2 notas de 10 reais e',val,'notas de um real')
    
    if saque == 30:
        print('Receba 3 notas de 10 reais.')
    
    if saque > 30 and saque <40:
        val = saque - 30
        print('Receba 3 notas de 10 reais e',val,'notas de um real.')

    if saque == 40:
        print('Receba 4 notas de 10 reais.')

    if saque > 40 and saque < 50:
        val = saque - 40
        print('Receba 4 notas de 10 reais e',val,'notas de 1 real.')



if saque == 50:
    print('Receba 1 nota de 50 reais.') 

if saque > 50 and saque <100:

    if saque > 50 and saque < 60:
        val = saque - 50
        print('Receba uma de 50 reais e',val,'notas de um real.')


    if saque == 60:
        print('Receba 1 nota de 50 reais e 1 de 10 reais.')

    if saque > 60 and saque < 70:
        val = saque - 60
        print('Receba 6 de 10 reais e',val,'notas de um real.')

    
    if saque == 70:
        print('Receba 1 nota de 50 reais e 2 de 10 reais.')


    if saque >70 and saque < 80:
        val = saque - 70
        print('Receba 1 nota de 50 reais, 2 notas de 10 reais e',val,'notas de um real.')

    if saque == 80:
        print('Receba 1 nota de 50 reais e 3 de 10 reais.')

    if saque > 80 and saque < 90:
        val = saque - 80
        print('Receba 8 notas de 10 reais e',val,'notas de um real.')

    if saque == 90:
        print('Receba 1 nota de 50 reais e 4 notas de 10 reais.')

    if saque > 90 and saque < 100:
        val = saque - 90
        print('Receba 9 notas de 10 reais e',val,'notas de um real.')


if saque == 100:
    print('Receba 1 nota de cem.')


if saque > 100 and saque <600:
    if saque == 200:
        print('Receba 2 notas de 100 reais.')
    
    if saque == 300:
        print("Receba 3 notas de 100 reais.")

    if saque == 400:
        print('Receba 4 notas de 100 reais.')

    if saque == 500:
        print('Receba 5 notas de 100 reais.')


if saque == 600:
    print('Receba 6 notas de 100 reais.')

if saque > 600:
    print('O saque pedido excede o limite.')

input('Pressione Enter para sair')