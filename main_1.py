import csv

with open('songs.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    answer = list(reader)[1:]
    for streams, artist_name, track_name, date in answer:
        if int(date[-4:]) >= 2002:
            if int(date[-7:-5]) >= 1:
                if int(date[:2]) >= 1:
                    print(f"{track_name} - {artist_name} - {streams}")
    sum_song = {}
    sum_name = {}
    e = {}
    for el in answer:
        sum_song[el[1]] = len(str(sum_song.get(el[1], 'unknown')))
        sum_name[el[1]] = len(str(sum_song.get(el[1], 'unknown')))
        date = el[-1]
        if int(date[-4:]) >= 2002:
            if int(date[-7:-5]) >= 1:
                if int(date[:2]) >= 1:
                    e[el[1]] = (int(date[-4:])*12*30 + int(date[-7:-5])* 30 + int(date[:2]) - (2002*12*60 + 30 + 1))
    for el in answer:
        if el[1] == 0:
            if e[el[1]] > 0:
                el[1] = e[el[1]] / (sum_song[el[1]] + sum_name[el[1]])
            else:
                el[1] = (0 - e[el[1]]) / (sum_song[el[1]] + sum_name[el[1]])
with open('songs_new.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerow(['streams', 'artist_name', 'track_name', 'date'])
    w.writerows(answer)