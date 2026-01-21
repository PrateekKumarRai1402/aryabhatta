def convert_mass(pair: str, magnitude: float) -> float:
    """
    Convert between mass/weight units.
    Example: convert_mass("kg2lb", 1)
    """

    # Conversion factors to kilograms
    units_to_kg = {
        "mg": 1e-6,
        "g": 1e-3,
        "kg": 1.0,
        "t": 1000.0,        # metric tonne
        "oz": 0.0283495,    # ounce
        "lb": 0.453592,     # pound
        "stone": 6.35029,   # UK stone
        "ton_us": 907.185,  # US short ton
        "ton_uk": 1016.05,  # UK long ton
        "amu": 1.66054e-27, # atomic mass unit
        "M☉": 1.989e30      # solar mass
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")

    src, dst = pair.split("2")
    if src not in units_to_kg or dst not in units_to_kg:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    kg = magnitude * units_to_kg[src]
    result = kg / units_to_kg[dst]
    return result
