# Before you can use the jobs API, you need to set up an access token.
# Log in to the IBM Q experience. Under "Account", generate a personal 
# access token. Replace 'PUT_YOUR_API_TOKEN_HERE' below with the quoted
# token string. Uncomment the APItoken variable, and you will be ready to go.

APItoken = 'ae0099f2355e7a4ab53fc610aaabb0c5bb8cba6ca57c128e4d2ce0b1c9995b5c15504ebaf9fab8b6a97472684c15e5924277d4dea3a892dc2f247ba117bda756'

config = {
    'url': 'https://quantumexperience.ng.bluemix.net/api',
}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
