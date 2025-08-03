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

#When setting up:
- Make sure to replace the variables "id" and "secret" to your respected id and secret generated from spotify developer portal
- Make sure to replace the client_secret json file generated from google cloud dashboard

#SpotifyID
- When copying spotify ID, make sure to click "Share playlist" from the spotifty app and click the link which will open it on a new website. Then copy the ID onward starting from playlist/.
- Example: In the link "https://open.spotify.com/playlist/0o4tHrkcQ3BsZU9EU843Bs", you should copy  "0o4tHrkcQ3BsZU9EU843Bs" as ID. 

#ErrorsCheckings
- The "safe_execute" function make sure to check for the internal server errors from Youtube side such as error 409, 500, 503. We bypass these error by waiting/delaying the request time and retrying again.
- If an unknown error occurs, the scrpit should skip the song that couldn't for example, be found and move on to the next song. 

##Keywords
spotify api, youtube data api, playlist converter, spotify to youtube, music playlist transfer, python automation, youtube playlist script, spotify mirror, public playlist, youtube api v3
