
print("\nAby stworzyć podmacierz B z macierzy orginalnej B należy podać zakres rzędów i wierszy\n\
      (na przykład podmacierz z wirszów 1-2 i  kolumn 3-4)")     
print("Jeśli chcesz zaznaczyć wszyskie kolumny lub wiersze wpisz 'wszystkie'\n ")

#dlugosc = input("Podaj długość macierzy A: ")
#wysokosc = input("Podaj wysokość macierzy B: ")

bx1 = input("podaj zakres wierszów ( najpierw dolna granica potem górna)\n")
if bx1 != "wszystkie":
    bx2 = input()
    b_x = f"{bx1}:{bx2}"
else:
    b_x = ":"


by1 = input("podaj zakres kolumn ( najpierw dolna granica potem górna)\n")
if by1 != "wszystkie":
    by2 = input()
    b_y = f"{by1}:{by2}"
else:
    b_y = ":"



print(f"B = A({b_x},{b_y})")
# print(f"B = A({x}:{y},{z}:{q})")