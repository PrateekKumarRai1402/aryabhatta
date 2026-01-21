def convert_frequency(pair: str, magnitude: float) -> float:
    """
    Convert between frequency units.
    Example: convert_frequency("mhz2hz", 1)
    """

    # Conversion factors to hertz
    units_to_hz = {
        "hz": 1.0,
        "khz": 1e3,
        "mhz": 1e6,
        "ghz": 1e9
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_hz or dst not in units_to_hz:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    hz = magnitude * units_to_hz[src]
    result = hz / units_to_hz[dst]
    return result
