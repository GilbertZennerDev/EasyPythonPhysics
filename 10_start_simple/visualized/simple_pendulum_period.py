# Enhanced Simple Pendulum with swing animation
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time

console = Console()

def pendulum_period(length, gravity=9.81):
    """T = 2π√(L/g)"""
    return 2 * math.pi * math.sqrt(length / gravity)

def pendulum_length(period, gravity=9.81):
    """L = (T²g)/(4π²)"""
    return (period**2 * gravity) / (4 * math.pi**2)

def draw_pendulum(angle, length_visual=15):
    """Draw pendulum at specific angle"""
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Calculate bob position
    x = int(length_visual * math.sin(angle_rad))
    y = int(length_visual * math.cos(angle_rad))
    
    # Create pendulum visualization
    pendulum_art = ""
    
    # Fixed point
    pendulum_art += " " * 20 + "╔═══╗\n"
    pendulum_art += " " * 20 + "║ ⚫ ║\n"
    pendulum_art += " " * 20 + "╚═══╝\n"
    
    # String and bob
    for i in range(abs(y)):
        spaces = 20 + int(i * x / abs(y)) if y != 0 else 20
        pendulum_art += " " * spaces + "│\n"
    
    # Bob
    bob_x = 20 + x
    pendulum_art += " " * bob_x + "🔴\n"
    
    return pendulum_art

def animate_pendulum(length, periods=2):
    """Animate pendulum swing"""
    console.print(Panel(Text("🕰️ PENDULUM MOTION SIMULATOR 🕰️", style="bold bright_green"), 
                       border_style="green"))
    
    period = pendulum_period(length)
    console.print(f"[yellow]📏 Length: {length:.2f} m[/yellow]")
    console.print(f"[yellow]⏱️ Period: {period:.2f} s[/yellow]")
    
    # Animation parameters
    max_angle = 30  # degrees
    steps = 60
    total_time = periods * period
    
    for i in range(int(steps * periods)):
        # Calculate current angle using sine wave
        t = i * total_time / (steps * periods)
        angle = max_angle * math.sin(2 * math.pi * t / period)
        
        # Clear screen and draw pendulum
        console.clear()
        console.print(Panel(Text("🕰️ PENDULUM MOTION SIMULATOR 🕰️", style="bold bright_green"), 
                           border_style="green"))
        console.print(f"[yellow]📏 Length: {length:.2f} m[/yellow]")
        console.print(f"[yellow]⏱️ Period: {period:.2f} s[/yellow]")
        console.print(f"[cyan]🌀 Current angle: {angle:.1f}°[/cyan]")
        
        pendulum_visual = draw_pendulum(angle)
        console.print(pendulum_visual)
        
        time.sleep(0.1)

def pendulum_comparison():
    """Compare different pendulum lengths"""
    console.print(Panel(Text("📊 PENDULUM LENGTH COMPARISON 📊", style="bold bright_magenta"), 
                       border_style="magenta"))
    
    lengths = [0.5, 1.0, 1.5, 2.0, 2.5]
    
    table = Table(title="Pendulum Properties", show_header=True)
    table.add_column("Length (m)", style="cyan")
    table.add_column("Period (s)", style="yellow")
    table.add_column("Frequency (Hz)", style="green")
    table.add_column("Visual Scale", style="white")
    
    for length in lengths:
        period = pendulum_period(length)
        frequency = 1 / period
        
        # Visual representation of period
        bar_length = int(period * 3)
        visual_bar = "█" * bar_length
        
        table.add_row(
            f"{length:.1f}",
            f"{period:.2f}",
            f"{frequency:.2f}",
            f"[blue]{visual_bar}[/blue]"
        )
    
    console.print(table)

# Run demonstrations
animate_pendulum(1.0, periods=2)
pendulum_comparison()
