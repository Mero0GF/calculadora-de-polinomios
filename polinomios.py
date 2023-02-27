import math

def geraPolinomio(vet,xElevado):
    polinomio =  ""
    for i in range (len(vet)-1,-1,-1):
        if vet[i]!=0:
            if i == 0:
                if vet[i] < 0:
                    polinomio += str(vet[i]) 
                else:
                    polinomio += "+ " + str(vet[i])
            elif i == len(vet)-1:
                polinomio += str(vet[i]) + xElevado + str(i) + " "      
            elif vet[i]>0:
                polinomio += "+ " + str(vet[i]) + xElevado + str(i) + " "         
            else:
                polinomio += str(vet[i]) + xElevado + str(i) + " "
    return polinomio
def inverteVetor(vet,vet2):
    n = len(vet)
    for i in range(n):
        vet2[i] = vet[n-1-i]
    return print(vet2)
def calculaPolinomio(x,vet,xElevado):
    calculo = vet[0]
    for i in range(1,len(vet)):
        xElevado = x**i
        calculo += xElevado*vet[i]
    print("O resultado do polinômio é:",calculo)
    xElevado = "x^"
def somaPolinomio(vet,grau,xElevado):
    grau = int(input("Digite o grau do polinomio: "))
    grau+=1
    vet2 = [0]*grau   
    for x in range(len(vet2)-1,-1,-1):
        vet2[x] = int(input("Digite o termo " + str(x) + ": "))
    print(geraPolinomio(vet2,xElevado))
    print(vet2)
    print(vet)
    polinomio = ""
    for n in range(len(vet)):
        for j in range(len(vet2)):
            if j == n:
                vet[n] = vet[n] + vet2[j]
    for i in range (len(vet)-1,-1,-1):
        if vet[i]!=0:
            if i == 0:
                if vet[i] < 0:
                    polinomio += str(vet[i]) 
                else:
                    polinomio += "+ " + str(vet[i])
            elif i == len(vet)-1:
                polinomio += str(vet[i]) + xElevado + str(i) + " "      
            elif vet[i]>0:
                polinomio += "+ " + str(vet[i]) + xElevado + str(i) + " "         
            else:
                polinomio += str(vet[i]) + xElevado + str(i) + " "
    print(polinomio)
def main():
    xElevado = "x^"
    grau = int(input("Digite o grau do polinomio: "))
    grau+=1
    vet = [0]*grau
    for i in range(len(vet)-1,-1,-1):
        vet[i] = int(input("Digite o termo " + str(i) + ": "))
    print(geraPolinomio(vet,xElevado))
    x = int(input("Digite o valor de x: "))
    calculaPolinomio(x,vet,xElevado)
    pergunta = input("Gostaria de somar polinômios? s/n ")
    if pergunta == "s":
        somaPolinomio(vet,grau,xElevado)
    else:
        print("entao ta bao")
main()
            