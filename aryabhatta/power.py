def convert_power(pair: str, magnitude: float) -> float:
    """
    Convert between power units.
    Example: convert_power("hp2w", 1)
    """

    # Conversion factors to watts
    units_to_watt = {
        "w": 1.0,
        "kw": 1e3,
        "mw": 1e6,
        "gw": 1e9,
        "hp": 745.7,       # mechanical horsepower
        "dbm": 0.001       # 1 dBm = 1 mW (approx, simplified)
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_watt or dst not in units_to_watt:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    watts = magnitude * units_to_watt[src]
    result = watts / units_to_watt[dst]
    return result
