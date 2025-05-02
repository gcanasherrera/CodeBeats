from collections import Counter
from typing import List, Dict, Set

def correlate_tracks_with_activity(tracks: List[Dict], active_days: Set[str]) -> Dict[str, int]:
    counter = Counter()
    for track in tracks:
        played_at = track.get('played_at', '')[:10]  # YYYY-MM-DD
        if played_at in active_days:
            name = track['track']['name']
            counter[name] += 1
    return dict(counter.most_common())

def generate_summary(stats_dict: Dict[str, int]) -> str:
    lines = [f"{name}: {count} plays" for name, count in stats_dict.items()]
    return "\n".join(lines)