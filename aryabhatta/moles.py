def convert_moles(pair: str, magnitude: float) -> float:
    """
    Convert between molar units.
    Example: convert_moles("mol2mmol", 2)
    """

    # Conversion factors to moles
    units_to_mol = {
        "mol": 1.0,
        "mmol": 1e-3,
        "umol": 1e-6,
        "particle": 1/6.022e23   # Avogadro's number
    }

    pair = pair.lower()
    if "2" not in pair:
        raise ValueError("Pair must be in format 'unit1unit2'")
    src, dst = pair.split("2")

    if src not in units_to_mol or dst not in units_to_mol:
        raise ValueError(f"Unknown unit(s): {src}, {dst}")

    mols = magnitude * units_to_mol[src]
    result = mols / units_to_mol[dst]
    return result
