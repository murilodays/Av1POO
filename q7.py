dividaInicial = 2100

parcelasOpcoes = [1, 3, 6, 9, 12]
jurosOpcoes = [0, 10, 15, 20, 25]

print(f"{'Dívida':<10} | {'Juros':<10} | {'Parcelas':<22} | {'Valor da Parcela'}")
print("-" * 60)

i = 0

while i < len(parcelasOpcoes):
    parcelas = parcelasOpcoes[i]
    juros = jurosOpcoes[i]
    
    valorJuros = dividaInicial * (juros / 100)
    valorDivida = dividaInicial + valorJuros
    valorParcela = valorDivida / parcelas

    print(f"R$ {valorDivida:,.2f}  | R$ {valorJuros:,.2f} | {parcelas:<22} | R$ {valorParcela:,.2f}")
    
    i += 1
