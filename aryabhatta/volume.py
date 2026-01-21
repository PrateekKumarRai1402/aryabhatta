def convert_volume(pair: str, magnitude: float) -> float:
    """
    Convert between any two of the defined volume units.
    Example: convert_volume("gallon2liter", 1)
    """

    # Conversion factors to cubic meters
    units_to_m3 = {
        # SI
        "mm3": 1e-9,
        "cm3": 1e-6,
        "m3": 1.0,
        "km3": 1e9,
        "l": 1e-3,       # liter
        "ml": 1e-6,      # milliliter

        # Imperial / US Customary
        "in3": 1.6387e-5,
        "ft3": 0.0283168,
        "yd3": 0.764555,
        "floz": 2.9573e-5,   # US fluid ounce
        "pt": 4.73176e-4,    # US pint
        "qt": 9.46353e-4,    # US quart
        "gal": 3.78541e-3,   # US gallon
        "bbl": 0.159,        # oil barrel

        # Engineering-specific
        "boardfoot": 2.35974e-3,   # 1 ft × 1 ft × 1 in
        "acrefoot": 1233.5,
        "cord": 3.62,              # 128 ft³

        # Astronomical / Scientific
        "pc3": 2.94e49,       # cubic parsec (approx)
        "ly3": 8.47e47,       # cubic light-year (approx)
        "au3": 3.35e33        # cubic astronomical unit (approx)
    }

    # Parse input like "gallon2liter"
    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2' with '2' in between")

    src, dst = pair.split("2")

    # Synonyms (British/US spellings, full names)
    synonyms = {
        "milliliter": "ml", "millilitre": "ml",
        "liter": "l", "litre": "l",
        "cubicmeter": "m3", "cubicmetre": "m3",
        "cubiccentimeter": "cm3", "cubiccentimetre": "cm3",
        "cubicmillimeter": "mm3", "cubicmillimetre": "mm3",
        "cubicinch": "in3", "cubicinches": "in3",
        "cubicfoot": "ft3", "cubicfeet": "ft3",
        "cubicyard": "yd3", "cubicyards": "yd3",
        "fluidounce": "floz",
        "pint": "pt",
        "quart": "qt",
        "gallon": "gal",
        "barrel": "bbl",
        "acrefoot": "acrefoot",
        "boardfoot": "boardfoot",
        "cord": "cord",
        "parsec3": "pc3",
        "lightyear3": "ly3",
        "au3": "au3"
    }
    src = synonyms.get(src, src)
    dst = synonyms.get(dst, dst)

    if src not in units_to_m3 or dst not in units_to_m3:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    # Convert: source → cubic meters → destination
    cubic_meters = magnitude * units_to_m3[src]
    result = cubic_meters / units_to_m3[dst]
    return result


# ✅ Example usage (only runs when file executed directly)
if __name__ == "__main__":
    print("1 gallon to liters:", convert_volume("gal2l", 1))
    print("5 liters to cubic feet:", convert_volume("l2ft3", 5))
    print("1000 cm³ to liters:", convert_volume("cm32l", 1000))
    print("1 acre-foot to gallons:", convert_volume("acrefoot2gal", 1))
