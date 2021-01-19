"""DOOMBot class."""
from typing import List

import config
import lyricsgenius
import lyricsgenius.song
import tweepy
import random

# We hard-code this to avoid "non-canon" albums. List of tuples (album_id, artist_id).
DISCOGRAPHY = [(5645, 70),  # Operation: Doomsday, MF DOOM
               (5658, 708),  # Take Me To Your Leader, King Geedorah
               (5665, 712),  # Vaudeville Villain, Viktor Vaughn
               (5668, 712),  # VV:2, Viktor Vaughn
               (5651, 70),  # MM...FOOD, MF DOOM
               (5643, 70),  # Born Like This, DOOM
               (5647, 150),  # Madvillainy, Madvillain
               (5666, 1277),  # The Mouse and the Mask, Danger Doom
               (20091, 23344)]  # Keys to the Kuffs, JJ Doom


class DOOMBot:
    """
    Uses the lyricsgenius package and genius.com API to generate a tweet of random MF DOOM lyrics
    with associated info (track name, album name, etc.). Uses tweepy package to post tweets.
    """

    def __init__(self):
        """
        Initializes bot. Calls helper initialization methods to set up communication
        with APIs using keys imported from `config.py`.
        """
        # Set up Twitter API communication.
        auth = tweepy.OAuthHandler(config.twitter_api_key, config.twitter_api_key_secret)
        auth.set_access_token(config.twitter_access_token, config.twitter_access_token_secret)
        self.twitter = tweepy.API(auth)

        # Set up Genius API communuciation.
        self.genius = lyricsgenius.Genius(config.genius_client_access_token)

        # Set discography. List of tuples (album_id, artist_id), hard-coded above.
        self.discography = DISCOGRAPHY

    def select_song(self):
        """
        Selects a random song from the discography.
        :return: A dictionary object representing the song selected.
        """
        print("Selecting a song...")

        # Select random album.
        print("\tFirst, selecting a random album...")
        album: dict = self.genius.album(random.choice(self.discography)[0])['album']
        print("\t\tAlbum Selected: " + album['name'] + " (ID = " + str(album['id']) + ")")

        # Select song from album.
        print("\tNow, selecting a random song from the album...")

        # Define function to check that a track is a song.
        def is_song(track_to_check: dict):
            search_terms = ['track\\s?list', 'album art(work)?', 'liner notes',
                            'booklet', 'credits', 'interview', 'skit',
                            'instrumental', 'setlist', 'remix', 'version']
            for term in search_terms:
                if term in track_to_check['song']['title'].lower():
                    return False
                else:
                    pass
            return True

        songs: List[dict] = list(filter(is_song, self.genius.album_tracks(album['id'])['tracks']))
        song: dict = random.choice(songs)['song']
        print("\t\tSong Selected: " + song['title'] + " (ID = " + str(song['id']) + ")")
        return song
        # lyrics: str = self.genius.lyrics(song['url'])
        # print(lyrics.split("\n"))


def main():
    print("Testing...")
    bot = DOOMBot()
    bot.select_song()


if __name__ == '__main__':
    main()
