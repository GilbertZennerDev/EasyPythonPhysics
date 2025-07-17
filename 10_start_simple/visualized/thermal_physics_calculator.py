# Enhanced Thermal Physics with temperature visualization
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, BarColumn, TextColumn
import time

console = Console()

def thermal_expansion(original_length, coefficient, temp_change):
    """ΔL = L₀ × α × ΔT"""
    return original_length * coefficient * temp_change

def heat_capacity(mass, specific_heat, temp_change):
    """Q = m × c × ΔT"""
    return mass * specific_heat * temp_change

def celsius_to_kelvin(celsius):
    """K = °C + 273.15"""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """°C = (°F - 32) × 5/9"""
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    """°C = K - 273.15"""
    return kelvin - 273.15

def draw_thermometer(temp_celsius, min_temp=-50, max_temp=150):
    """Draw thermometer visualization"""
    # Normalize temperature to 0-1 range
    temp_normalized = (temp_celsius - min_temp) / (max_temp - min_temp)
    temp_normalized = max(0, min(1, temp_normalized))
    
    # Thermometer height
    height = 20
    filled_height = int(temp_normalized * height)
    
    # Color based on temperature
    if temp_celsius < 0:
        color = "bright_blue"
        symbol = "❄️"
    elif temp_celsius < 30:
        color = "green"
        symbol = "🌡️"
    elif temp_celsius < 60:
        color = "yellow"
        symbol = "🌡️"
    else:
        color = "red"
        symbol = "🔥"
    
    # Build thermometer
    thermometer = f"{symbol} {temp_celsius:.1f}°C\n"
    thermometer += "┌─┐\n"
    
    for i in range(height):
        if i < height - filled_height:
            thermometer += "│ │\n"
        else:
            thermometer += f"│[{color}]█[/{color}]│\n"
    
    thermometer += "└─┘\n"
    thermometer += "███"
    
    return thermometer

def animate_heating(initial_temp, final_temp, duration=5):
    """Animate temperature change"""
    console.print(Panel(Text("🔥 THERMAL HEATING SIMULATION 🔥", style="bold bright_red"), 
                       border_style="red"))
    
    steps = 50
    temp_step = (final_temp - initial_temp) / steps
    
    for i in range(steps + 1):
        current_temp = initial_temp + (i * temp_step)
        
        console.clear()
        console.print(Panel(Text("🔥 THERMAL HEATING SIMULATION 🔥", style="bold bright_red"), 
                           border_style="red"))
        
        # Draw thermometer
        thermometer = draw_thermometer(current_temp)
        console.print(thermometer)
        
        # Temperature conversions
        temp_k = celsius_to_kelvin(current_temp)
        temp_f = current_temp * 9/5 + 32
        
        console.print(f"[cyan]Celsius: {current_temp:.1f}°C[/cyan]")
        console.print(f"[yellow]Kelvin: {temp_k:.1f}K[/yellow]")
        console.print(f"[magenta]Fahrenheit: {temp_f:.1f}°F[/magenta]")
        
        time.sleep(duration / steps)

def thermal_expansion_demo():
    """Demonstrate thermal expansion"""
    console.print(Panel(Text("📏 THERMAL EXPANSION DEMO 📏", style="bold bright_blue"), 
                       border_style="blue"))
    
    materials = [
        {"name": "🔩 Steel", "coefficient": 12e-6, "color": "white"},
        {"name": "🔶 Aluminum", "coefficient": 23e-6, "color": "bright_blue"},
        {"name": "🔹 Copper", "coefficient": 17e-6, "color": "red"},
        {"name": "🪵 Wood", "coefficient": 5e-6, "color": "yellow"},
        {"name": "🏗️ Concrete", "coefficient": 10e-6, "color": "gray"},
    ]
    
    original_length = 10  # meters
    temp_change = 50  # °C
    
    table = Table(title=f"Thermal Expansion (L₀ = {original_length}m, ΔT = {temp_change}°C)", 
                  show_header=True)
    table.add_column("Material", style="cyan")
    table.add_column("Coefficient (×10⁻⁶/°C)", style="yellow")
    table.add_column("Expansion (mm)", style="green")
    table.add_column("Expansion Visualization", style="white")
    
    for material in materials:
        expansion = thermal_expansion(original_length, material["coefficient"], temp_change)
        expansion_mm = expansion * 1000
        
        # Visualization bar
        bar_length = int(expansion_mm / 2)  # Scale for display
        expansion_bar = "█" * bar_length
        
        table.add_row(
            material["name"],
            f"{material['coefficient']*1e6:.0f}",
            f"{expansion_mm:.2f}",
            f"[{material['color']}]{expansion_bar}[/{material['color']}]"
        )
    
    console.print(table)

