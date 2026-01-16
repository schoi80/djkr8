"""Rekordbox 6 database loader."""

import logging
from dataclasses import dataclass

from dj_playlist_optimizer.models import Track

try:
    from pyrekordbox import Rekordbox6Database

    HAS_PYREKORDBOX = True
except ImportError:
    HAS_PYREKORDBOX = False
    Rekordbox6Database = None

logger = logging.getLogger(__name__)


# Mapping from standard musical keys to Camelot notation
KEY_MAPPING = {
    # Major Keys
    "B": "1B",
    "B Major": "1B",
    "B Maj": "1B",
    "F#": "2B",
    "F# Major": "2B",
    "F# Maj": "2B",
    "Gb": "2B",
    "Gb Major": "2B",
    "Gb Maj": "2B",
    "Db": "3B",
    "Db Major": "3B",
    "Db Maj": "3B",
    "C#": "3B",
    "C# Major": "3B",
    "C# Maj": "3B",
    "Ab": "4B",
    "Ab Major": "4B",
    "Ab Maj": "4B",
    "G#": "4B",
    "G# Major": "4B",
    "G# Maj": "4B",
    "Eb": "5B",
    "Eb Major": "5B",
    "Eb Maj": "5B",
    "D#": "5B",
    "D# Major": "5B",
    "D# Maj": "5B",
    "Bb": "6B",
    "Bb Major": "6B",
    "Bb Maj": "6B",
    "A#": "6B",
    "A# Major": "6B",
    "A# Maj": "6B",
    "F": "7B",
    "F Major": "7B",
    "F Maj": "7B",
    "C": "8B",
    "C Major": "8B",
    "C Maj": "8B",
    "G": "9B",
    "G Major": "9B",
    "G Maj": "9B",
    "D": "10B",
    "D Major": "10B",
    "D Maj": "10B",
    "A": "11B",
    "A Major": "11B",
    "A Maj": "11B",
    "E": "12B",
    "E Major": "12B",
    "E Maj": "12B",
    # Minor Keys
    "Abm": "1A",
    "Ab Minor": "1A",
    "Ab Min": "1A",
    "G#m": "1A",
    "G# Minor": "1A",
    "G# Min": "1A",
    "Ebm": "2A",
    "Eb Minor": "2A",
    "Eb Min": "2A",
    "D#m": "2A",
    "D# Minor": "2A",
    "D# Min": "2A",
    "Bbm": "3A",
    "Bb Minor": "3A",
    "Bb Min": "3A",
    "A#m": "3A",
    "A# Minor": "3A",
    "A# Min": "3A",
    "Fm": "4A",
    "F Minor": "4A",
    "F Min": "4A",
    "Cm": "5A",
    "C Minor": "5A",
    "C Min": "5A",
    "Gm": "6A",
    "G Minor": "6A",
    "G Min": "6A",
    "Dm": "7A",
    "D Minor": "7A",
    "D Min": "7A",
    "Am": "8A",
    "A Minor": "8A",
    "A Min": "8A",
    "Em": "9A",
    "E Minor": "9A",
    "E Min": "9A",
    "Bm": "10A",
    "B Minor": "10A",
    "B Min": "10A",
    "F#m": "11A",
    "F# Minor": "11A",
    "F# Min": "11A",
    "Gbm": "11A",
    "Gb Minor": "11A",
    "Gb Min": "11A",
    "Dbm": "12A",
    "Db Minor": "12A",
    "Db Min": "12A",
    "C#m": "12A",
    "C# Minor": "12A",
    "C# Min": "12A",
}


@dataclass
class PlaylistInfo:
    """Basic info about a Rekordbox playlist."""

    id: str
    name: str
    path: str
    count: int


class RekordboxLoader:
    """Handles interaction with Rekordbox 6 database."""

    def __init__(self):
        if not HAS_PYREKORDBOX:
            raise ImportError(
                "pyrekordbox is not installed. Install with 'pip install pyrekordbox'"
            )
        try:
            self.db = Rekordbox6Database()
        except Exception as e:
            # Often fails if configuration file is missing or db locked
            raise RuntimeError(f"Failed to initialize Rekordbox database: {e}") from e

    def _convert_key(self, key_str: str | None) -> str:
        """Convert Rekordbox tonality to Camelot key."""
        if not key_str:
            return ""

        # Already in Camelot? (e.g. "8A", "12B")
        if key_str[0].isdigit() and key_str[-1] in ("A", "B"):
            return key_str

        return KEY_MAPPING.get(key_str, key_str)

    def list_playlists(self) -> list[PlaylistInfo]:
        """List all available playlists in the database."""
        playlists = []

        # pyrekordbox get_playlist() returns a list of playlist objects
        # The structure is hierarchical, but we'll try to flatten or just show top/relevant ones
        # For simplicity, let's just get the flat list if possible or walk the tree
        # Using the standard iterator which usually walks everything

        for pl in self.db.get_playlist():
            # Filter out folders or root
            if pl.Name == "ROOT":
                continue

            # Calculate full path or just use name
            # Assuming flat list for now or just top level
            try:
                count = len(pl.Songs) if hasattr(pl, "Songs") else 0
                playlists.append(
                    PlaylistInfo(
                        id=str(pl.ID),
                        name=pl.Name,
                        path=pl.Name,  # Ideally we'd construct the path
                        count=count,
                    )
                )
            except Exception as e:
                logger.warning(f"Error reading playlist {pl.Name}: {e}")

        return playlists

    def get_tracks(self, playlist_name: str) -> list[Track]:
        """Get tracks from a specific playlist by name."""
        target_pl = None
        for pl in self.db.get_playlist():
            if pl.Name == playlist_name:
                target_pl = pl
                break

        if not target_pl:
            raise ValueError(f"Playlist '{playlist_name}' not found")

        tracks = []
        for song in target_pl.Songs:
            content = song.Content

            if not content:
                continue

            try:
                # Rekordbox specific fields
                title = content.Title or "Unknown"
                artist = content.Artist.Name if content.Artist else "Unknown"
                track_id = f"{artist} - {title}"

                bpm_raw = content.BPM or 0
                bpm_val = bpm_raw / 100.0 if bpm_raw > 200 else float(bpm_raw)

                key_raw = getattr(content, "KeyName", None)
                if not key_raw:
                    key_raw = getattr(content, "Tonality", None)

                key = self._convert_key(key_raw)

                if not key or bpm_val <= 0:
                    logger.warning(
                        f"Skipping track {track_id}: Missing Key ({key_raw}) or BPM ({bpm_val})"
                    )
                    continue

                tracks.append(
                    Track(
                        id=track_id,
                        key=key,
                        bpm=bpm_val,
                        energy=int(content.Rating or 0),
                        duration=float(content.Length or 0),
                    )
                )
            except Exception as e:
                logger.warning(f"Error parsing track in playlist: {e}")
                continue

        return tracks
