from math import factorial

x=int(input("Dame el valor de x para euler e^x: "))#-5
n=int(input("Dame el valor de n: "))#10, 20, 30
Sumatoria=1#y
for i in range(n):
    i=i+1#contador iteraciones
    Sumatoria=(x**i)/factorial(i)+Sumatoria
Resultado_Segunda_Formula=1/Sumatoria

print("")
print ("Valor de la sumatoria: ",Sumatoria)
print ("Resultado para la segunda formula: ",Resultado_Segunda_Formula)
