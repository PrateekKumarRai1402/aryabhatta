def convert_energy(pair: str, magnitude: float) -> float:
    """
    Convert between energy units.
    Example: convert_energy("kwh2joule", 1)
    """

    # Conversion factors to joules
    units_to_joule = {
        "j": 1.0,
        "kj": 1e3,
        "mj": 1e6,
        "cal": 4.184,       # small calorie
        "kcal": 4184.0,     # food calorie
        "btu": 1055.06,
        "wh": 3600.0,
        "kwh": 3.6e6,
        "ev": 1.602e-19     # electronvolt
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_joule or dst not in units_to_joule:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    joules = magnitude * units_to_joule[src]
    result = joules / units_to_joule[dst]
    return result
