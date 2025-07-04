import requests
import base64

# 1. Spotify Developer panelinden alacağın bilgileri buraya yaz
CLIENT_ID = 'aaaaaaa'
CLIENT_SECRET = 'aaaaaa'

def get_access_token(client_id, client_secret):
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth_str}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    res = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    res_json = res.json()
    return res_json.get("access_token")

def get_track_info(track_id, access_token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    res = requests.get(url, headers=headers)
    return res.json()

def main():
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    if not access_token:
        print("Access token alınamadı, bilgileri kontrol et.")
        return

    track_id = "track id"       # Buraya sorgulamak istediğin şarkının ID'sini yaz
    track_info = get_track_info(track_id, access_token)

    if "name" in track_info:
        print("Track Title:", track_info["name"])
        artists = ", ".join(artist["name"] for artist in track_info["artists"])
        print("Artist(s):", artists)
    else:
        print("Şarkı bilgisi alınamadı:", track_info)

if __name__ == "__main__":
    main()
