from operator import itemgetter


def my_mp3_playlist(file_path):
    songs = []
    with open(file_path,'r') as songs:
        new_list = parse_songs(songs)
        longes_song_name = sorted(new_list,key=itemgetter(2))[-1][0]
        number_of_songs = len(new_list)
        performer = big_performer(new_list)
        return (longes_song_name, number_of_songs, performer)
        


def parse_songs(songs):
    new_list = []
    for line in songs:
        new_list.append(parse_song(line))
    return new_list

def parse_song(song):
    ls = list(song.split(";"))
    return ls

def big_performer(songs):
    my_dict = {}
    for song in songs:
        if song[1] in my_dict:
            my_dict[song[1]] += 1
        else:
            my_dict[song[1]] = 1
    max = 0
    performer = ""
    for p, n in my_dict.items():
        if n > max:
            max = n
            performer = p
    return performer
