op = input("O que deseja achar?\n 1 - Concentração\n 2 - Massa\n 3 - Volume\n")

if op == "1": # descobrir a concentração
    massa = float(input("Digite a massa em gramas: "))
    volume = float(input("Digite o volume em litros: "))
    concentracao = massa / volume

    print("A concentração comum é:", concentracao, "g/L")

elif op == "2": # descobrir massa
    concentracao = float(input("Digite a concentração: "))
    volume = float(input("Digite o volume em litros: "))
    massa = concentracao * volume

    print("A massa é:", massa)

elif op == "3": # descobrir volume
    massa = float(input("Digite a massa em gramas: "))
    concentracao = float(input("Digite a concentração em g/L: "))
    volume = massa / concentracao

    print("O volume é:", volume, "L")

else:
    print("Opção inválida. Tente novamente.")
