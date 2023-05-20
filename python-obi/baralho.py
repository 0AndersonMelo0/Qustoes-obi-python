#https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/
cartas = input()

c = []
e = []
u = []
p = []

for i in range(2,len(cartas),3):
    if cartas[i]=='C':
        c.append(cartas[i-2:i])
    elif cartas[i]=='E':
        e.append(cartas[i-2:i])
    elif cartas[i]=='U':
        u.append(cartas[i-2:i])
    elif cartas[i]=='P':
        p.append(cartas[i-2:i])

[print(13-(len(c))) if (len(c)==len(set(c))) else print('erro')]
[print(13-(len(e))) if (len(e)==len(set(e))) else print('erro')]
[print(13-(len(u))) if (len(u)==len(set(u))) else print('erro')]
[print(13-(len(p))) if (len(p)==len(set(p))) else print('erro')]