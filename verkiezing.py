print("0. Stoppen")
print("1. Rutte")
print("2. Den Uyl")
print("3. Henk")
print("4. Theo")
print("5. Klaas")

keuze = 9
kvs = ["Rutte", "Den Uyl, Henk, Theo, Klaas"]
keuzes = []
aantal_gekozen = []

while keuze != 0:
    keuze = int(input("Kies een nieuwe klassenvertegenwoordiger (1,2,3,4 en 5)"))
    keuzes.append(keuze)

print(keuzes)
print(f"Rutte is {keuzes.count(1)} keer gekozen")
print(f"Den Uyl is {keuzes.count(2)} keer gekozen")
print(f"Henk is {keuzes.count(3)} keer gekozen")
print(f"Theo is {keuzes.count(4)} keer gekozen")
print(f"Klaas is {keuzes.count(5)} keer gekozen")
aantal_gekozen.append(keuzes.count(1))
aantal_gekozen.append(keuzes.count(2))
aantal_gekozen.append(keuzes.count(3))
aantal_gekozen.append(keuzes.count(4))
aantal_gekozen.append(keuzes.count(5))
aantal_gekozen.sort(reverse=True)
print(aantal_gekozen)