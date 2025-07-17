# Enhanced Wave Properties with wave visualization
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
import math
import time

console = Console()

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

def draw_wave(frequency, amplitude, phase=0, width=60):
    """Draw sine wave"""
    wave_str = ""
    height = 10
    
    for y in range(height):
        line = ""
        for x in range(width):
            # Calculate wave value
            wave_val = amplitude * math.sin(2 * math.pi * frequency * x / width + phase)
            
            # Map to screen coordinates
            wave_y = int((wave_val + amplitude) * (height - 1) / (2 * amplitude))
            
            if wave_y == (height - 1 - y):
                line += "●"
            elif y == height // 2:  # Center line
                line += "─"
            else:
                line += " "
        
        wave_str += line + "\n"
    
    return wave_str

def animate_wave(frequency, amplitude=3, cycles=3):
    """Animate wave propagation"""
    console.print(Panel(Text("🌊 WAVE PROPAGATION SIMULATOR 🌊", style="bold bright_cyan"), 
                       border_style="cyan"))
    
    wavelength = 20  # arbitrary units for visualization
    wave_speed_vis = wavelength * frequency
    
    # Display wave properties
    props_table = Table(title="Wave Properties", show_header=True)
    props_table.add_column("Property", style="cyan")
    props_table.add_column("Value", style="magenta")
    props_table.add_column("Unit", style="green")
    
    props_table.add_row("Frequency", f"{frequency:.1f}", "Hz")
    props_table.add_row("Wavelength", f"{wavelength:.1f}", "units")
    props_table.add_row("Amplitude", f"{amplitude:.1f}", "units")
    props_table.add_row("Wave Speed", f"{wave_speed_vis:.1f}", "units/s")
    
    console.print(props_table)
    
    # Animation
    steps = 60
    for i in range(int(steps * cycles)):
        phase = 2 * math.pi * i / steps
        
        console.clear()
        console.print(Panel(Text("🌊 WAVE PROPAGATION SIMULATOR 🌊", style="bold bright_cyan"), 
                           border_style="cyan"))
        
        wave_visual = draw_wave(frequency, amplitude, phase)
        console.print(wave_visual)
        
        # Phase indicator
        console.print(f"[yellow]Phase: {phase:.2f} radians[/yellow]")
        
        time.sleep(0.1)

def electromagnetic_spectrum():
    """Display electromagnetic spectrum"""
    console.print(Panel(Text("📡 ELECTROMAGNETIC SPECTRUM 📡", style="bold bright_yellow"), 
                       border_style="yellow"))
    
    c = 3e8  # speed of light in m/s
    
    em_waves = [
        {"name": "🔴 Radio Waves", "freq": 1e6, "color": "red"},
        {"name": "📺 Microwaves", "freq": 1e9, "color": "yellow"},
        {"name": "🔥 Infrared", "freq": 1e12, "color": "bright_red"},
        {"name": "🌈 Visible Light", "freq": 5e14, "color": "green"},
        {"name": "🔬 Ultraviolet", "freq": 1e15, "color": "blue"},
        {"name": "⚡ X-rays", "freq": 1e18, "color": "magenta"},
        {"name": "☢️ Gamma Rays", "freq": 1e20, "color": "bright_magenta"},
    ]
    
    table = Table(title="Electromagnetic Spectrum", show_header=True)
    table.add_column("Type", style="cyan")
    table.add_column("Frequency (Hz)", style="yellow")
    table.add_column("Wavelength (m)", style="green")
    table.add_column("Energy Scale", style="white")
    
    for wave in em_waves:
        wavelength = wave_wavelength(c, wave["freq"])
        
        # Energy scale visualization
        energy_scale = int(math.log10(wave["freq"]) - 6)
        energy_bar = "█" * energy_scale if energy_scale > 0 else "░"
        
        table.add_row(
            wave["name"],
            f"{wave['freq']:.0e}",
            f"{wavelength:.2e}",
            f"[{wave['color']}]{energy_bar}[/{wave['color']}]"
        )
    
    console.print(table)

def sound_wave_demo():
    """Demonstrate sound wave properties"""
    console.print(Panel(Text("🔊 SOUND WAVE PROPERTIES 🔊", style="bold bright_green"), 
                       border_style="green"))
    
    sound_speed = 343  # m/s at room temperature
    
    musical_notes = [
        {"note": "🎵 C4", "freq": 261.63, "name": "Middle C"},
        {"note": "🎵 D4", "freq": 293.66, "name": "D"},
        {"note": "🎵 E4", "freq": 329.63, "name": "E"},
        {"note": "🎵 F4", "freq": 349.23, "name": "F"},
        {"note": "🎵 G4", "freq": 392.00, "name": "G"},
        {"note": "🎵 A4", "freq": 440.00, "name": "A (Concert Pitch)"},
        {"note": "🎵 B4", "freq": 493.88, "name": "B"},
        {"note": "🎵 C5", "freq": 523.25, "name": "High C"},
    ]
    
    table = Table(title="Musical Notes and Wavelengths", show_header=True)
    table.add_column("Note", style="cyan")
    table.add_column("Frequency (Hz)", style="yellow")
    table.add_column("Wavelength (m)", style="green")
    table.add_column("Pitch Visualization", style="white")
    
    for note in musical_notes:
        wavelength = wave_wavelength(sound_speed, note["freq"])
        
        # Pitch visualization (higher frequency = more compressed)
        pitch_vis = "~" * int(20 - note["freq"] / 50)
        
        table.add_row(
            note["note"],
            f"{note['freq']:.2f}",
            f"{wavelength:.3f}",
            f"[blue]{pitch_vis}[/blue]"
        )
    
    console.print(table)
    
    # Doppler effect example
    console.print("\n[bold blue]🚗 Doppler Effect Example[/bold blue]")
    
    source_freq = 1000  # Hz (car horn)
    car_speed = 30  # m/s
    
    # Car approaching
    observed_freq_approach = doppler_effect(source_freq, car_speed, 0, sound_speed)
    # Car receding
    observed_freq_recede = doppler_effect(source_freq, -car_speed, 0, sound_speed)
    
    doppler_table = Table(title="Doppler Effect (Car Horn at 1000 Hz)", show_header=True)
    doppler_table.add_column("Scenario", style="cyan")
    doppler_table.add_column("Observed Frequency", style="yellow")
    doppler_table.add_column("Change", style="green")
    
    doppler_table.add_row("🚗→ Car Approaching", f"{observed_freq_approach:.1f} Hz", "[green]Higher[/green]")
    doppler_table.add_row("🚗 Car Stationary", f"{source_freq:.1f} Hz", "[yellow]Normal[/yellow]")
    doppler_table.add_row("🚗← Car Receding", f"{observed_freq_recede:.1f} Hz", "[red]Lower[/red]")
    
    console.print(doppler_table)

# Run demonstrations
animate_wave(2, amplitude=3, cycles=2)
electromagnetic_spectrum()
sound_wave_demo()
