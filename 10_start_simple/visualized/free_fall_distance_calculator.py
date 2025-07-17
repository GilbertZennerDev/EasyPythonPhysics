# Enhanced Free Fall Distance Calculator with Rich formatting
import math
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich.text import Text

console = Console()

def create_physics_header(title):
    """Create a stylized header for physics calculations"""
    header = Text(title, style="bold bright_blue")
    return Panel(header, border_style="bright_blue", padding=(1, 2))

def fall_distance(time_val):
    """Calculate distance fallen in free fall given time"""
    g = 9.81  # gravity acceleration (m/s²)
    return 0.5 * g * time_val**2

def fall_duration(distance):
    """Calculate time to fall given distance"""
    g = 9.81
    return math.sqrt(2 * distance / g)

def animate_fall(height, steps=10):
    """Visual animation of object falling"""
    console.print(create_physics_header("🌍 FREE FALL SIMULATION"))
    
    fall_time = fall_duration(height)
    
    for i in track(range(steps), description="[red]Object falling..."):
        current_time = (i + 1) * fall_time / steps
        current_distance = fall_distance(current_time)
        current_velocity = 9.81 * current_time
        
        # Create visual representation
        fall_progress = int((current_distance / height) * 20)
        sky = "🌤️" + " " * 18
        ground = "🌍" + "─" * 18
        falling_obj = "🔴"
        
        visual = sky + "\n"
        for j in range(20):
            if j == fall_progress:
                visual += falling_obj + "\n"
            else:
                visual += " " + "\n"
        visual += ground
        
        # Create data table
        table = Table(title="Fall Data", show_header=True)
        table.add_column("Parameter", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_column("Unit", style="green")
        
        table.add_row("Time", f"{current_time:.2f}", "s")
        table.add_row("Distance", f"{current_distance:.2f}", "m")
        table.add_row("Velocity", f"{current_velocity:.2f}", "m/s")
        table.add_row("Height", f"{height:.2f}", "m")
        
        console.clear()
        console.print(create_physics_header("🌍 FREE FALL SIMULATION"))
        console.print(visual)
        console.print(table)
        time.sleep(0.3)

# Test the enhanced function
console.print("[bold green]🧮 FREE FALL CALCULATOR[/bold green]")
test_height = 50
animate_fall(test_height)

# Final calculations
final_time = fall_duration(test_height)
console.print(f"\n[bold yellow]⏱️  Total fall time: {final_time:.2f} seconds[/bold yellow]")
console.print(f"[bold red]💨 Final velocity: {9.81 * final_time:.2f} m/s[/bold red]")
