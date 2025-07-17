# Enhanced Density and Buoyancy with fluid simulation
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, BarColumn, TextColumn
import time

console = Console()

def density(mass, volume):
    """ρ = m / V"""
    return mass / volume

def buoyant_force(fluid_density, volume, gravity=9.81):
    """F_b = ρ_fluid × V × g"""
    return fluid_density * volume * gravity

def archimedes_principle(object_density, fluid_density):
    """Calculate submerged volume fraction"""
    return min(object_density / fluid_density, 1.0)

def pressure_at_depth(depth, fluid_density, gravity=9.81):
    """P = ρ × g × h"""
    return fluid_density * gravity * depth

def draw_floating_object(obj_density, fluid_density, obj_name="🔵"):
    """Draw object floating in fluid"""
    submerged_fraction = archimedes_principle(obj_density, fluid_density)
    
    # Container dimensions
    width = 30
    height = 15
    water_level = 10
    
    # Object dimensions
    obj_width = 4
    obj_height = 6
    obj_x = width // 2 - obj_width // 2
    
    # Calculate object position
    if submerged_fraction < 1.0:
        # Floating
        submerged_height = int(obj_height * submerged_fraction)
        obj_y = water_level - submerged_height
        status = "FLOATING"
        color = "green"
    else:
        # Sinking
        obj_y = water_level + 2
        status = "SINKING"
        color = "red"
    
    # Create visualization
    container = [[" " for _ in range(width)] for _ in range(height)]
    
    # Draw container walls
    for y in range(height):
        container[y][0] = "│"
        container[y][width-1] = "│"
    for x in range(width):
        container[height-1][x] = "─"
    
    # Draw water
    for y in range(water_level, height-1):
        for x in range(1, width-1):
            container[y][x] = "~"
    
    # Draw object
    for y in range(obj_y, min(obj_y + obj_height, height-1)):
        for x in range(obj_x, min(obj_x + obj_width, width-1)):
            if y < water_level:
                container[y][x] = "▓"  # Above water
            else:
                container[y][x] = "█"  # Below water
    
    # Convert to string
    visual = ""
    for row in container:
        visual += "".join(row) + "\n"
    
    return visual, status, color

def animate_density_test():
    """Animate density test with different objects"""
    console.print(Panel(Text("⚖️ DENSITY & BUOYANCY SIMULATOR ⚖️", style="bold bright_blue"), 
                       border_style="blue"))
    
    water_density = 1000  # kg/m³
    
    objects = [
        {"name": "🪵 Wood", "density": 600, "emoji": "🪵"},
        {"name": "🧊 Ice", "density": 917, "emoji": "🧊"},
        {"name": "⚽ Ball", "density": 400, "emoji": "⚽"},
        {"name": "🪨 Rock", "density": 2500, "emoji": "🪨"},
        {"name": "🔩 Steel", "density": 7800, "emoji": "🔩"},
    ]
    
    for obj in objects:
        console.clear()
        console.print(Panel(Text("⚖️ DENSITY & BUOYANCY SIMULATOR ⚖️", style="bold bright_blue"), 
                           border_style="blue"))
        
        console.print(f"\n[bold cyan]Testing: {obj['name']} (ρ = {obj['density']} kg/m³)[/bold cyan]")
        
        # Draw floating simulation
        visual, status, color = draw_floating_object(obj["density"], water_density)
        console.print(visual)
        
        # Calculate properties
        volume = 0.001  # 1 liter
        mass = obj["density"] * volume
        buoyant_force_val = buoyant_force(water_density, volume)
        weight = mass * 9.81
        
        # Results table
        results_table = Table(title=f"Results for {obj['name']}", show_header=True)
        results_table.add_column("Property", style="cyan")
        results_table.add_column("Value", style="magenta")
        results_table.add_column("Unit", style="green")
        
        results_table.add_row("Mass", f"{mass:.3f}", "kg")
        results_table.add_row("Weight", f"{weight:.2f}", "N")
        results_table.add_row("Buoyant Force", f"{buoyant_force_val:.2f}", "N")
        results_table.add_row("Net Force", f"{weight - buoyant_force_val:.2f}", "N")
        results_table.add_row("Status", f"[{color}]{status}[/{color}]", "")
        
        console.print(results_table)
        
        if status == "FLOATING":
            submerged_fraction = archimedes_principle(obj["density"], water_density)
            console.print(f"[green]✓ {obj['name']} floats with {submerged_fraction*100:.1f}% submerged[/green]")
        else:
            console.print(f"[red]✗ {obj['name']} sinks to the bottom[/red]")
        
        time.sleep(3)

