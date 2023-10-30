#Duplicate code example
import duplicate_code

def calculate_volume_surface_area(length, width, height):
    volume = calculate_volume(length, width, heigth)
    surface_area = calculate_surface_area(length, width, height)
    print("volume:", volume)
    print("Surface Area:", surface_area)


# Duplicate code: calculate_area and calculate_perimeter functions have similar calculations.
def calculate_area_perimeter(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print("Area:", area)
    print("Perimeter:", perimeter)

