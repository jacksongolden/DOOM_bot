import requests


# -------------------- RAPID API SETUP --------------------
# The url of the API to be queried and query parameters
api_url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
headers = {
    'x-rapidapi-key': "6db516ad83msh3e323dc5eee0c95p1acafajsn6445775526b7",
    'x-rapidapi-host': "andruxnet-random-famous-quotes.p.rapidapi.com"
}
querystring = {"count": "1"}        # Get just one recipe
# ---------------------------------------------------------

# -------------------- FUNCTIONS ----- --------------------


# Gets a random quote from the API and returns tweet object (string-ish)
def get_quote():
    response = requests.get(api_url, headers=headers, params=querystring)
    json = response.json()[0]
    tweet = json['quote'] + '-' + json['author']
    return tweet
