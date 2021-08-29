def my_mp4_playlist(file_path, new_song):
    with open(file_path,'r') as songs:
        new_list = parse_songs(songs)
        while len(new_list) < 3:
            new_list.append(['','','','\n'])
        new_list[2][0] = new_song
    with open(file_path,'w') as songs:
        for s in new_list:
            songs.write("{};{};{};\n".format(s[0],s[1],s[2]))
    with open(file_path,'r') as songs:
        print(songs.read().replace(",;",",").replace(";;;",";"))


def parse_songs(songs):
    new_list = []
    for line in songs:
        new_list.append(parse_song(line))
    return new_list

def parse_song(song):
    ls = list(song.split(";"))
    return ls

