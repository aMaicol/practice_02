playlist = [
    {"title": "Bohemian Rhapsody", "duration": "5:55"},
    {"title": "Hotel California", "duration": "6:30"},
    {"title": "Stairway to Heaven", "duration": "8:02"},
    {"title": "Imagine", "duration": "3:07"},
    {"title": "Smells Like Teen Spirit", "duration": "5:01"},
    {"title": "Billie Jean", "duration": "4:54"},
    {"title": "Hey Jude", "duration": "7:11"},
    {"title": "Like a Rolling Stone", "duration": "6:13"},
]

total_time = 0
long_song = playlist[0]
short_song = playlist[0]

long_time = long_song["duration"].split(":")
long_time = int(long_time[0]) * 60 + int(long_time[1])
short_time = long_time

for n in playlist:
    time = n["duration"].split(":")
    song_time = int(time[0]) * 60 + int(time[1])
    total_time += song_time

    if song_time > long_time:
        long_time = song_time
        long_song = n

    if song_time < short_time:
        short_time = song_time
        short_song = n

total_minutes, total_seconds = divmod(total_time, 60)

print(f"La duración total es: {total_minutes}m {total_seconds}s")
print(f"La canción más larga es: {long_song['title']} con {long_song['duration']}")
print(f"La canción más corta es: {short_song['title']} con {short_song['duration']}")
