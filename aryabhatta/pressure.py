def convert_pressure(pair: str, magnitude: float) -> float:
    """
    Convert between pressure units.
    Example: convert_pressure("psi2pa", 1)
    """

    # Conversion factors to pascals
    units_to_pa = {
        "pa": 1.0,
        "kpa": 1e3,
        "bar": 1e5,
        "atm": 101325.0,
        "psi": 6894.76,
        "torr": 133.322,
        "mmhg": 133.322
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_pa or dst not in units_to_pa:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    pascals = magnitude * units_to_pa[src]
    result = pascals / units_to_pa[dst]
    return result