def heat_transfer_demo():
    """Demonstrate heat transfer calculations"""
    console.print(Panel(Text("🔥 HEAT TRANSFER CALCULATOR 🔥", style="bold bright_yellow"), 
                       border_style="yellow"))
    
    substances = [
        {"name": "💧 Water", "specific_heat": 4186, "color": "blue"},
        {"name": "🔩 Steel", "specific_heat": 500, "color": "white"},
        {"name": "🔶 Aluminum", "specific_heat": 900, "color": "bright_blue"},
        {"name": "🪵 Wood", "specific_heat": 1700, "color": "yellow"},
        {"name": "🪨 Stone", "specific_heat": 840, "color": "gray"},
    ]
    
    mass = 1  # kg
    temp_change = 20  # °C
    
    table = Table(title=f"Heat Required (m = {mass}kg, ΔT = {temp_change}°C)", 
                  show_header=True)
    table.add_column("Substance", style="cyan")
    table.add_column("Specific Heat (J/kg·°C)", style="yellow")
    table.add_column("Heat Required (J)", style="green")
    table.add_column("Heat Scale", style="white")
    
    max_heat = max(substance["specific_heat"] for substance in substances) * mass * temp_change
    
    for substance in substances:
        heat_required = heat_capacity(mass, substance["specific_heat"], temp_change)
        
        # Heat scale visualization
        scale_length = int((heat_required / max_heat) * 30)
        heat_scale = "█" * scale_length
        
        table.add_row(
            substance["name"],
            f"{substance['specific_heat']:,}",
            f"{heat_required:,.0f}",
            f"[{substance['color']}]{heat_scale}[/{substance['color']}]"
        )
    
    console.print(table)

def phase_change_demo():
    """Demonstrate phase changes"""
    console.print(Panel(Text("🧊 PHASE CHANGE DEMO 🧊", style="bold bright_cyan"), 
                       border_style="cyan"))
    
    # Water phase changes
    phases = [
        {"temp": -10, "state": "🧊 Solid Ice", "color": "bright_blue"},
        {"temp": 0, "state": "🧊→💧 Melting", "color": "blue"},
        {"temp": 25, "state": "💧 Liquid Water", "color": "cyan"},
        {"temp": 100, "state": "💧→💨 Boiling", "color": "yellow"},
        {"temp": 110, "state": "💨 Steam", "color": "white"},
    ]
    
    console.print("[bold blue]Water Phase Diagram:[/bold blue]")
    
    for phase in phases:
        thermometer = draw_thermometer(phase["temp"])
        console.print(f"\n[{phase['color']}]{phase['state']}[/{phase['color']}]")
        console.print(thermometer)
        time.sleep(1)

def temperature_converter():
    """Interactive temperature converter"""
    console.print(Panel(Text("🌡️ TEMPERATURE CONVERTER 🌡️", style="bold bright_green"), 
                       border_style="green"))
    
    test_temps = [
        {"desc": "🧊 Absolute Zero", "kelvin": 0},
        {"desc": "🧊 Freezing Point", "kelvin": 273.15},
        {"desc": "🌡️ Room Temperature", "kelvin": 293.15},
        {"desc": "🌡️ Body Temperature", "kelvin": 310.15},
        {"desc": "🔥 Boiling Point", "kelvin": 373.15},
        {"desc": "🔥 Oven Temperature", "kelvin": 473.15},
    ]
    
    table = Table(title="Temperature Conversions", show_header=True)
    table.add_column("Description", style="cyan")
    table.add_column("Kelvin", style="yellow")
    table.add_column("Celsius", style="green")
    table.add_column("Fahrenheit", style="red")
    table.add_column("Thermometer", style="white")
    
    for temp in test_temps:
        celsius = kelvin_to_celsius(temp["kelvin"])
        fahrenheit = celsius * 9/5 + 32
        
        # Mini thermometer
        if celsius < 0:
            therm_color = "bright_blue"
        elif celsius < 40:
            therm_color = "green"
        else:
            therm_color = "red"
        
        mini_therm = f"[{therm_color}]|||[/{therm_color}]"
        
        table.add_row(
            temp["desc"],
            f"{temp['kelvin']:.1f}K",
            f"{celsius:.1f}°C",
            f"{fahrenheit:.1f}°F",
            mini_therm
        )
    
    console.print(table)

# Run demonstrations
animate_heating(20, 100, duration=3)
thermal_expansion_demo()
heat_transfer_demo()
phase_change_demo()
temperature_converter()
