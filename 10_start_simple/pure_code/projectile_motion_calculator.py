# Calculate projectile motion parameters
import math

def projectile_range(initial_velocity, angle_degrees, gravity=9.81):
    """R = v²sin(2θ)/g"""
    angle_rad = math.radians(angle_degrees)
    return (initial_velocity**2 * math.sin(2 * angle_rad)) / gravity

def projectile_max_height(initial_velocity, angle_degrees, gravity=9.81):
    """h = v²sin²(θ)/(2g)"""
    angle_rad = math.radians(angle_degrees)
    return (initial_velocity**2 * math.sin(angle_rad)**2) / (2 * gravity)

def projectile_time_flight(initial_velocity, angle_degrees, gravity=9.81):
    """t = 2v sin(θ)/g"""
    angle_rad = math.radians(angle_degrees)
    return (2 * initial_velocity * math.sin(angle_rad)) / gravity

# Test projectile motion
v0 = 30  # m/s
angle = 45  # degrees

range_distance = projectile_range(v0, angle)
max_height = projectile_max_height(v0, angle)
flight_time = projectile_time_flight(v0, angle)

print(f"Range: {range_distance:.2f} m")
print(f"Max height: {max_height:.2f} m")
print(f"Flight time: {flight_time:.2f} s")
