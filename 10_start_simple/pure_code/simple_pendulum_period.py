# Calculate period of a simple pendulum
import math

def pendulum_period(length, gravity=9.81):
    """T = 2π√(L/g)"""
    return 2 * math.pi * math.sqrt(length / gravity)

def pendulum_length(period, gravity=9.81):
    """L = (T²g)/(4π²)"""
    return (period**2 * gravity) / (4 * math.pi**2)

# Test calculations
length = 1.0  # meter
period = pendulum_period(length)
print(f"Period of {length}m pendulum: {period:.2f} seconds")

desired_period = 2.0  # seconds
required_length = pendulum_length(desired_period)
print(f"Length needed for {desired_period}s period: {required_length:.2f} meters")
