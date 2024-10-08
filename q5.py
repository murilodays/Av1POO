contador = 1
valorUnitario = 1.99

print('Lojas Quase Dois - Tabela de Preços')
while(contador < 51):
    print(f'{contador} - R$ {contador * valorUnitario}')
    contador += 1

print('============================================================')
qtdItens = int(input('Quantidade de itens: '))
print(f'VALOR A PAGAR: R$ {qtdItens * valorUnitario}')
