print(' '*10,'-'*50,'REAJUSTE SALARIAL','-'*50,'\n\n')
salario = int(input('Qual o seu salario?: '))


if salario <= 280:
    novo_salario = 0.2*salario + salario
    print('O salario antes do ajuste era de',salario,'reais','\n')
    print(r'Foi aplicado um aumento de 20% em seu salario','\n')
    print('Gerando um aumento de',0.2*salario,'reais','\n')
    print('O novo salario agora é de',novo_salario,'reais','\n')
elif salario > 280 and salario <700:
    novo_salario = 0.15*salario + salario
    print('O salario antes do ajuste era de',salario,'reais','\n')
    print(r'Foi aplicado um aumento de 15% em seu salario','\n')
    print('Gerando um aumento de',0.15*salario,'reais','\n')
    print('O novo salario agora é de',novo_salario,'reais','\n')
    
elif salario > 700 and salario <1500:
    novo_salario = 0.1*salario + salario
    print('O salario antes do ajuste era de',salario,'reais')
    print(r'Foi aplicado um aumento de 10% em seu salario')
    print('Gerando um aumento de',0.1*salario,'reais')
    print('O novo salario agora é de',novo_salario,'reais')
elif salario > 1500:
    novo_salario = 0.05*salario + salario
    print('O salario antes do ajuste era de',salario,'reais')
    print(r'Foi aplicado um aumento de 5% em seu salario')
    print('Gerando um aumento de',0.05*salario,'reais')
    print('O novo salario agora é de',novo_salario,'reais')

input('Pressione Enter para sair.')