# TAREA 1 (Calculador de numeros perfectos)
N = [int(input('INTRODUZCA LA CANTIDAD DE NUMEROS PERFECTOS QUE DESEA ENCONTRAR: '))]
num = N[0]
i = 0
a = 0
k=0
M = 0
#----------------------------------------------
def numero_perfecto():
    global a
    global num

    for i in range(0, k-1):
        i=i+1
        M = k % i
        if M == 0:
            a=a+i
    if a == k:       
        print('>>>>>>EL NUMERO PERFECTO ES:', a)
    else:
        num=num+1
#------------------------------
while k < (num):
    k=k+1
    numero_perfecto() 
    a = 0 
