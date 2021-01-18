import config
import random
from lyricsgenius import Genius
from lyricsgenius.artist import Artist

# -------------------- GENIUS API SETUP -----------------
genius_client_id = config.genius_client_id
genius_client_secret_id = config.genius_client_secret_id
genius_client_access_token = config.genius_client_access_token
# -------------------------------------------------------

# -------------------- PARAMETERS -----------------------
# Dictionary for holding map from DOOM name / alias to Genius artist_id.
identities = {"MF DOOM": 70}

DOOM_ARTIST_ID = 70

# Number of annotations a song must have to "qualify"
MIN_ANNOTATIONS = 5

# Size of snippet to look for
MIN_LYRIC_LENGTH = 50
MAX_LYRIC_LENGTH = 150


# -------------------------------------------------------

def get_tweet_info():
    # Create a new genius object
    genius = Genius(genius_client_access_token)

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

        # Check that the song has a "qualifying" number of annotations and they are of right length
        annotation_count = selected_song['annotation_count']
        print("\t\t" + str(annotation_count) + " annotations found...")

        # If we found a song with sufficient annotations, continue; otherwise, try again
        if selected_song['annotation_count'] >= MIN_ANNOTATIONS:

            # Pick a random annotation for the selected song
            selected_lyric = random.choice(genius.song_annotations(selected_song['id']))[0]
            tweet_text = selected_lyric + "\n\n(" + selected_song['title_with_featured'] + ", " + selected_album[
                'name'] + ")"
            return tweet_text

        else:
            print("Trying again...")


# -------------------- FOR TESTING ----------------------
def main():
    get_tweet_info()


if __name__ == '__main__':
    main()
# -------------------------------------------------------
