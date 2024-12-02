import os
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
from shapely.geometry import Point
import matplotlib.colors as mcolors

# Shapefiles
countries_shapefile = 'shapefiles/ne_110m_admin_0_countries.shp'
states_shapefile = 'shapefiles/ne_110m_admin_1_states_provinces.shp'

# Failsafe
for path in [countries_shapefile, states_shapefile]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Shapefile not found at '{path}'. Please check the folder and file name.")

countries_map = gpd.read_file(countries_shapefile)
states_map = gpd.read_file(states_shapefile)

continents = sorted(countries_map['CONTINENT'].unique())
countries = sorted(countries_map['NAME'].unique())
states = sorted(states_map['name'].unique())

# hex codes
def is_valid_hex_color(hex_color):
    if hex_color.startswith("#") and len(hex_color) in {7, 4}:
        try:
            mcolors.hex2color(hex_color)
            return True
        except ValueError:
            return False
    return False

# Prog. begin
show_list = False
while True:
    if show_list:
        print("\nHere are the valid options:")
        print("\nValid continents:", ", ".join(continents))
        print("\nValid countries:", ", ".join(countries))
        print("\nValid states:", ", ".join(states))
    region = input("\nEnter the name of a continent, country, or state: ").strip().lower()
    if region in (name.lower() for name in continents + countries + states):
        break
    print("\nInvalid region. Please try again.")
    show_list = True  # Show list after the first invalid input

# Color prompt
while True:
    dot_color = input("Enter the color you want for the dots (e.g., 'blue', 'red', 'green', or a hex code like '#FF5733'): ").strip().lower()
    if dot_color in mcolors.CSS4_COLORS or dot_color in mcolors.TABLEAU_COLORS or is_valid_hex_color(dot_color):
        break
    print("\nInvalid color. Please enter a valid color name (e.g., 'blue', 'red', 'green') or a valid hex code (e.g., '#FF5733').")

# Density
while True:
    try:
        density = float(input("Enter the density of the grid (1 for sparse, 100 for dense, or a value in between): ").strip())
        if 1 <= density <= 100:
            break
        else:
            print("Invalid input! Please enter a value between 1 and 100 (inclusive).")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

#find correct map
def find_filtered_map(region):
    region_lower = region.lower()
    if region_lower in (name.lower() for name in countries_map['CONTINENT'].unique()):
        return countries_map[countries_map['CONTINENT'].str.lower() == region_lower]
    elif region_lower in (name.lower() for name in countries_map['NAME'].unique()):
        return countries_map[countries_map['NAME'].str.lower() == region_lower]
    elif region_lower in (name.lower() for name in states_map['name'].unique()):
        return states_map[states_map['name'].str.lower() == region_lower]
    else:
        raise ValueError(f"'{region}' is not a valid continent, country, or state.")

# Filter the map based on the input region
filtered_map = find_filtered_map(region)

# Ensure the filtered map has geometry
if filtered_map.empty:
    raise ValueError(f"No data found for '{region}'. Please check the input.")

bounds = filtered_map.total_bounds
minx, miny, maxx, maxy = bounds
width = maxx - minx
height = maxy - miny

# Population w/ failsafe
resolution = max(min(width, height) / density, 0.01)  # Ensure resolution is non-zero
x_coords = np.arange(minx, maxx, resolution)
y_coords = np.arange(miny, maxy, resolution)
grid_points = [Point(x, y) for x in x_coords for y in y_coords]
point_gdf = gpd.GeoDataFrame(geometry=grid_points, crs=filtered_map.crs)
point_gdf = gpd.clip(point_gdf, filtered_map)
fig, ax = plt.subplots(figsize=(10, 6))
filtered_map.plot(ax=ax, color='none', edgecolor='none')
point_gdf.plot(ax=ax, color=dot_color, markersize=5)
ax.set_axis_off()

# Save to desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, f"{region.replace(' ', '_')}-map.svg")
plt.savefig(output_file, format='svg', bbox_inches='tight', pad_inches=0)
plt.close()

print(f"SVG file has been saved to your desktop as '{output_file}'")
