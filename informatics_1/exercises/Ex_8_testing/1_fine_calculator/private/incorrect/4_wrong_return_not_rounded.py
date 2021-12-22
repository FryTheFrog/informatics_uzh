#!/usr/bin/env python3
# Hint: Your test suite does not always detect invalid return values.
def fine_calculator(area, speed):
    coefficients = {
        'urban': 1,
        'expressway': 0.8,
        'motorway': 0.5
    }

    speed_limits = {
        'urban': 50,
        'expressway': 100,
        'motorway': 120
    }

    if not isinstance(area, str):
        return "Invalid Area Type"
    elif area not in coefficients:
        return "Invalid Area Value"
    elif area not in coefficients:
        return "Invalid Area"
    elif (not isinstance(speed, (int, float)) and not isinstance(speed, bool)):
        return "Invalid Speed Type"
    elif speed < 0:
        return "Invalid Speed Value"
    else:
        speed_limit = speed_limits[area]
        if (speed <= speed_limit):
            return 0
        else:
            coefficient = coefficients[area]
            difference = speed - speed_limit
            difference_ratio = (difference / speed_limit)*100
            fine = coefficient * difference_ratio**2
            return fine
