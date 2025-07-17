# Calculate electrical power in different ways
def power_vi(voltage, current):
    """P = V × I"""
    return voltage * current

def power_v2r(voltage, resistance):
    """P = V² / R"""
    return voltage**2 / resistance

def power_i2r(current, resistance):
    """P = I² × R"""
    return current**2 * resistance

def energy_cost(power_watts, hours, cost_per_kwh):
    """Calculate electricity cost"""
    energy_kwh = (power_watts * hours) / 1000
    return energy_kwh * cost_per_kwh

# Test power calculations
voltage = 120  # V
current = 5    # A
resistance = 24  # Ω

print(f"Power (V×I): {power_vi(voltage, current)} W")
print(f"Power (V²/R): {power_v2r(voltage, resistance)} W")
print(f"Power (I²×R): {power_i2r(current, resistance)} W")

# Calculate monthly cost of a 100W bulb
monthly_cost = energy_cost(100, 24*30, 0.12)
print(f"Monthly cost of 100W bulb: ${monthly_cost:.2f}")
