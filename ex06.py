# 6) Escreva um programa que receba o preço de dois produtos. Calcule um desconto de de 8% no primeiro produto, 11% no segundo e apresente o valor final a ser pago.

val1 = int(input("Digite o valor do primeiro produto: "))
val2 = int(input("Digite o valor do segundo produto: "))

val1d = (val1*8)/100
val2d = (val1*11)/100
valor = val1+val1d

print ("O valor a ser pago é: ",valor)