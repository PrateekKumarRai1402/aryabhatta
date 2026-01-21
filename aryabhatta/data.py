def convert_storage(pair: str, magnitude: float) -> float:
    """
    Convert between digital storage units.
    Example: convert_storage("mb2gb", 500)
    """

    # Conversion factors to bytes
    units_to_bytes = {
        "bit": 0.125,   # 1 bit = 1/8 byte
        "b": 1.0,       # byte
        "kb": 1e3,
        "mb": 1e6,
        "gb": 1e9,
        "tb": 1e12,
        "pb": 1e15,
        "kib": 1024,
        "mib": 1024**2,
        "gib": 1024**3
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_bytes or dst not in units_to_bytes:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    bytes_val = magnitude * units_to_bytes[src]
    result = bytes_val / units_to_bytes[dst]
    return result
