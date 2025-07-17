# Calculate density and buoyancy forces
def density(mass, volume):
    """ρ = m / V"""
    return mass / volume

def buoyant_force(fluid_density, volume, gravity=9.81):
    """F_b = ρ_fluid × V × g"""
    return fluid_density * volume * gravity

def archimedes_principle(object_density, fluid_density, total_volume):
    """Calculate submerged volume fraction"""
    return object_density / fluid_density

def pressure_at_depth(depth, fluid_density, gravity=9.81):
    """P = ρ × g × h"""
    return fluid_density * gravity * depth

# Test density and buoyancy
# Object properties
mass = 2.7  # kg
volume = 0.001  # m³ (1 liter)
obj_density = density(mass, volume)
print(f"Object density: {obj_density} kg/m³")

# Water properties
water_density = 1000  # kg/m³
buoyant_force_water = buoyant_force(water_density, volume)
print(f"Buoyant force in water: {buoyant_force_water:.2f} N")

# Check if object floats
submerged_fraction = archimedes_principle(obj_density, water_density, volume)
if submerged_fraction <= 1:
    print(f"Object floats, {submerged_fraction*100:.1f}% submerged")
else:
    print("Object sinks")

# Pressure at depth
depth = 10  # meters
pressure = pressure_at_depth(depth, water_density)
print(f"Pressure at {depth}m depth: {pressure/1000:.1f} kPa")
