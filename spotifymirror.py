import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tokenspotify import id, secret
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import time
import googleapiclient.errors

def safe_execute(request, retries=3, delay=2):
    for i in range(retries):
        try:
            return request.execute()
        except googleapiclient.errors.HttpError as e:
            if e.resp.status in [409, 500, 503]: #look for internal server errors or conflicts
                print(f"Temporary error: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2 
            else:
                raise
    raise Exception("Failed after retries") #if all retries fail, raise an exception of custom error message

auth_manager = SpotifyClientCredentials(
    client_id=id,
    client_secret=secret
) #auth_manager is used to authenticate the Spotify API client using the client ID and secret from tokenspotify.py
sp = spotipy.Spotify(auth_manager=auth_manager)
# sp is the Spotify API client that allows you to interact with Spotify's web API.
playlist_id = input("Enter your spotify playlist ID: ")

playlist = sp.playlist_tracks(playlist_id) # This retrieves the tracks from the specified Spotify playlist.

TrackList = []
for item in playlist["items"]:
    track = item["track"]
    name = track['name']
    artists = ', '.join(artist['name'] for artist in track['artists'])
    TrackList.append([name, artists]) # This creates a list of tracks with their names and artists from the playlist.

NewTracklist = []
for track in TrackList:
    NewTracklist.append(track[0] + " by " + track[1]) # This formats each track as "Track Name by Artist Name" and adds it to a new list.


SCOPES = ["https://www.googleapis.com/auth/youtube"]
# This scope allows the application to manage YouTube resources.
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES)
creds = flow.run_local_server(port=0)
#opens up a local server to authenticate the user and get credentials.
youtube = build('youtube', 'v3', credentials=creds)
# This builds the YouTube API client using the credentials obtained from the OAuth flow.





def youtube_search(youtube, options):
     # Call the search.list method to retrieve results matching the specified
    # query term.
    request = youtube.search().list(
        q = options,
        part = "snippet",
        maxResults = 1,
        type = "video"
    )
# youtube.search().list(...) sets up a YouTube API request to search for videos.
# q=query: The search term. Example: "Blinding Lights The Weeknd"
# part="snippet": You’re asking for basic details like title, channel name, etc.
# maxResults=1: Only return the top 1 result
# type="video": Only search for actual videos (not playlists, channels, etc.)
    response = safe_execute(request)
    # Execute the request and get the response json file.
    items = response.get("items", [])
    #check if there are any items in the response, if not they return an empty list.
    if items:
        return items[0]["id"]["videoId"]
    #returns the number 1 result and unique video ID from the response.
    else:
        return None
    

def create_youtube_playlist(youtube, title, description):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            'snippet': {
                'title': title,
                'description': description
            },
            'status': {
                'privacyStatus' : 'private'
            }
        })
    response = safe_execute(request)
    return response['id']

def add_video_to_playlist(youtube, playlist_id, video_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            'snippet':{
                'playlistId': playlist_id,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id
                }
            }
        }
    )
    response = safe_execute(request)

playlist_title = input("Enter the title for your YouTube playlist: ")
description = "hi"
yt_playlist_id = create_youtube_playlist(youtube, playlist_title, description)
for track in NewTracklist:
    video_id = youtube_search(youtube, track)
    if video_id:
        add_video_to_playlist(youtube,yt_playlist_id, video_id)
        print("Added video for:", track)
    else:
        print("No video found for:", track)
print("Playlist created with ID:", yt_playlist_id)  


