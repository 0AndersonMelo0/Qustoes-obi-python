#https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/cifra/
def  vogal_px():
    e=0
    c=0
    for a in alfabetoD2:
        if a in vogais:
            break
        else:
            c+=1
    for i in alfabetoD:
        if i in vogais:
            break
        else:
            e+=1
    if e<=c:
            return alfabetoD[e]
    else:
            return alfabetoD2[c]

def consoante_segue():
    for a in alfabetoD2:
        if a in vogais:
            None
        else:
            return a

palavra = input()
cifra = ''
alfabeto = 'abcdefghijklmnopqrstuvxz'
alfabeto2 = list(alfabeto)
vogais= 'a e i o u'
for letra in palavra:
    if letra in vogais:
        cifra+=letra
    else:
        if letra == 'z':
            cifra+='zuz'
        else:
            cifra+=letra
            indece = alfabeto.index(letra)
            alfabetoD = (alfabeto2[:indece])[::-1]
            alfabetoD2 = alfabeto2[indece+1:]
            cifra+=vogal_px()
            cifra+=consoante_segue()
print(cifra)