x=int (input("Dame el valor de x para euler e^x: "))
n = int (input("Dame el valor de n:"))
fact=1
i=1
acumulador=0
while(i<=n):
    fact=fact*i
    elevar = pow (x,i)
    division = elevar / fact
    acumulador+=division
    i=i+1

resultado_segunda_formula = 1 / acumulador
print ("Valor de la sumatoria: ", acumulador+1)
print("")
print("Resultado para la segunda formula: ", resultado_segunda_formula)