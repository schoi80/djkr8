from djkr8 import HarmonicLevel, PlaylistOptimizer, Track

print("=" * 70)
print("Energy Boost Mixing Demo - Mixed In Key Philosophy")
print("=" * 70)

tracks = [
    Track(id="1", key="5A", bpm=120, energy=3, title="Warm Start"),
    Track(id="2", key="6A", bpm=122, energy=3, title="Building"),
    Track(id="3", key="7A", bpm=124, energy=4, title="Energy Boost Target"),
    Track(id="4", key="8A", bpm=126, energy=4, title="Sustained Energy"),
    Track(id="5", key="12A", bpm=128, energy=5, title="Peak Energy"),
    Track(id="6", key="7A", bpm=130, energy=5, title="Armin Variation Target"),
]

print("\n📊 Available Tracks:")
print("-" * 70)
for t in tracks:
    print(f"  {t.id}. {t.title:25} | Key: {t.key:3} | BPM: {t.bpm:3.0f} | Energy: {t.energy}")

print("\n\n🎵 SCENARIO 1: Standard Harmonic Mixing (No Energy Boosts)")
print("-" * 70)
optimizer = PlaylistOptimizer(
    harmonic_level=HarmonicLevel.STRICT,
    max_energy_boosts=0,
    transition_quality_weight=10.0,
)

result = optimizer.optimize(tracks)

print(f"Playlist Length: {len(result.playlist)} tracks")
print(f"Transitions: {len(result.transitions)}")
print("\nSequence:")
for i, track in enumerate(result.playlist, 1):
    print(f"  {i}. {track.title:25} ({track.key}, Energy {track.energy})")

if result.transitions:
    print("\nTransition Analysis:")
    for i, trans in enumerate(result.transitions, 1):
        quality_label = (
            "✓ Smooth"
            if trans.quality_score >= 0.8
            else "⚡ Boost"
            if trans.quality_score >= 0.5
            else "⚠ Clash"
        )
        print(
            f"  {i}. {trans.from_track.key} → {trans.to_track.key} | "
            f"Quality: {trans.quality_score:.2f} | {quality_label}"
        )

print("\n\n⚡ SCENARIO 2: With Energy Boosts (Mixed In Key Style)")
print("-" * 70)
optimizer = PlaylistOptimizer(
    harmonic_level=HarmonicLevel.STRICT,
    max_energy_boosts=2,
    transition_quality_weight=10.0,
)

result = optimizer.optimize(tracks)

print(f"Playlist Length: {len(result.playlist)} tracks")
print(f"Transitions: {len(result.transitions)}")
print("\nSequence:")
for i, track in enumerate(result.playlist, 1):
    print(f"  {i}. {track.title:25} ({track.key}, Energy {track.energy})")

if result.transitions:
    print("\nTransition Analysis:")
    boost_count = 0
    for i, trans in enumerate(result.transitions, 1):
        is_boost = trans.transition_type.value == "energy_boost"
        if is_boost:
            boost_count += 1
            quality_label = f"⚡ ENERGY BOOST #{boost_count}"
        elif trans.quality_score >= 0.8:
            quality_label = "✓ Smooth"
        else:
            quality_label = "⚠ Clash"

        print(
            f"  {i}. {trans.from_track.key} → {trans.to_track.key} | "
            f"Quality: {trans.quality_score:.2f} | {quality_label}"
        )

    print(f"\n💡 Energy Boosts Used: {boost_count}/{optimizer.max_energy_boosts}")

print("\n\n🎯 Key Insights:")
print("-" * 70)
print("• Energy boosts (+2 on Camelot wheel) add excitement but are used sparingly")
print("• Professional DJs use 2-3 energy boosts per set (we allow up to 3)")
print("• The solver balances playlist length with transition quality")
print("• Higher quality_weight prioritizes smoother mixes over longer playlists")
print("\n" + "=" * 70)
