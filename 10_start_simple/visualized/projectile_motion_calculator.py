# Enhanced Projectile Motion with trajectory visualization
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
import math
import time

console = Console()

def projectile_range(initial_velocity, angle_degrees, gravity=9.81):
    """R = v²sin(2θ)/g"""
    angle_rad = math.radians(angle_degrees)
    return (initial_velocity**2 * math.sin(2 * angle_rad)) / gravity

def projectile_max_height(initial_velocity, angle_degrees, gravity=9.81):
    """h = v²sin²(θ)/(2g)"""
    angle_rad = math.radians(angle_degrees)
    return (initial_velocity**2 * math.sin(angle_rad)**2) / (2 * gravity)

def projectile_time_flight(initial_velocity, angle_degrees, gravity=9.81):
    """t = 2v sin(θ)/g"""
    angle_rad = math.radians(angle_degrees)
    return (2 * initial_velocity * math.sin(angle_rad)) / gravity

def calculate_trajectory_point(v0, angle_degrees, t, gravity=9.81):
    """Calculate x, y position at time t"""
    angle_rad = math.radians(angle_degrees)
    x = v0 * math.cos(angle_rad) * t
    y = v0 * math.sin(angle_rad) * t - 0.5 * gravity * t**2
    return x, y

def draw_trajectory(v0, angle, width=60, height=20):
    """Draw projectile trajectory"""
    flight_time = projectile_time_flight(v0, angle)
    max_range = projectile_range(v0, angle)
    max_height = projectile_max_height(v0, angle)
    
    # Create grid
    grid = [[" " for _ in range(width)] for _ in range(height)]
    
    # Draw trajectory
    for i in range(width):
        t = (i / width) * flight_time
        x, y = calculate_trajectory_point(v0, angle, t)
        
        # Scale to grid
        grid_x = int((x / max_range) * (width - 1))
        grid_y = int((y / max_height) * (height - 1))
        
        if 0 <= grid_x < width and 0 <= grid_y < height:
            grid[height - 1 - grid_y][grid_x] = "•"
    
    # Add ground
    for i in range(width):
        grid[height - 1][i] = "─"
    
    # Add launcher
    grid[height - 1][0] = "🚀"
    
    # Convert to string
    trajectory_str = ""
    for row in grid:
        trajectory_str += "".join(row) + "\n"
    
    return trajectory_str

def animate_projectile(v0, angle):
    """Animate projectile motion"""
    console.print(Panel(Text("🚀 PROJECTILE MOTION SIMULATOR 🚀", style="bold bright_blue"), 
                       border_style="blue"))
    
    flight_time = projectile_time_flight(v0, angle)
    max_range = projectile_range(v0, angle)
    max_height = projectile_max_height(v0, angle)
    
    # Display parameters
    params_table = Table(title="Launch Parameters", show_header=True)
    params_table.add_column("Parameter", style="cyan")
    params_table.add_column("Value", style="magenta")
    params_table.add_column("Unit", style="green")
    
    params_table.add_row("Initial Velocity", f"{v0:.1f}", "m/s")
    params_table.add_row("Launch Angle", f"{angle:.1f}", "°")
    params_table.add_row("Max Range", f"{max_range:.1f}", "m")
    params_table.add_row("Max Height", f"{max_height:.1f}", "m")
    params_table.add_row("Flight Time", f"{flight_time:.1f}", "s")
    
    console.print(params_table)
    
    # Animation
    steps = 50
    for i in range(steps + 1):
        t = (i / steps) * flight_time
        x, y = calculate_trajectory_point(v0, angle, t)
        
        if y < 0:  # Landed
            break
        
        # Create frame
        width, height = 60, 20
        frame = [[" " for _ in range(width)] for _ in range(height)]
        
        # Draw ground
        for j in range(width):
            frame[height - 1][j] = "─"
        
        # Draw trajectory path
        for j in range(i + 1):
            t_path = (j / steps) * flight_time
            x_path, y_path = calculate_trajectory_point(v0, angle, t_path)
            
            grid_x = int((x_path / max_range) * (width - 1))
            grid_y = int((y_path / max_height) * (height - 1))
            
            if 0 <= grid_x < width and 0 <= grid_y < height:
                frame[height - 1 - grid_y][grid_x] = "·"
        
        # Draw projectile
        grid_x = int((x / max_range) * (width - 1))
        grid_y = int((y / max_height) * (height - 1))
        
        if 0 <= grid_x < width and 0 <= grid_y < height:
            frame[height - 1 - grid_y][grid_x] = "🔴"
        
        # Draw launcher
        frame[height - 1][0] = "🚀"
        
        # Display frame
        console.clear()
        console.print(Panel(Text("🚀 PROJECTILE MOTION SIMULATOR 🚀", style="bold bright_blue"), 
                           border_style="blue"))
        
        frame_str = ""
        for row in frame:
            frame_str += "".join(row) + "\n"
        
        console.print(frame_str)
        
        # Display current stats
        vx = v0 * math.cos(math.radians(angle))
        vy = v0 * math.sin(math.radians(angle)) - 9.81 * t
        
        console.print(f"[yellow]Time: {t:.1f}s  Position: ({x:.1f}, {y:.1f})m  Velocity: ({vx:.1f}, {vy:.1f})m/s[/yellow]")
        
        time.sleep(0.2)
    
    console.print("[bold green]🎯 Projectile has landed![/bold green]")

def trajectory_comparison():
    """Compare trajectories at different angles"""
    console.print(Panel(Text("📊 TRAJECTORY ANGLE COMPARISON 📊", style="bold bright_magenta"), 
                       border_style="magenta"))
    
    v0 = 30  # m/s
    angles = [15, 30, 45, 60, 75]
    
    table = Table(title="Trajectory Comparison (v₀ = 30 m/s)", show_header=True)
    table.add_column("Angle (°)", style="cyan")
    table.add_column("Range (m)", style="yellow")
    table.add_column("Max Height (m)", style="green")
    table.add_column("Flight Time (s)", style="blue")
    table.add_column("Trajectory", style="white")
    
    for angle in angles:
        range_val = projectile_range(v0, angle)
        max_height = projectile_max_height(v0, angle)
        flight_time = projectile_time_flight(v0, angle)
        
        # Simple trajectory visualization
        trajectory_bar = "🚀" + "·" * int(range_val / 10) + "🎯"
        
        table.add_row(
            f"{angle}",
            f"{range_val:.1f}",
            f"{max_height:.1f}",
            f"{flight_time:.1f}",
            trajectory_bar
        )
    
    console.print(table)
    
    # Find optimal angle
    optimal_angle = 45
    optimal_range = projectile_range(v0, optimal_angle)
    console.print(f"\n[bold green]🎯 Optimal angle for maximum range: {optimal_angle}° (Range: {optimal_range:.1f}m)[/bold green]")

# Run demonstrations
animate_projectile(30, 45)
trajectory_comparison()
