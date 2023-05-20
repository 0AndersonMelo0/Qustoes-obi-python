#https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/zero/
N = int(input())
nums = []
for i in range(N):
    X = int(input())
    if X != 0:
        nums.append(X)
    else:
        del nums[-1]
print(sum(nums))