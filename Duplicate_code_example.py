#Duplicate code example

def calculate_volume_surface_area(length, width, height):
    volume = calculate_volume(length,width,height)
    surface_area = calculate_surface_area(length,height)
    return volume, surface_area


# Duplicate code: calculate_area and calculate_perimeter functions have similar calculations.
def calculate_area_perimeter(length, width):
    area = calculate_area(length,width)
    perimeter = calculate_perimeter(length, width)
    return area, perimeter
    perimeter = 2 * (length + width)
    return area, perimeter
