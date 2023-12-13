grid1 = [[1,1,0],
        [0,1,0],
        [1,1,0],]



for i in range(0,3):
    somme = 0
    for el in grid1[i] :
        somme += el
    if somme == 3:
        print('ligne win')
    elif somme == -3:
        print('ligne win')

for i in range(0,3):
    somme = 0
    for el in grid1:
        somme += el[i]
    if somme == 3:
        print('colonne win')
    elif somme == -3:
        print('ligne win')

big_grid = [[[],[],[]]for i in range(9)]
print(big_grid)