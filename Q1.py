# -*- coding: utf-8 -*-
import os
import math
import time

# Variáveis declaradas fora do loop para manter o estado
a = 0.0
b = 0.0
c = 0.0
delta = 0.0
xI = 0.0
xII = 0.0

dados_lidos = False
calculo_feito = False

while True:
    os.system('clear')
    print("===== MENU =====")
    print("1 - Leitura")
    print("2 - Cálculo")
    print("3 - Impressão")
    print("4 - Saída\n")
    
    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("\nPor favor, digite apenas números inteiros!")
        time.sleep(1.5)
        continue

    if opcao == 1:
        os.system('clear')
        print("--- 1. LEITURA DOS COEFICIENTES ---\n")
        
        while True:
            a = float(input("Digite A: "))
            if a == 0:
                print("O valor de A não pode ser zero numa equação do 2º grau!\n")
            else:
                break

        b = float(input("Digite B: "))
        c = float(input("Digite C: "))

        dados_lidos = True
        calculo_feito = False
        
        print("\nDados lidos com sucesso!")
        time.sleep(1.5)

    elif opcao == 2:
        os.system('clear')
        print("--- 2. CÁLCULO ---\n")
        
        if not dados_lidos:
            print("Erro: Faça a Leitura (Opção 1) antes de calcular!")
        else:
            delta = b**2 - 4 * a * c

            if delta >= 0:
                xI = (-b + math.sqrt(delta)) / (2 * a)
                xII = (-b - math.sqrt(delta)) / (2 * a)

            calculo_feito = True
            print("Delta calculado com sucesso!")

        time.sleep(1.5)

    elif opcao == 3:
        os.system('clear')
        print("--- 3. IMPRESSÃO DOS RESULTADOS ---\n")
        
        if not calculo_feito:
            print("Erro: Faça o Cálculo (Opção 2) antes de imprimir!")
        else:
            print(f"A = {a}")
            print(f"B = {b}")
            print(f"C = {c}")
            print(f"Delta = {delta}")

            if delta >= 0:
                print(f"X1 = {xI:.2f}")
                print(f"X2 = {xII:.2f}")
            else:
                print("Sem solução no conjunto dos números Reais!")

        print("\n----------------------------------")
        input("Pressione Enter para voltar ao menu...")

    elif opcao == 4:
        print("\nSaindo do programa...")
        break

    else:
        print("\nOpção inválida! Escolha entre 1 e 4.")
        time.sleep(1.5)