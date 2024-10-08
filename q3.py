numero = int(input('Digite um número: '))

if numero < 2:
    print('NÃO É PRIMO!')
else:
    primo = True
    contador = 2 

    while contador * contador <= numero:
        if numero % contador == 0:
            primo = False
            break
        contador += 1

    if primo:
        print('É PRIMO!')
    else:
        print('NÃO É PRIMO!')
