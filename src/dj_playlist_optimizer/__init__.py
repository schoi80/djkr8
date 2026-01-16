"""DJ Playlist Optimizer - Harmonic mixing with Google OR-Tools."""

from dj_playlist_optimizer.models import (
    HarmonicLevel,
    PlaylistResult,
    PlaylistStatistics,
    Track,
    TransitionInfo,
)
from dj_playlist_optimizer.optimizer import PlaylistOptimizer
from dj_playlist_optimizer.camelot import (
    parse_camelot_key,
    is_harmonic_compatible,
    get_compatible_keys,
)
from dj_playlist_optimizer.bpm import bpm_compatible, get_bpm_difference

__version__ = "0.1.0"

__all__ = [
    "PlaylistOptimizer",
    "Track",
    "PlaylistResult",
    "PlaylistStatistics",
    "TransitionInfo",
    "HarmonicLevel",
    "parse_camelot_key",
    "is_harmonic_compatible",
    "get_compatible_keys",
    "bpm_compatible",
    "get_bpm_difference",
]
