def convert_temp(pair: str, magnitude: float) -> float:
    """
    Convert between temperature units.
    Example: convert_temperature("c2f", 100)
    """

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")

    src, dst = pair.split("2")

    # Normalize synonyms
    synonyms = {"celsius": "c", "fahrenheit": "f", "kelvin": "k", "rankine": "r"}
    src = synonyms.get(src, src)
    dst = synonyms.get(dst, dst)

    # Convert source → Celsius
    if src == "c":
        celsius = magnitude
    elif src == "f":
        celsius = (magnitude - 32) * 5/9
    elif src == "k":
        celsius = magnitude - 273.15
    elif src == "r":
        celsius = (magnitude - 491.67) * 5/9
    else:
        raise ValueError(f"Unknown unit: {src}")

    # Convert Celsius → destination
    if dst == "c":
        return celsius
    elif dst == "f":
        return celsius * 9/5 + 32
    elif dst == "k":
        return celsius + 273.15
    elif dst == "r":
        return (celsius + 273.15) * 9/5
    else:
        raise ValueError(f"Unknown unit: {dst}")
