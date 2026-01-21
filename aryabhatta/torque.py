def convert_torque(pair: str, magnitude: float) -> float:
    """
    Convert between torque units.
    Example: convert_torque("nm2ftlb", 10)
    """

    # Conversion factors to newton-meters
    units_to_nm = {
        "nm": 1.0,
        "ftlb": 1.35582,   # foot-pound force
        "kgfm": 9.80665    # kilogram-force meter
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_nm or dst not in units_to_nm:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    nm = magnitude * units_to_nm[src]
    result = nm / units_to_nm[dst]
    return result
