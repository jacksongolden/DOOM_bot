import config
import random
from lyricsgenius import Genius

# -------------------- GENIUS API SETUP -----------------
genius_client_id = config.genius_client_id
genius_client_secret_id = config.genius_client_secret_id
genius_client_access_token = config.genius_client_access_token
# -------------------------------------------------------

# Set "MF DOOM" artist_id
DOOM_ARTIST_ID = 70


def get_tweet_info():
    # Create a new genius object
    genius = Genius(client_access_token)

    # Pick a random song until we find one that has annotations (shouldn't take long)
    print("Looking for annotations ...")
    while True:
        # Narrow selection by picking an album
        albums = genius.artist_albums(DOOM_ARTIST_ID)
        selected_album = random.choice(albums['albums'])
        print("\tALBUM: " + selected_album['name'])

        # Get the songs from the album and pick one
        tracks = genius.album_tracks(selected_album['id'])
        selected_track = random.choice(tracks['tracks'])
        selected_song = selected_track['song']
        print("\tSONG: " + selected_song['title_with_featured'])

        # Try to get an annotated lyric
        annotation_count = selected_song['annotation_count']
        print("\t\t" + str(annotation_count) + " annotations found...")

        # If we found a song with annotations, continue; otherwise, try again
        if selected_song['annotation_count'] > 10:
            break
        else:
            print("Trying again...")

    # Pick a random annotation for the selected song
    selected_lyric = random.choice(genius.song_annotations(selected_song['id']))[0]
    tweet_text = selected_lyric + "\n\n(" + selected_song['title_with_featured'] + ", " + selected_album['name'] + ")"
    return tweet_text


def main():
    genius = Genius(genius_client_access_token)
    album = genius.search_albums("Keys to the Kuffs")
    print(album)

if __name__ == '__main__':
    main()