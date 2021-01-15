import random
from lyricsgenius import Genius

# -------------------- GENIUS API SETUP -----------------
client_id = "LqaxuVXGuYxoMR_nC2N8J0Ftte6snKzPJLeldHGx8xl5HFY3M7ba-_RYbO9ZSsk7"
client_secret_id = "db5KzQ9ljW_cIozFoQflej8SnqC3QL-Hm_8dtDr8VcpaPrOZMmhiGCjCWxCjaA57pK6D9TFat3OWxftZ09hxcw"
client_access_token = "x8UFMB2mi14fkP7KeCYBcvsteIMQ_0cG7LOTEJN-EqudunfTQp0LhUNqxl_arABr"
# -------------------------------------------------------

# Set "MF DOOM" artist_id
DOOM_ARTIST_ID = 70


def make_tweet():
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
    tweet = selected_lyric + "\n\n(" + selected_song['title_with_featured'] + ", " + selected_album['name'] + ")"
    return tweet
