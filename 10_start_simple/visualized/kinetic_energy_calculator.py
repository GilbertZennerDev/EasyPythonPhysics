# Enhanced Kinetic Energy Calculator with velocity visualization
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.text import Text
import time
import math

console = Console()

def kinetic_energy(mass, velocity):
    """KE = 1/2 × m × v²"""
    return 0.5 * mass * velocity**2

def velocity_from_ke(kinetic_energy, mass):
    """v = √(2KE/m)"""
    return math.sqrt(2 * kinetic_energy / mass)

def create_velocity_bar(velocity, max_velocity=50):
    """Create visual velocity indicator"""
    bar_length = 30
    filled_length = int((velocity / max_velocity) * bar_length)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    
    if velocity < 10:
        color = "green"
    elif velocity < 30:
        color = "yellow"
    else:
        color = "red"
    
    return f"[{color}]{bar}[/{color}] {velocity:.1f} m/s"

def kinetic_energy_demo():
    """Interactive kinetic energy demonstration"""
    console.print(Panel(Text("🚗 KINETIC ENERGY CALCULATOR 🚗", style="bold bright_cyan"), 
                       border_style="cyan"))
    
    # Test objects
    objects = [
        {"name": "🚗 Car", "mass": 1500, "velocity": 25, "emoji": "🚗"},
        {"name": "🏃 Runner", "mass": 70, "velocity": 8, "emoji": "🏃"},
        {"name": "⚽ Soccer Ball", "mass": 0.45, "velocity": 30, "emoji": "⚽"},
        {"name": "🚂 Train", "mass": 50000, "velocity": 15, "emoji": "🚂"},
    ]
    
    # Create comparison table
    table = Table(title="Kinetic Energy Comparison", show_header=True)
    table.add_column("Object", style="cyan")
    table.add_column("Mass (kg)", style="magenta")
    table.add_column("Velocity", style="yellow")
    table.add_column("KE (J)", style="green")
    table.add_column("Visualization", style="white")
    
    for obj in objects:
        ke = kinetic_energy(obj["mass"], obj["velocity"])
        velocity_bar = create_velocity_bar(obj["velocity"])
        
        table.add_row(
            f"{obj['emoji']} {obj['name']}",
            f"{obj['mass']:,}",
            f"{obj['velocity']:.1f} m/s",
            f"{ke:,.0f}",
            velocity_bar
        )
    
    console.print(table)
    
    # Interactive velocity increase simulation
    console.print("\n[bold blue]🏎️ Velocity Increase Simulation[/bold blue]")
    
    car_mass = 1500
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        console=console
    ) as progress:
        
        task = progress.add_task("Accelerating car...", total=50)
        
        for v in range(1, 51):
            ke = kinetic_energy(car_mass, v)
            progress.update(task, advance=1)
            
            if v % 10 == 0:  # Show every 10 m/s
                console.print(f"[cyan]At {v} m/s: KE = {ke:,.0f} J[/cyan]")
            
            time.sleep(0.1)
    
    console.print("[bold green]🏁 Simulation complete![/bold green]")

kinetic_energy_demo()
