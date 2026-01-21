def convert_area(pair: str, magnitude: float) -> float:
    """
    Convert between area units.
    Example: convert_area("acre2m2", 1)
    """

    # Conversion factors to square meters
    units_to_m2 = {
        "mm2": 1e-6,
        "cm2": 1e-4,
        "m2": 1.0,
        "km2": 1e6,
        "in2": 0.00064516,
        "ft2": 0.092903,
        "yd2": 0.836127,
        "acre": 4046.86,
        "hectare": 10000.0
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_m2 or dst not in units_to_m2:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    m2 = magnitude * units_to_m2[src]
    result = m2 / units_to_m2[dst]
    return result
