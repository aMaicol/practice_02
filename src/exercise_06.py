import re

posts = [
    "Arrancando el lunes con energía #Motivación #NuevaSemana",
    "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
    "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
    "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
    "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
    "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
    "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
    "Finde de lluvia, maratón de series #SerieAdicta #Relax",
    "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación",
]

trending = dict()

for post in posts:
    lista_hashtags = re.findall(r"#\w+", post)

    for hashtag in lista_hashtags:
        trending[hashtag] = trending.get(hashtag, 0) + 1

print("Los hashtags trending son:")

for hashtag, cant in trending.items():
    if cant > 1:
        print(f"{hashtag}: {cant}")

print(f"Total de hashtags (sin repetirse): {len(trending)}")
