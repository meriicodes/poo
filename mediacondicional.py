nota1 = float(input("Digite a sua primeira nota: \n"))
nota2 = float(input("Digite a sua segunda nota: \n"))

media = (nota1 + nota2)/2
print(f'Sua média é: {media}')

if media < 7:
    print('está de reprovado')

else:
    print('você passou')
