#https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/lista/
N=int(input())
c = list(map(int, input().split()))
m = 0
for i in range(0,N//2):
    if (c[i]!=c[(-i)-1]):
        m+=1
print(m)