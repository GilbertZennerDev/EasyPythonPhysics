# Calculate kinetic energy of moving objects
def kinetic_energy(mass, velocity):
    """KE = 1/2 × m × v²"""
    return 0.5 * mass * velocity**2

def velocity_from_ke(kinetic_energy, mass):
    """v = √(2KE/m)"""
    return (2 * kinetic_energy / mass)**0.5

# Test with different objects
car_mass = 1500  # kg
car_velocity = 25  # m/s
car_ke = kinetic_energy(car_mass, car_velocity)
print(f"Car kinetic energy: {car_ke:,.0f} J")

ball_mass = 0.5  # kg
ball_ke = 100  # J
ball_velocity = velocity_from_ke(ball_ke, ball_mass)
print(f"Ball velocity: {ball_velocity:.2f} m/s")
