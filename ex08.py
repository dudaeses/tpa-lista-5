# 8) Escreva um algoritmo que receba um nome e três notas e atenda exiba uma mensagem diferente para cada um dos casos a seguir:
# A) Se a média for maior que 7, exiba a mensagem "Parabéns (nome)! Você foi aprovado".
# B) Se a média for menor que 7 e maior que 5, exiba a mensagem "Você ficou com média (media) e está de recuperação".
# C) Se a média for menor que 5, exiba a mensagem "(Nome), você está reprovado".

nome = (input("Nome: "))
nota1 = int(input("Nota: "))
nota2 = int(input("Nota: "))
nota3 = int(input("Nota: "))

nota = (nota1+nota2+nota3)/3

if nota > 7:
    print ("Parabéns", nome,"! Você foi aprovado.")
else:
    if nota <= 7 and nota >= 5:
            print ("Você ficou com média", nota, "e está de recuperação.")
    else:
        if nota < 5:
            print (nome,", você está reprovado.")
