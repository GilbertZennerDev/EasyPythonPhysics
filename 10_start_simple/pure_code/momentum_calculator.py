# Calculate momentum and analyze collisions
def momentum(mass, velocity):
    """p = m × v"""
    return mass * velocity

def elastic_collision_1d(m1, v1, m2, v2):
    """Calculate final velocities after elastic collision"""
    v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_final, v2_final

# Test momentum calculations
car_mass = 1200  # kg
car_velocity = 20  # m/s
car_momentum = momentum(car_mass, car_velocity)
print(f"Car momentum: {car_momentum} kg⋅m/s")

# Test collision
m1, v1 = 5, 10  # 5 kg at 10 m/s
m2, v2 = 3, -5  # 3 kg at -5 m/s
v1_final, v2_final = elastic_collision_1d(m1, v1, m2, v2)
print(f"After collision: v1 = {v1_final:.2f} m/s, v2 = {v2_final:.2f} m/s")