def pressure_depth_demo():
    """Demonstrate pressure at different depths"""
    console.print(Panel(Text("🌊 UNDERWATER PRESSURE DEMO 🌊", style="bold bright_cyan"), 
                       border_style="cyan"))
    
    water_density = 1000  # kg/m³
    depths = [0, 5, 10, 20, 50, 100]
    
    # Create pressure visualization
    max_depth = max(depths)
    
    for depth in depths:
        pressure = pressure_at_depth(depth, water_density)
        atmospheric_pressure = 101325  # Pa
        gauge_pressure = pressure
        absolute_pressure = pressure + atmospheric_pressure
        
        # Depth visualization
        depth_bar = "█" * int(depth / max_depth * 30) if depth > 0 else ""
        
        console.print(f"\n[cyan]Depth: {depth} m[/cyan]")
        console.print(f"[blue]{'🌊' * int(depth/5)}[/blue]")
        console.print(f"[yellow]Gauge Pressure: {gauge_pressure/1000:.1f} kPa[/yellow]")
        console.print(f"[green]Absolute Pressure: {absolute_pressure/1000:.1f} kPa[/green]")
        
        if depth > 0:
            console.print(f"[white]Depth Scale: {depth_bar}[/white]")
        
        time.sleep(1)

def fluid_comparison():
    """Compare different fluid densities"""
    console.print(Panel(Text("🧪 FLUID DENSITY COMPARISON 🧪", style="bold bright_magenta"), 
                       border_style="magenta"))
    
    fluids = [
        {"name": "🌪️ Air", "density": 1.2, "color": "white"},
        {"name": "⛽ Gasoline", "density": 750, "color": "yellow"},
        {"name": "🛢️ Oil", "density": 900, "color": "bright_yellow"},
        {"name": "💧 Water", "density": 1000, "color": "blue"},
        {"name": "🩸 Blood", "density": 1060, "color": "red"},
        {"name": "🧂 Salt Water", "density": 1025, "color": "cyan"},
        {"name": "🥛 Milk", "density": 1030, "color": "white"},
        {"name": "🍯 Honey", "density": 1400, "color": "bright_yellow"},
        {"name": "🥈 Mercury", "density": 13534, "color": "bright_white"},
    ]
    
    table = Table(title="Fluid Density Comparison", show_header=True)
    table.add_column("Fluid", style="cyan")
    table.add_column("Density (kg/m³)", style="yellow")
    table.add_column("Relative to Water", style="green")
    table.add_column("Density Scale", style="white")
    
    water_density = 1000
    max_density = max(fluid["density"] for fluid in fluids)
    
    for fluid in fluids:
        relative_density = fluid["density"] / water_density
        
        # Density scale (logarithmic for mercury)
        if fluid["density"] > 5000:
            scale_length = int(30 * (1 + 0.1 * (fluid["density"] - 5000) / 1000))
        else:
            scale_length = int(30 * fluid["density"] / 5000)
        
        density_scale = "█" * min(scale_length, 30)
        
        table.add_row(
            fluid["name"],
            f"{fluid['density']:.1f}",
            f"{relative_density:.2f}",
            f"[{fluid['color']}]{density_scale}[/{fluid['color']}]"
        )
    
    console.print(table)

def layered_fluids_demo():
    """Demonstrate fluid layering by density"""
    console.print(Panel(Text("🌈 LAYERED FLUIDS DEMO 🌈", style="bold bright_green"), 
                       border_style="green"))
    
    layers = [
        {"name": "🍯 Honey", "density": 1400, "color": "bright_yellow"},
        {"name": "🧂 Salt Water", "density": 1025, "color": "cyan"},
        {"name": "💧 Water", "density": 1000, "color": "blue"},
        {"name": "🛢️ Oil", "density": 900, "color": "yellow"},
        {"name": "⛽ Gasoline", "density": 750, "color": "bright_red"},
    ]
    
    # Sort by density (heaviest first)
    layers.sort(key=lambda x: x["density"], reverse=True)
    
    console.print("[bold blue]Fluid layers (heaviest at bottom):[/bold blue]")
    
    # Animate layering
    for i, layer in enumerate(layers):
        console.print(f"\n[bold]Layer {i+1}:[/bold]")
        
        # Draw container with layers
        container_height = 15
        layer_height = container_height // len(layers)
        
        visual = ""
        for y in range(container_height):
            line = "│"
            
            # Determine which layer this row belongs to
            layer_index = y // layer_height
            if layer_index < len(layers):
                current_layer = layers[layer_index]
                line += f"[{current_layer['color']}]" + "█" * 20 + f"[/{current_layer['color']}]"
            else:
                line += " " * 20
            
            line += "│"
            visual += line + "\n"
        
        # Bottom of container
        visual += "└" + "─" * 20 + "┘"
        
        console.print(visual)
        
        # Show current layer info
        current_layer = layers[i]
        console.print(f"[{current_layer['color']}]Added: {current_layer['name']} (ρ = {current_layer['density']} kg/m³)[/{current_layer['color']}]")
        
        time.sleep(1.5)
    
    console.print("\n[bold green]✓ All layers settled by density![/bold green]")

# Run demonstrations
animate_density_test()
pressure_depth_demo()
fluid_comparison()
layered_fluids_demo()
