def calc_bmi(weight_kg: float, height_cm: float) -> float:
    if height_cm <= 0:
        raise ValueError("height_cm must be > 0")
    h_m = height_cm / 100.0
    return round(weight_kg / (h_m * h_m), 2)
