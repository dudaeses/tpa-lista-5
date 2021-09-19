# 5) Escreva um algoritmo para calcular o fatorial de um número. Se o usuário digitou por exemplo 5, o resultado a ser exibido pelo algoritmo é: 5! é igual 120.

num = int(input("Digite um número: "))

count = 1 
resultado = 1

while count <=  num:
    resultado *= count
    count += 1

print ("O fatorial de", num,"é",resultado)

