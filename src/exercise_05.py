kg = float(input("Ingrese el peso del paquete: "))
zonas = ("local", "regional", "nacional")
destino = input(f"Ingrese la zona de destino {zonas}: ").lower()

if destino not in zonas:
    print("Error. Ingrese una zona válida.")
else:
    prices = {
        "hasta_uno": {"local": 500, "regional": 1000, "nacional": 2000},
        "de_uno_a_cinco": {"local": 1000, "regional": 2500, "nacional": 4500},
        "mas_de_cinco": {"local": 2000, "regional": 5000, "nacional": 8000},
    }

    if kg <= 1:
        cat = "hasta_uno"
    elif kg <= 5:
        cat = "de_uno_a_cinco"
    else:
        cat = "mas_de_cinco"

    print(f"Costo de envío: ${prices[cat][destino]}")
