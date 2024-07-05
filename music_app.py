class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.playlists = []
        self.failed_attempts = 0
        self.locked = False

    def create_playlist(self, playlist_name):
        playlist = Playlist(playlist_name)
        self.playlists.append(playlist)
        return playlist

    def authenticate(self, password):
        if self.locked:
            return "User locked"
        if self.password == password:
            self.failed_attempts = 0
            return "Login successful"
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                self.locked = True
                return "User locked"
            return "Incorrect password"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play(self):
        for song in self.songs:
            print(f"Playing {song.title} by {song.artist}")

class MusicApp:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register_user(self, username, password):
        if username in self.users:
            return "Username already exists"
        self.users[username] = User(username, password)
        return "User registered successfully"

    def login_user(self, username, password):
        if username not in self.users:
            return "Username does not exist"
        return self.users[username].authenticate(password)

    def create_playlist(self, playlist_name):
        if self.current_user is None:
            return "No user is currently logged in"
        return self.current_user.create_playlist(playlist_name)

    def add_song_to_playlist(self, playlist_name, song):
        if self.current_user is None:
            return "No user is currently logged in"
        for playlist in self.current_user.playlists:
            if playlist.name == playlist_name:
                playlist.add_song(song)
                return "Song added to playlist"
        return "Playlist not found"

    def play_playlist(self, playlist_name):
        if self.current_user is None:
            return "No user is currently logged in"
        for playlist in self.current_user.playlists:
            if playlist.name == playlist_name:
                playlist.play()
                return "Playing playlist"
        return "Playlist not found"
