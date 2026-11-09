#zadanie7
#Posortu krotke moja_krotka= (10, 2, 6, 6, 9, 13, 0,1), operacji tej dokonaj posługując się pomocniczo listą 

moja_krotka = (10, 2, 6, 6, 9, 13, 0, 1)

lista_pomocnicza = list(moja_krotka)
lista_pomocnicza.sort()

posortowana_krotka = tuple(lista_pomocnicza)
print("Posortowana krotka:", posortowana_krotka)