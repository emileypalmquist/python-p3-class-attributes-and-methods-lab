class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.update_count()
        Song.add_genre(genre)
        Song.add_artist(artist)
        Song.update_genre_count(genre)
        Song.update_artist_count(artist)

    @classmethod
    def update_count(cls):
        cls.count += 1

    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

        if not cls.genre_count.get(genre):
            cls.genre_count[genre] = 0

    @classmethod
    def add_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

        if not cls.artist_count.get(artist):
            cls.artist_count[artist] = 0

    @classmethod
    def update_genre_count(cls, genre):
        cls.genre_count[genre] += 1

    @classmethod
    def update_artist_count(cls, artist):
        cls.artist_count[artist] += 1
