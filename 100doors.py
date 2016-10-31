tab = []

for d in range(100):
    tab.append(0)

def door(step):
    for d in range(step-1, 100, step):
        if tab[d] == 0:
           tab[d] = 1
        else:
            tab[d] = 0

for i in range(1, 101):
    door(i)

print(tab)

for d, v in enumerate(tab):
    if tab[d] == 1:
        print(d+1,end=" ")
