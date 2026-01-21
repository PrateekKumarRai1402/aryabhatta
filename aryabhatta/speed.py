def convert_speed(pair: str, magnitude: float) -> float:
    """
    Convert between speed/velocity units.
    Example: convert_speed("kmh2mph", 100)
    """

    # Conversion factors to meters per second
    units_to_ms = {
        "m/s": 1.0,
        "km/h": 0.277778,
        "mph": 0.44704,
        "ft/s": 0.3048,
        "knot": 0.514444,
        "mach": 340.29,   # Mach 1 at sea level
        "c": 299792458.0  # speed of light
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_ms or dst not in units_to_ms:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    ms = magnitude * units_to_ms[src]
    result = ms / units_to_ms[dst]
    return result
