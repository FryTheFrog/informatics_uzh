#!/usr/bin/env python3
# Hint: Your test suite does not detect invalid areas evaluations: urban,expressway and motorway are the only valid areas.
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

    if area not in coefficients:
        return "Invalid Area Value"
    if (not isinstance(speed, (int, float)) and not isinstance(speed, bool)):
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
            # speed_limit is always non zero.
            difference_ratio = (difference / speed_limit) * 100
            fine = coefficient * difference_ratio**2
            return round(fine)
