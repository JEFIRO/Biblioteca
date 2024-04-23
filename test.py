"""Exercício 7 – Preparado(a) para raiz quadrada?

Calcule a parte inteira da raiz quadrada de um número inteiro positivo sem usar a função sqrt.
Para isso, você precisa saber que a raiz quadrada de um número n é igual aproximadamente à quantidade de números ímpares
 consecutivos (a partir do 1) cuja soma é igual a n (ou o mais próxima possível de n)

"""
numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Por favor, digite um número inteiro positivo.")


raiz = 0
soma_impares = 0

for i in range(2,numero+1):
    if i % 2 != 0  and soma_impares <= numero:
        soma_impares += i
        raiz += 1

print(f"A parte inteira da raiz quadrada é aproximadamente {raiz}.")


