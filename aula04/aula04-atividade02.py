def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite novamente a nota: "))

notaA = float(input("Digite a 1a nota: "))
validar_nota(notaA)

notaB = float(input("Digite a 2a nota: "))
validar_nota(notaB)