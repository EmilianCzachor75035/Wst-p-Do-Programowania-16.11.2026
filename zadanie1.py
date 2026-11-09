#zadanie1

#Utwórz listę: Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21], przetestuj działanie wszystkich 
#zaprezentowanych operacji na listach, a ich wynik wyświetl w konsoli. 

x = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]


print("Długość listy:", len(x))
print("Max:", max(x))
print("Min:", min(x))
print("Suma:", sum(x))
print("Zwrócona posortowana (sorted):", sorted(x))

x.append(6)
x.insert(1, 99)
x.extend([100, 101])
x.remove(3)
pobrany_element = x.pop()
x.sort()
x.reverse()

print("Pierwszy element:", x[0])
print("Ostatni element:", x[-1])
print("Wycinek od indeksu 2 do 5:", x[2:5])
print("Wycinek z krokiem 2:", x[::2])
print("Odwrócona lista wycinkiem:", x[::-1])

lista_zdublowana = x * 2

x.clear()