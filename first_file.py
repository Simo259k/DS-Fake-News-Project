data = ["Simon", "William", "Emil","Simon 2.0"]

# Find den person med det første forbogstav
min_name = min(data)  # min() sammenligner alfabetisk
data.remove(min_name)  # Fjern personen fra sin nuværende placering
data.insert(0, min_name)  # Tilføj personen forrest

if len(data) == 4:
    print("Accepted group size")
else:
    print("Max 4, min 4")

print(data)

