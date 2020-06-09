# TAREA 2 (Calculador de numeros amigos)
N = [int(input('INTRODUZCA LA CANTIDAD DE NUMEROS AMIGOS QUE DESEA ENCONTRAR: '))]
n = (N[0])*(1100)
for a in range(1, n):
    s= 0
    for n in range(1, a):
        if a%n==0:
            s=s+n
    for b in range(1, n):
        t=0
        for n in range(1, b):
            if b%n==0:
                t=t+n
            #Se comparando si los dos numeros son amigos
        if s==b and t==a and a!=b:
            print('los numeors amigos son:',a,b)
            
            