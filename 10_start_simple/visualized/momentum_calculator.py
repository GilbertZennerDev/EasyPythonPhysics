# Enhanced Momentum Calculator with collision visualization
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.columns import Columns
import time

console = Console()

def momentum(mass, velocity):
    """p = m × v"""
    return mass * velocity

def elastic_collision_1d(m1, v1, m2, v2):
    """Calculate final velocities after elastic collision"""
    v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_final, v2_final

def draw_collision_scene(obj1_pos, obj2_pos, v1, v2, step):
    """Draw collision animation frame"""
    scene_width = 40
    
    # Create scene
    scene = [" "] * scene_width
    
    # Add objects
    if 0 <= obj1_pos < scene_width:
        scene[obj1_pos] = "🔴"
    if 0 <= obj2_pos < scene_width:
        scene[obj2_pos] = "🔵"
    
    # Add velocity indicators
    velocity_line = [" "] * scene_width
    if v1 > 0:
        velocity_line[obj1_pos + 1] = "→" if obj1_pos + 1 < scene_width else " "
    elif v1 < 0:
        velocity_line[obj1_pos - 1] = "←" if obj1_pos - 1 >= 0 else " "
    
    if v2 > 0:
        velocity_line[obj2_pos + 1] = "→" if obj2_pos + 1 < scene_width else " "
    elif v2 < 0:
        velocity_line[obj2_pos - 1] = "←" if obj2_pos - 1 >= 0 else " "
    
    # Create display
    scene_str = "".join(scene)
    velocity_str = "".join(velocity_line)
    
    return f"""
[white]Step {step}:[/white]
[yellow]{'─' * scene_width}[/yellow]
[white]{scene_str}[/white]
[green]{velocity_str}[/green]
[yellow]{'─' * scene_width}[/yellow]
"""

def animate_collision():
    """Animate elastic collision"""
    console.print(Panel(Text("💥 ELASTIC COLLISION SIMULATOR 💥", style="bold bright_red"), 
                       border_style="red"))
    
    # Initial conditions
    m1, m2 = 2.0, 1.0  # masses in kg
    v1_initial, v2_initial = 3.0, -1.0  # initial velocities in m/s
    
    # Calculate final velocities
    v1_final, v2_final = elastic_collision_1d(m1, v1_initial, m2, v2_initial)
    
    # Show initial conditions
    table = Table(title="Initial Conditions", show_header=True)
    table.add_column("Object", style="cyan")
    table.add_column("Mass (kg)", style="magenta")
    table.add_column("Initial Velocity (m/s)", style="yellow")
    table.add_column("Initial Momentum (kg⋅m/s)", style="green")
    
    p1_initial = momentum(m1, v1_initial)
    p2_initial = momentum(m2, v2_initial)
    
    table.add_row("🔴 Object 1", f"{m1}", f"{v1_initial:+.1f}", f"{p1_initial:+.1f}")
    table.add_row("🔵 Object 2", f"{m2}", f"{v2_initial:+.1f}", f"{p2_initial:+.1f}")
    table.add_row("[bold]Total[/bold]", "-", "-", f"[bold]{p1_initial + p2_initial:+.1f}[/bold]")
    
    console.print(table)
    
    # Animation
    obj1_pos, obj2_pos = 10, 30
    collision_point = 20
    
    for step in range(25):
        # Move objects
        if step < 10:  # Before collision
            obj1_pos += 1
            obj2_pos -= 1
            v1_current, v2_current = v1_initial, v2_initial
        else:  # After collision
            obj1_pos += int(v1_final * 0.5)
            obj2_pos += int(v2_final * 0.5)
            v1_current, v2_current = v1_final, v2_final
        
        # Draw scene
        scene = draw_collision_scene(obj1_pos, obj2_pos, v1_current, v2_current, step)
        
        console.clear()
        console.print(Panel(Text("💥 ELASTIC COLLISION SIMULATOR 💥", style="bold bright_red"), 
                           border_style="red"))
        console.print(scene)
        
        if step == 10:
            console.print("[bold red]💥 COLLISION! 💥[/bold red]")
        
        time.sleep(0.3)
    
    # Final results
    console.print("\n[bold blue]📊 Final Results:[/bold blue]")
    final_table = Table(title="After Collision", show_header=True)
    final_table.add_column("Object", style="cyan")
    final_table.add_column("Final Velocity (m/s)", style="yellow")
    final_table.add_column("Final Momentum (kg⋅m/s)", style="green")
    
    p1_final = momentum(m1, v1_final)
    p2_final = momentum(m2, v2_final)
    
    final_table.add_row("🔴 Object 1", f"{v1_final:+.1f}", f"{p1_final:+.1f}")
    final_table.add_row("🔵 Object 2", f"{v2_final:+.1f}", f"{p2_final:+.1f}")
    final_table.add_row("[bold]Total[/bold]", "-", f"[bold]{p1_final + p2_final:+.1f}[/bold]")
    
    console.print(final_table)
    
    # Verify conservation
    momentum_conserved = abs((p1_initial + p2_initial) - (p1_final + p2_final)) < 0.001
    if momentum_conserved:
        console.print("[bold green]✅ Momentum is conserved![/bold green]")
    else:
        console.print("[bold red]❌ Momentum not conserved (calculation error)[/bold red]")

animate_collision()
