# Calculate thermal physics properties
def thermal_expansion(original_length, coefficient, temp_change):
    """ΔL = L₀ × α × ΔT"""
    return original_length * coefficient * temp_change

def heat_capacity(mass, specific_heat, temp_change):
    """Q = m × c × ΔT"""
    return mass * specific_heat * temp_change

def celsius_to_kelvin(celsius):
    """K = °C + 273.15"""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """°C = (°F - 32) × 5/9"""
    return (fahrenheit - 32) * 5/9

# Test thermal calculations
steel_length = 10  # meters
steel_coefficient = 12e-6  # per °C
temp_change = 50  # °C

expansion = thermal_expansion(steel_length, steel_coefficient, temp_change)
print(f"Steel expansion: {expansion*1000:.2f} mm")

# Heat required to warm water
water_mass = 1  # kg
specific_heat_water = 4186  # J/(kg⋅°C)
temp_rise = 20  # °C

heat_needed = heat_capacity(water_mass, specific_heat_water, temp_rise)
print(f"Heat needed: {heat_needed} J")

# Temperature conversions
print(f"100°C = {celsius_to_kelvin(100)} K")
print(f"32°F = {fahrenheit_to_celsius(32):.1f}°C")
