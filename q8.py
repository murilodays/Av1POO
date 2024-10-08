gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

totalAlunos = 0
notas = []

while True:
    totalAcertos = 0
    print(f"\nAluno {totalAlunos + 1}, responda as 10 questões:")

    respostas = []
    i = 0
    while i < 10:
        resposta = input(f"Questão {i + 1}: ").upper()
        respostas.append(resposta)
        i += 1

    i = 0
    while i < 10:
        if respostas[i] == gabarito[i]:
            totalAcertos += 1
        i += 1

    notas.append(totalAcertos)
    totalAlunos += 1
    
    outroAluno = input("Outro aluno vai utilizar o sistema? (S/N): ").upper()
    if outroAluno != 'S':
        break

if totalAlunos > 0:
    print("\nResultados da Turma:")
    print(f"Maior Acerto: {max(notas)}")
    print(f"Menor Acerto: {min(notas)}")
    print(f"Total de Alunos que utilizaram o sistema: {totalAlunos}")
    print(f"Média das Notas da Turma: {sum(notas) / totalAlunos:.2f}")
else:
    print("Nenhum aluno utilizou o sistema.")
