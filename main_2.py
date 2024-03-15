import csv
with open('songs.csv', encoding="utf8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=';', quotechar='"'))
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while float(reader[j]['date'] < key['date']) and j >= 0:
            reader[j + 1] = reader[j]
            j -= 1
        reader[j + 1] = key
count = 1
for el in reader:
    if '10' in el['date']:
        date = str(el["date"].split('.'))[2:-2]
        track_name = str(el["track_name"].split('.'))[1:-1]
        artist_name = str(el["artist_name"].split('.'))[1:-1]
        print(f'{j} {track_name}, {artist_name}, {date}')
        count += 1
    if count == 4:
        break