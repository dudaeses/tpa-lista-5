# 7) Escreva um algoritmo que receba dois números e exiba para o usuário todos os números intermediários a eles, veja o exemplo:
# Primeiro número: 5
# Segundo número: 15
# Resultado: 6 7 8 9 10 11 12 13 14

num1 = int(input("Digite um número: ")) 
num2 = int(input("Digite outro número: ")) 

cont = num1
while cont <= num2:
    print (cont)
    cont = cont + 1
    
