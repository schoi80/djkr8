# 🎧 DJ Playlist Optimizer

Optimize DJ playlists for harmonic mixing using Google OR-Tools constraint programming.

## Features

- ✨ **Longest Path Optimization**: Finds the maximum number of tracks that can be mixed together
- 🎵 **Harmonic Mixing**: Uses the Camelot Wheel system for key compatibility
- 🔊 **BPM Matching**: Supports direct, halftime, and doubletime BPM compatibility
- ⚙️ **Configurable Strictness**: STRICT, MODERATE, or RELAXED harmonic compatibility levels
- 🚀 **Fast**: Powered by Google OR-Tools CP-SAT solver (award-winning constraint solver)
- 📦 **SDK + CLI**: Use as a Python library or command-line tool

## Installation

```bash
uv add dj-playlist-optimizer
```

Or with pip:

```bash
pip install dj-playlist-optimizer
```

## Quick Start

### SDK Usage

```python
from dj_playlist_optimizer import PlaylistOptimizer, Track, HarmonicLevel

tracks = [
    Track(id="track_001", key="8A", bpm=128),
    Track(id="track_002", key="8B", bpm=130),
    Track(id="track_003", key="9A", bpm=125),
]

optimizer = PlaylistOptimizer(
    bpm_tolerance=10,
    allow_halftime_bpm=True,
    max_violation_pct=0.10,
    harmonic_level=HarmonicLevel.STRICT,
)

result = optimizer.optimize(tracks)

for i, track in enumerate(result.playlist, 1):
    print(f"{i}. {track.id} ({track.key}, {track.bpm} BPM)")
```

### CLI Usage

```bash
# Basic usage
dj-optimize tracks.json

# With custom settings
dj-optimize tracks.json --bpm-tolerance 8 --harmonic-level moderate

# Save results to JSON
dj-optimize tracks.json --output result.json
```

## Input Format

JSON file with tracks containing `id`, `key` (Camelot notation), and `bpm`:

```json
{
  "tracks": [
    {"id": "track_001", "key": "8A", "bpm": 128},
    {"id": "track_002", "key": "8B", "bpm": 130},
    {"id": "track_003", "key": "9A", "bpm": 125}
  ]
}
```

## How It Works

### 1. BPM Compatibility

Adjacent tracks must have compatible BPMs within tolerance:

| Track A | Track B | Tolerance | Match? | Reason |
|---------|---------|-----------|--------|--------|
| 128 BPM | 130 BPM | ±10 | ✅ | Direct (diff = 2) |
| 128 BPM | 64 BPM | ±10 | ✅ | Half-time (128 = 64×2) |
| 75 BPM | 150 BPM | ±10 | ✅ | Double-time (75×2 = 150) |
| 128 BPM | 100 BPM | ±10 | ❌ | Too far |

### 2. Harmonic Mixing (Camelot Wheel)

Harmonic compatibility levels:

**STRICT** (default):
- Same key (8A → 8A)
- ±1 hour same letter (8A → 7A, 9A)
- Same hour different letter (8A → 8B)

**MODERATE**:
- Above + ±1 hour different letter (8A → 9B, 7B)

**RELAXED**:
- Above + ±3 hours (8A → 5A, 11A)

### 3. Optimization Goal

Maximize playlist length while keeping non-harmonic transitions below the threshold (default: 10%).

## Configuration Options

| Parameter | Default | Description |
|-----------|---------|-------------|
| `bpm_tolerance` | 10.0 | Maximum BPM difference for direct match |
| `allow_halftime_bpm` | True | Enable half/double-time matching |
| `max_violation_pct` | 0.10 | Max percentage of non-harmonic transitions |
| `harmonic_level` | STRICT | Harmonic compatibility strictness |
| `time_limit_seconds` | 60.0 | Solver time limit |

## Examples

See `examples/` directory:
- `example_tracks.json` - Sample input data
- `sdk_usage.py` - SDK usage demonstration

## Development

```bash
# Clone repository
git clone https://github.com/yourusername/dj-playlist-optimizer
cd dj-playlist-optimizer

# Install with dev dependencies
uv sync --dev

# Run tests
uv run pytest

# Run example
uv run python examples/sdk_usage.py
```

## How the Solver Works

The optimizer uses Google OR-Tools CP-SAT solver with:

1. **Binary Variables**: `included[i]` = track i is in playlist
2. **Edge Variables**: `edge[i,j]` = track j follows track i
3. **Circuit Constraint**: `AddCircuit` ensures valid track ordering
4. **BPM Constraints**: Only create edges between BPM-compatible tracks
5. **Harmonic Soft Constraints**: Penalize non-harmonic transitions
6. **Objective**: Maximize `sum(included)`

## License

MIT

## Credits

Built with:
- [Google OR-Tools](https://developers.google.com/optimization) - Constraint programming solver
- Camelot Wheel system by Mark Davis (Mixed In Key)