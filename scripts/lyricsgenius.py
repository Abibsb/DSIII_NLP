import lyricsgenius
genius = lyricsgenius.Genius('zNPN5vfP2kxGma0MpZ_6Td1-7aSgaVMl-ziucTzxdVpXyKgcdwUpGlBemADCZTXh')

artist = genius.search_artist("St. Vincent", max_songs=3, sort="title")
print(artist.songs)

song = artist.song("Actor Out of Work")
print(song.lyrics)

album = genius.search_album("St. Vincent", "St. Vincent")
album.save_lyrics()

albums = ["Marry Me", "Actor", "Strange Mercy", "St. Vincent (Deluxe Edition)", "MASSEDUCTION", "Daddy's Home", "All Born Screaming", "Krokodil - Single", "Ratsliveonnoevilstar - EP", "The Nowhere Inn"]

for album_title in albums:
    album = genius.search_album(album_title, "St. Vincent")
    album.save_lyrics()
