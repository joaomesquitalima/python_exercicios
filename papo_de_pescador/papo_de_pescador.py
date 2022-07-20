print('A lei de um municipio diz que não se pode pescar mais que 50kg. Cada kg acima de 50 é cobrado multa de 4 reais.')
kg_permitido = 50
multa_excesso = 4
massa = int(input('Quanto você pescou?: '))
excesso = massa-kg_permitido
multa = excesso*multa_excesso
if massa > 50:

    print("Você excedeu", excesso, 'kilos.')
    print('Deverá pagar', multa, 'reais de multa.')
else:
    print('Voce excedeu',excesso)
    print('Você está dentro das normas.')

input('Pressione Enter para sair.')
