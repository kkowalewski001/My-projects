import tkinter as tk

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
            break

    #pełna kolumna check
    for i in range(w):
        kolumna = i
        kolumna = [element[kolumna] for element in matrix]
        if all(x == 1 for x in kolumna):
            #print(f"pelna kolumna nr {i+1}")
            b_x = ":"
            break

    codeM = f"B = A({b_x},{b_y})"
    if codeM == "B = A(:,:)":
        return "B = A"
    else:
        return str(codeM)


# zmiana stanu przycisku, zmiana 0 i 1 w macierzy
def toggle(button, matrix, row, col):
    if button['bg'] == 'red':
        button.config(text = "B",bg='green')
        matrix[row][col] = 1
    else:
        button.config(text = "A",bg='red')
        matrix[row][col] = 0
    matrix_label.config(text=matGen(matrix))


num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

#Macierz (nested lists)
matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]



window = tk.Tk()
window.geometry("500x250")

#Generowanie przycisków
buttons = []
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        button = tk.Button(window, text='A', bg='red', width=5, height=2, command=lambda x=i, y=j: toggle(buttons[x][y], matrix, x, y))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

#Label wyświetlający kod generowany przez funkcję matGen()
matrix_label = tk.Label(window, text=matGen(matrix), font=("Arial Bold", 12))
matrix_label.grid(row=0, column=num_cols+1, rowspan=num_rows+1, sticky="e")

#Label "Code for Matlab"
label = tk.Label(window, text="Code for MatLab", font=("Arial Bold", 12))
label.grid(row=0, column=num_cols+2, sticky="e")


window.mainloop()
