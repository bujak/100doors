#  creatig empty list
tab = []

# filling list with 0 100 times  (0 means that door is closed)
for door in range(100):
    tab.append(0)

# walking around hallway 100 times
for step in range(1, 101):

    # shutting and opening doors
    for door in range(step-1, 100, step):
        if tab[door] == 0:
           tab[door] = 1
        else:
            tab[door] = 0

print("Doors opened:", end=" ")

# printing index of opened doors
for door, v in enumerate(tab):
    if tab[door] == 1:
        print(door + 1, end=", ")
