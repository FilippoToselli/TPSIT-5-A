import math

print("Inserire p:")
p = int(input())
print("inserire q:")
q = int(input())

n = int(p * q)

print("n =", n)

m = 0

if(p>q):
    maggiore = p
else:
    maggiore = q

while(m==0):
    if((maggiore % (p-1) == 0) and (maggiore % (q-1) == 0)):
        m = maggiore
        break
    maggiore = maggiore + 1

print("m =", m) 

while(True):
    print("Inserire un c che sia compreso tra 1 e m:")
    c = int(input())
    if(math.gcd(c, m)==1):
        break
    else:
        print("Il numero inserito non è compreso tra 1 e m:")

d = 0

while(True):
    if((c*d)%m == 1):
        break
    else:
        d = d + 1

print("d =", d)

print("Chiave pubblica: n=", n," c=", c)
print("Chiave privata: m=", m," d=", d)