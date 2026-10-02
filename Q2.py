import math

numLados = 0
medLados = 0
area = 0
perimetro = 0

print ("Bem-Vindo a calculadora de polígonos")
while True:
    numLados = int (input ("Digite quantos lados tem seu polígono: "))
    
    if (numLados < 2):
        print("NÃO É UM POLÍGONO")

    elif (numLados > 5):
        print("POLÍGONO NÃO IDENTIFICADO")
        
    else:
        medLados = int (input ("Digite a medida dos lados do seu polígono: "))
        if (numLados == 3):
            print("TRIÂNGULO")
            perimetro = (medLados * 3) / 2
            area = math.sqrt(perimetro * ((perimetro - medLados) ** 3))
            print(f"A área do triangulo é aproximadamente {round(area, 2)}")
        if (numLados == 4):
            print("QUADRADO")
            area = medLados ** 2
            print(f"A área do quadrado é {round(area, 2)}")
        if (numLados == 5):
            print("PENTÁGONO")
            area = 1.72 * (medLados ** 2)
            print(f"A área do pentágono é aproximadamente {round(area, 2)}")
        break