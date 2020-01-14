import numpy as np

print("Inserire un numero:")
#n = int(input())
n = 8759068*7979968

print(n)

isprime = True
for p in range(2,int(np.sqrt(n))):
    if (n % p == 0):
        print(f'Trovato fattore: {p}')
        isprime = False
if isprime:
    print(f'il numero {n} è primo')