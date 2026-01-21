def convert_force(pair: str, magnitude: float) -> float:
    """
    Convert between force units.
    Example: convert_force("n2lbf", 10)
    """

    # Conversion factors to newtons
    units_to_n = {
        "n": 1.0,
        "dyn": 1e-5,       # dyne
        "lbf": 4.44822,    # pound-force
        "kgf": 9.80665     # kilogram-force
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_n or dst not in units_to_n:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    newtons = magnitude * units_to_n[src]
    result = newtons / units_to_n[dst]
    return result
