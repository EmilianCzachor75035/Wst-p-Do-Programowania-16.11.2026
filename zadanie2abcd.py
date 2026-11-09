#zadanie2a

#Stwórz listę z imionami 4 osób.  
#a. Posortuj ją alfabetycznie i wyświetl,  

imiona = ["Piotr", "Anna", "Krzysztof", "Ewa"]

imiona.sort()
print("a. Posortowane:", imiona)



#zadanie2b

#Stwórz listę z imionami 4 osób.  
#b. Dodaj na końcu dwie osoby i pobierz ostatnią z nich poleceniem pop().  


imiona.append("Zofia")
imiona.append("Jan")
ostatnia_osoba = imiona.pop()
print("b. Pobrana ostatnia osoba:", ostatnia_osoba)



#zadanie2c

#Stwórz listę z imionami 4 osób. 
#c. Na pozycji 3 dodaj jeszcze jedną osobę.  


imiona.insert(2, "Michał")
print("c. Po dodaniu na pozycji 3:", imiona)



#zadanie2d

#d. Odwróć kolejność na liście i zdubluj ją. 

imiona.reverse()
imiona_zdublowane = imiona * 2
print("d. Odwrócone i zdublowane:", imiona_zdublowane)

