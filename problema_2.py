# TAREA 2 (Calculador de numeros amigos)
N1 = [int(input('Introduzca el primer numero: '))]
N2 = [int(input('Introduzca el segundo numero: '))]
num1 = N1[0]
num2 = N2[0]
i = 0
a = 0
j = 0
b = 0
while i < (num1-1):
    i=i+1
    M1 = num1 % i
    print(i)
    if M1 == 0:
        a=a+i
while j < (num2-1):
    j=j+1
    M2 = num2 % j
    print(j)
    if M2 == 0:
        b=b+j

print('La suma de a: ', a)
print('La suma de b: ', b)
if a == num2:
    print('>>>>>LOS NUMEROS', num1, 'y', num2, 'SON AMIGOS :D <<<<<<<')
else:
    print('>>>>>LOS NUMEROS', num1, 'y', num2, 'NO SON AMIGOS!! :( <<<<<<<')
