#zadanie9
#Stwórz listę zakupów jako słownik (artykuł : kwota). Wyświetl go i podsumuj wydatki. 

lista_zakupow = {
    "Chleb": 4.50,
    "Mleko": 3.20,
    "Ser zolty": 12.00,
    "Sound Blaster ae 7": 8.50,
    "Maslo": 7.00
}

print("Lista zakupów:")
for artykul, kwota in lista_zakupow.items():
    print(f"- {artykul}: {kwota} zł")

podsumowanie = sum(lista_zakupow.values())
print(f"\nPodsumowanie wydatków: {podsumowanie} zł")