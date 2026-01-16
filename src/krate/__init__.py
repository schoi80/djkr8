"""DJ Playlist Optimizer - Harmonic mixing with Google OR-Tools."""

from krate.bpm import bpm_compatible, get_bpm_difference
from krate.camelot import (
    get_compatible_keys,
    is_harmonic_compatible,
    parse_camelot_key,
)
from krate.models import (
    HarmonicLevel,
    PlaylistResult,
    PlaylistStatistics,
    Track,
    TransitionInfo,
)
from krate.optimizer import PlaylistOptimizer

__version__ = "0.1.0"

__all__ = [
    "HarmonicLevel",
    "PlaylistOptimizer",
    "PlaylistResult",
    "PlaylistStatistics",
    "Track",
    "TransitionInfo",
    "bpm_compatible",
    "get_bpm_difference",
    "get_compatible_keys",
    "is_harmonic_compatible",
    "parse_camelot_key",
]
