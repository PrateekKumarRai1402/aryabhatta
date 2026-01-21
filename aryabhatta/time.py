def convert_time(pair: str, magnitude: float) -> float:
    """
    Convert between time units.
    Example: convert_time("hr2s", 1)
    """

    # Conversion factors to seconds
    units_to_sec = {
        "ns": 1e-9,
        "µs": 1e-6,
        "ms": 1e-3,
        "s": 1.0,
        "min": 60.0,
        "hr": 3600.0,
        "day": 86400.0,
        "week": 604800.0,
        "month": 2.628e6,   # average month (30.44 days)
        "year": 3.154e7,    # Julian year (365.25 days)
        "julianyear": 3.154e7,
        "siderealday": 86164.1
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")

    src, dst = pair.split("2")
    if src not in units_to_sec or dst not in units_to_sec:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    seconds = magnitude * units_to_sec[src]
    result = seconds / units_to_sec[dst]
    return result
