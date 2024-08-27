print('Bem-vindo a Loja do Leonardo Pinheiro')

valor_unitario = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))

valor_total = valor_unitario * quantidade #Multiplica o valor do produto pela quantidadede de produtos, assim calculando o valor total

desconto4 = valor_total / 100 * 4 #Cálculo do desconto de 4%
desconto7 = valor_total / 100 * 7 #Cálculo do desconto de 7%
desconto11 = valor_total / 100 * 11 #Cálculo do desconto de 11%

if valor_total < 2500: #Se o valor total for menos que 2500, entra nesta condição
    print(f'O valor SEM desconto: R${valor_total:.2f}')
    print(f'O valor COM desconto: R${valor_total:.2f}')

elif valor_total >= 2500 and valor_total < 6000: #Se o valor total for igual ou maior a 2500 e menor que 6000, entra nesta condição
    print(f'O valor SEM desconto: R${valor_total:.2f}')
    print(f'O valor COM desconto: R${valor_total - desconto4:.2f}')

elif valor_total >= 6000 and valor_total < 10000: #Se o valor total for igual ou maior 6000 e menor que 10000, entra nesta condição
    print(f'O valor SEM desconto: R${valor_total:.2f}')
    print(f'O valor COM desconto: R${valor_total - desconto7:.2f}')

else: #Qualquer outra condição que não for nenhuma das anteriores, entra nesta
    print(f'O valor SEM desconto: R${valor_total}') 
    print(f'O valor COM desconto: R${valor_total - desconto11:.2f}')