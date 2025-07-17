# Calculate wave properties
def wave_speed(frequency, wavelength):
    """v = f × λ"""
    return frequency * wavelength

def wave_frequency(speed, wavelength):
    """f = v / λ"""
    return speed / wavelength

def wave_wavelength(speed, frequency):
    """λ = v / f"""
    return speed / frequency

def doppler_effect(source_freq, source_speed, observer_speed, wave_speed):
    """Doppler effect calculation"""
    return source_freq * (wave_speed + observer_speed) / (wave_speed - source_speed)

# Test wave calculations
c = 3e8  # speed of light (m/s)
sound_speed = 343  # speed of sound (m/s)

# Light wave
freq = 5e14  # Hz
wavelength = wave_wavelength(c, freq)
print(f"Light wavelength: {wavelength*1e9:.0f} nm")

# Sound wave
freq_sound = 440  # Hz (A note)
wavelength_sound = wave_wavelength(sound_speed, freq_sound)
print(f"Sound wavelength: {wavelength_sound:.3f} m")

# Doppler effect
observed_freq = doppler_effect(1000, 30, 0, sound_speed)
print(f"Observed frequency: {observed_freq:.1f} Hz")
