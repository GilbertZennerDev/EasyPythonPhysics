# Calculate voltage, current, or resistance using Ohm's Law
def calculate_voltage(current, resistance):
    """V = I × R"""
    return current * resistance

def calculate_current(voltage, resistance):
    """I = V / R"""
    return voltage / resistance

def calculate_resistance(voltage, current):
    """R = V / I"""
    return voltage / current

# Test calculations
print(f"Voltage: {calculate_voltage(2, 10)} V")
print(f"Current: {calculate_current(12, 6)} A")
print(f"Resistance: {calculate_resistance(9, 3)} Ω")
