import spotipy
from typing import List, Dict

def get_recent_tracks(sp: spotipy.Spotify, limit: int = 50) -> List[Dict]:
    results = sp.current_user_recently_played(limit=limit)
    return results.get('items', [])

def get_top_tracks(sp: spotipy.Spotify, time_range: str = "medium_term", limit: int = 20) -> List[Dict]:
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    return results.get('items', [])