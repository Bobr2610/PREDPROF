import csv
with open('songs.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    data = list(reader)
artist_name = input()
while artist_name != '0':
    artist_name = artist_name
    for el in data:
        if el['artist_name'] == artist_name:
            track_name = el["track_name"].split()
            print(f"У artist_name найдена песня: {track_name}")
            break
    else:
        print('Ничего не найдено')
    id_project = input()