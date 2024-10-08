salario = 1000
taxa = 0.015

ano = 1996

while (ano < 2026):
    salario = salario + (taxa * salario)

    ano += 1
    taxa = taxa * 2

print(f'O salário em 2025 vai ser de: R$ {salario}.')