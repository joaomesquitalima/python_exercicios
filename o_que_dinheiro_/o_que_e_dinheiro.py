import time

dia = 24
celular = 2000
print('--Vou te ensinar o que é dinheiro.--')
money = input('Quanto você ganha por mês?: ')
horas_trabalhadas = input('Quantas horas você trabalha por dia?: ')
money = int(money)
horas_trabalhadas = int(horas_trabalhadas)
ganho_por_hora = money/(horas_trabalhadas*30)
custo_de_vida = celular/ganho_por_hora
dias = custo_de_vida/dia
print(' '*40,'*--Considerando que um mês tem 30 dias exatamente.--*\n\n')
time.sleep(4)
print('Você trabalhando',horas_trabalhadas,' horas por dia, em um mês, dá um total de',(horas_trabalhadas*30),'horas trabalhadas por mês.\n')
print('-'*100,'\n')
print('Você ganhando',money,'reais por mês, dá um total de',ganho_por_hora,'reais por cada hora trabalhada \n\n')
time.sleep(1)
print('Isso significa que cada hora que você trabalha vale',ganho_por_hora,'reais\n\n')
print('-'*100,'\n')

print('Então quando você compra um celular de',celular,'reais, por exemplo, ela não custa 2000 reais.\n\nCusta',custo_de_vida,'horas da sua vida.','São',dias,'dias da sua vida. ;)\n\n')
time.sleep(5)
sair = input('Aperte  tecla enter pra sair.')