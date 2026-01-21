def convert_length(pair: str, magnitude: float) -> float:
    """
    Convert between any two of the 24 defined length units.
    Example: convert_length("mile2lightyear", 1)
    """

    # Conversion factors to meters
    units_to_meters = {
        # SI
        "nm": 1e-9,
        "µm": 1e-6,
        "mm": 1e-3,
        "cm": 1e-2,
        "m": 1.0,
        "km": 1e3,

        # Imperial
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,

        # Engineering-specific
        "mil": 2.54e-5,       # 0.001 inch
        "micron": 1e-6,       # synonym for µm
        "chain": 20.1168,     # 66 ft
        "rod": 5.0292,        # 16.5 ft
        "furlong": 201.168,   # 1/8 mile
        "league": 4828.032,   # ~3 miles

        # Astronomical
        "AU": 1.496e11,       # meters
        "ly": 9.461e15,       # meters
        "pc": 3.086e16        # meters
    }

    # Normalize input
    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2' with '2' in between")

    src, dst = pair.split("2")

    # Handle synonyms
    synonyms = {
        "nanometer": "nm",
        "micrometer": "µm",
        "millimeter": "mm",
        "centimeter": "cm",
        "meter": "m",
        "kilometer": "km",
        "inch": "in",
        "foot": "ft",
        "yard": "yd",
        "mile": "mi",
        "astronomicalunit": "AU",
        "lightyear": "ly",
        "parsec": "pc"
    }
    src = synonyms.get(src, src)
    dst = synonyms.get(dst, dst)

    if src not in units_to_meters or dst not in units_to_meters:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    # Convert: source → meters → destination
    meters = magnitude * units_to_meters[src]
    result = meters / units_to_meters[dst]

    return result


# ✅ Only runs when executed directly, not when imported
if __name__ == "__main__":
    print("Testing convert_length function:")
    print("1 mile to light-year:", convert_length("mile2lightyear", 1))
    print("5 km to miles:", convert_length("km2mi", 5))
    print("1000 nm to µm:", convert_length("nm2µm", 1000))
