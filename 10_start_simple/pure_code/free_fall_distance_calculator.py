# Calculate distance fallen in free fall
import math

def fall_distance(time):
    """Calculate distance fallen in free fall given time"""
    g = 9.81  # gravity acceleration (m/s²)
    return 0.5 * g * time**2

def fall_duration(distance):
    """Calculate time to fall given distance"""
    g = 9.81
    return math.sqrt(2 * distance / g)

# Test the functions
time = 3  # seconds
distance = fall_distance(time)
print(f"Distance fallen in {time} seconds: {distance:.2f} meters")

height = 50  # meters
duration = fall_duration(height)
print(f"Time to fall {height} meters: {duration:.2f} seconds")
