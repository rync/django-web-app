# utils.py

def liters_to_gallons(liters):
    """Convert liters to gallons."""
    return liters * 0.264172

def gallons_to_liters(gallons):
    """Convert gallons to liters."""
    return gallons / 0.264172

def kilograms_to_pounds(kilograms):
    """Convert kilograms to pounds."""
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    """Convert pounds to kilograms."""
    return pounds / 2.20462

def meal_compatibility(meal1, meal2):
    """Check compatibility of two meals based on ingredients or preferences."""
    # Example logic (this would require more details based on actual requirements)
    if meal1['dietary_restrictions'].intersection(meal2['ingredients']):
        return False
    return True

def filter_residents_by_preference(residents, preference):
    """Filter residents based on dietary preference."""
    return [resident for resident in residents if preference in resident['dietary_preferences']]