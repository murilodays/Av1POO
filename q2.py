contador = 0
par = 0
impar = 0

while (contador < 10):
    numero = int(input('Informe um número: '))

    if (numero % 2 == 0):
        par += 1
    else:
        impar += 1
    
    contador += 1

print(f'NÚMEROS PARES: {par}')
print(f'NÚMEROS ÍMPAR: {impar}')