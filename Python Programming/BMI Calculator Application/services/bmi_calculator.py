def calculate_bmi(weight, height, units):
    # Convert weight to kg
    if units['weight'] == 'lbs':
        weight = weight * 0.453592  # lbs to kg
    elif units['weight'] == 'kg':
        pass  # already in kg
    else:
        return "Invalid weight unit"

    # Convert height to meters
    if units['height'] == 'inch':
        height = height * 0.0254  # inch to meters
    elif units['height'] == 'cm':
        height = height / 100  # cm to meters
    else:
        return "Invalid height unit"

    # Check if weight and height are in valid ranges
    if not (30 <= weight <= 300) or not (1 <= height <= 2.5):
        return "Invalid weight or height range"

    # Calculate BMI
    bmi = weight / (height ** 2)

    return bmi