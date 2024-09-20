nota1 = float(input("Qual foi a nota da primeira prova? "))
nota2 = float(input("Qual foi a nota da segunda prova? "))
nota3 = float(input("Qual foi a nota da terceira prova? "))
nota4 = float(input("Qual foi a nota da quarta prova? "))
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4
print("O total das notas é igual a ",soma)
print("A média do aluno é igual a ", media)
if media >= 6:
    print("Parabéns! O aluno foi aprovado!")
else:
    print("Que pena... O aluno foi reprovado...")