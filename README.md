# SpotifyMirror

This Python script transfers a public **Spotify playlist** into a **YouTube playlist** by:

1. Extracting song titles and artists from a Spotify playlist
2. Searching each song on YouTube
3. Creating a new YouTube playlist on your account
4. Adding the first video result for each song into the playlist

##Requirements

- A **Spotify Developer Account** : https://developer.spotify.com/dashboard
- A **Google Cloud Project with Youtube API v3** : https://console.cloud.google.com/

You will need:
- Your Spotify **Client ID** and **Client Secret**
- Your YouTube API **client_secret.json** file (OAuth 2.0 credentials)

#Dependencies required 
- spotipy
- google-auth-oauthlib
- google-api-python-client
- time

When setting up:
- Make sure to replace the variables "id" and "secret" to your respected id and secret generated from spotify developer portal
- Make sure to replace the client_secret json file generated from google cloud dashboard

##Keywords
spotify api, youtube data api, playlist converter, spotify to youtube, music playlist transfer, python automation, youtube playlist script, spotify mirror, public playlist, youtube api v3
