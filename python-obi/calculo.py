#https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/calculo/
S,A,B = (int(input()) for i in range(3))
intervalo = list(range(A,B+1))
k = 0
for n in intervalo:
    sm = 0
    for j in str(n):
        sm+=int(j)
    if (sm==S):
        k+=1
print(k)