def fine_calculator(area, speed):
    if area == "urban":
        fine_coefficient = 1
        overspeed_percentage = (speed - 50) / 0.5
    elif area == "expressway":
        fine_coefficient = 0.8
        overspeed_percentage = speed - 100
    elif area == "motorway":
        fine_coefficient = 0.5
        overspeed_percentage = (speed - 120) / 1.2
    return round(fine_coefficient * overspeed_percentage**2)
