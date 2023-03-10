def matGen(matrix):

    b_x= 0
    b_y= 0
    wier = []
    kolu = []

    #długość kolumny
    l = len(matrix)

    #długośc rzędu
    w = len(matrix[0])

 
    
    #zakres wierszów
    #help = [0,0,0]
    help = [0] * w
    for i in range(l):
        for j in range(w):
            if matrix[i][j] == 1:
                help[j] = 1
    for i in range(len(help)):
        if help[i] == 1:
            wier.append(i+1)
    b_y = wier

    #zakres kolumn
    help = [0] * l
    for i in range(w):
        kolumna = i
        kolumna = [element[kolumna] for element in matrix]
        for j in range(len(kolumna)):
                if kolumna[j] == 1:
                    help[j] = 1

    for i in range(len(help)):
        if help[i] == 1:
            kolu.append(i+1)
    b_x = kolu


    #pełny rząd check
    for i in range(w):
        if all(x == 1 for x in matrix[i]):
            #print(f"pelny rząd nr {i+1}")
            b_y = ":"
            skip_wiersz = True
            break

    #pełna kolumna check
    for i in range(w):
        kolumna = i
        kolumna = [element[kolumna] for element in matrix]
        if all(x == 1 for x in kolumna):
            #print(f"pelna kolumna nr {i+1}")
            b_x = ":"
            skip_kolumna = True
            break

        
    return f"B = A({b_x},{b_y})"


m = [[1, 0, 1], [1, 0, 1], [1, 0, 1]]
print(matGen(m))

