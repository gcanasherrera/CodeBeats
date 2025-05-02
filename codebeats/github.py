import requests
from typing import List, Dict, Set

def get_commit_activity(username: str, token: str) -> List[Dict]:
    headers = {'Authorization': f'token {token}'}
    events = []
    url = f"https://api.github.com/users/{username}/events"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        for event in r.json():
            if event['type'] == 'PushEvent':
                for commit in event['payload']['commits']:
                    events.append({
                        'repo': event['repo']['name'],
                        'timestamp': event['created_at'],
                    })
    return events

def get_active_days(commits: List[Dict]) -> Set[str]:
    return {c['timestamp'][:10] for c in commits}  # YYYY-MM-DD