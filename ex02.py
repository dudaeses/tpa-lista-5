# 2) Escreve um algoritmo que receba 10 valores digitados pelo usuário e no final exiba o maior número.

cont = 1
num = int(input("Digite um número: "))

maior_num = 0

while cont <= 9:
    num = int(input("Digite um número: "))
    cont = cont + 1 

if num > maior_num:
    maior_num = num

print ("O maior número é: ", maior_num)
