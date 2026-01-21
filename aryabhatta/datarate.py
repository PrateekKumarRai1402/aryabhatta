def convert_datarate(pair: str, magnitude: float) -> float:
    """
    Convert between data transfer rates.
    Example: convert_datarate("mbps2kbps", 10)
    """

    # Conversion factors to bits per second
    units_to_bps = {
        "bps": 1.0,
        "kbps": 1e3,
        "mbps": 1e6,
        "gbps": 1e9
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_bps or dst not in units_to_bps:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    bps = magnitude * units_to_bps[src]
    result = bps / units_to_bps[dst]
    return result
