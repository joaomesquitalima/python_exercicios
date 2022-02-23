#isso é um programa para uma loja de tintas
#a tinta é vendida em latas de 18 litros, que custam 80 reais
#uma lata = 80 reais
# a cobertura da tinta é de um litro para cada 3 metros quadrados
#isso significa que uma lata serve para 54 metros quadrados

#informar ao usuario a quantidade de latas de tinta a serem compradas e o preco total
lata_litro = 18
lata_price = 80
tamanho = int(input('Tamanho da area a ser pintada(em metros quadrados): '))

latas = tamanho//54
total = latas*lata_price
print('Serão necessarias', latas,'latas de tinta.')
print('Com o custo de',total,'reais')
input('Pressione Enter para sair')

