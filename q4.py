popA = 80000
taxaA = 0.03
popB = 200000
taxaB = 0.015

qtdAnos = 0

while(popA < popB):
    popA = popA + (popA * taxaA)
    popB = popB + (popB * taxaB)

    qtdAnos += 1

print(f'A população do país A vai ultrapassar a populção do país B em: {qtdAnos} anos.')