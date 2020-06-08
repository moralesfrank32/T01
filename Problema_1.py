# TAREA 1 (Calculador de numeros perfectos)
N = [int(input('Introduzca un numero: '))]
num = N[0]
i = 0
a = 0
while i < (num-1):
    i=i+1
    M = num % i
    print(i)
    if M == 0:
        a=a+i
print('La suma es: ', a)
if a == num:
    print('>>>>>ES UN NUMERO PERFECTO<<<<<<<')
else:
    print('No es un numero perfecto')






    
    




