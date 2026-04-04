import random


def amigo_invisible(names):
    mixed = names.copy()
    random.shuffle(mixed)

    print("Sorteo de amigo invisible:")

    for i in range(len(mixed)):
        regala = mixed[i]
        recibe = mixed[(i + 1) % len(mixed)]

        print(f"{regala} → {recibe}")


names = input("Ingrese los participantes (separados por coma): ")

list_names = [name.title() for n in names.split(",") if (name := n.strip())]

if len(list_names) < 3:
    print("Error: hay menos de tres participantes.")
elif len(set(list_names)) != len(list_names):
    print("Error: hay nombres duplicados.")
else:
    amigo_invisible(list_names)
