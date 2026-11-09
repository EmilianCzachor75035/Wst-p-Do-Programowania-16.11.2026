#zadanie3a
#3a. Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.

imie = input("Podaj imię: ")
print("Witaj", imie)

#zadanie3b
#b. Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek. 

wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

#zadanie3c
#c. Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.  

imie_c = input("Podaj imię: ")
nazwisko_c = input("Podaj nazwisko: ")
print("Inicjały:", imie_c[0].upper() + nazwisko_c[0].upper())

#zadanie3d
#d. Wczyta łańcuch i wyświetli go pięć razy. 

lancuch = input("Podaj dowolny łańcuch znaków: ")
print(lancuch * 5)

#zadanie3e
#e. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy. 

lan1 = input("Podaj pierwszy łańcuch: ")
lan2 = input("Podaj drugi łańcuch: ")
lan3_polaczone = lan1 + lan2
print("Połączony łańcuch:", lan3_polaczone)

#zadanie3f
#f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę drugiego.\
 
lan1_f = input("Podaj pierwszy łańcuch (zad f): ")
lan2_f = input("Podaj drugi łańcuch (zad f): ")
polowa1 = lan1_f[:len(lan1_f)//2]
polowa2 = lan2_f[len(lan2_f)//2:]
lan3_z_polow = polowa1 + polowa2
print("Łańcuch z połów:", lan3_z_polow)