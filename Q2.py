import sys

A = 0
B = 0
C = 0
triangulo = False

print("1 Ler e Exibir")
print("2 Sair")
tecla = input("item: ")

if tecla == "1":
    A = float(input("Digite A: "))
    B = float(input("Digite B: "))
    C = float(input("Digite C: "))

    if (A < B + C) and (B < A + C) and (C < A + B):
        triangulo = True
    else:
        triangulo = False

    if triangulo == True:
        print("Trata-se de um Triângulo!")
    else:
        print("Uma figura qualquer de três lados")

    print("\nPrograma Finalizado!")

elif tecla == "2":
    print("\nPrograma Finalizado!")

sys.exit()