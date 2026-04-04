import re

review = """La película sigue a un grupo de astronautas que viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo a través
de tormentas solares y fallos en el sistema de navegación. Al llegar
a Marte descubren que la base está abandonada y los suministros
destruidos. Torres decide sacrificar la nave nodriza para salvar
al equipo y logran volver a la Tierra en una cápsula de emergencia.
El final revela que Torres sobrevivió gracias a un pasaje secreto."""

spoilers_raw = input("Ingrese las palabras spoiler (separadas por comas): ")
spoilers = [s.strip() for s in spoilers_raw.split(",")]
for word in spoilers:
    # No reemplaza palabras con tilde.
    review = re.sub(word, "*" * len(word), review, flags=re.IGNORECASE)

print()
print(review)
