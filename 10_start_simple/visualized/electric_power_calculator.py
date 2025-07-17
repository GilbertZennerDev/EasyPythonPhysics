# Enhanced Electric Power Calculator with circuit visualization
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, BarColumn, TextColumn
import time
import math

console = Console()

def power_vi(voltage, current):
    """P = V × I"""
    return voltage * current

def power_v2r(voltage, resistance):
    """P = V² / R"""
    return voltage**2 / resistance

def power_i2r(current, resistance):
    """P = I² × R"""
    return current**2 * resistance

def energy_cost(power_watts, hours, cost_per_kwh):
    """Calculate electricity cost"""
    energy_kwh = (power_watts * hours) / 1000
    return energy_kwh * cost_per_kwh

def draw_power_meter(power, max_power=1000):
    """Draw power meter visualization"""
    percentage = min(power / max_power, 1.0)
    meter_width = 30
    filled = int(percentage * meter_width)
    
    if percentage < 0.3:
        color = "green"
    elif percentage < 0.7:
        color = "yellow"
    else:
        color = "red"
    
    meter = "█" * filled + "░" * (meter_width - filled)
    return f"[{color}]{meter}[/{color}] {power:.1f} W"

def draw_electrical_circuit(voltage, current, resistance, power):
    """Draw enhanced circuit diagram"""
    circuit = f"""
[bright_blue]╔══════════════════════════════════════╗[/bright_blue]
[bright_blue]║[/bright_blue]           [bold yellow]ELECTRICAL CIRCUIT[/bold yellow]           [bright_blue]║[/bright_blue]
[bright_blue]╠══════════════════════════════════════╣[/bright_blue]
[bright_blue]║[/bright_blue]                                      [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]     [red]V = {voltage:6.1f} V[/red]  ⚡  [green]P = {power:6.1f} W[/green]     [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]          [yellow]│[/yellow]                       [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]    [yellow]──────┼──────[/yellow]              [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]    [yellow]│[/yellow]     [yellow]│[/yellow]     [yellow]│[/yellow]              [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]    [yellow]│[/yellow]  [cyan]I={current:4.1f}A[/cyan]  [yellow]│[/yellow]              [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]    [yellow]│[/yellow]     [yellow]↓[/yellow]     [yellow]│[/yellow]              [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]    [yellow]│[/yellow]  [magenta]R={resistance:4.1f}Ω[/magenta]  [yellow]│[/yellow]              [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]    [yellow]│[/yellow]           [yellow]│[/yellow]              [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]    [yellow]──────────────[/yellow]              [bright_blue]║[/bright_blue]
[bright_blue]║[/bright_blue]                                      [bright_blue]║[/bright_blue]
[bright_blue]╚══════════════════════════════════════╝[/bright_blue]
"""
    return circuit

def power_calculator_demo():
    """Interactive power calculator demonstration"""
    console.print(Panel(Text("⚡ ELECTRIC POWER CALCULATOR ⚡", style="bold bright_yellow"), 
                       border_style="yellow"))
    
    # Test scenarios
    scenarios = [
        {"name": "🏠 Home Light Bulb", "V": 120, "I": 0.5, "device": "💡"},
        {"name": "🔌 Electric Heater", "V": 240, "I": 8.3, "device": "🔥"},
        {"name": "💻 Laptop Computer", "V": 19, "I": 3.2, "device": "💻"},
        {"name": "🚗 Car Headlight", "V": 12, "I": 4.2, "device": "🚗"},
    ]
    
    for scenario in scenarios:
        console.print(f"\n[bold blue]📊 {scenario['name']} {scenario['device']}[/bold blue]")
        
        voltage = scenario["V"]
        current = scenario["I"]
        resistance = voltage / current
        power = power_vi(voltage, current)
        
        # Draw circuit
        console.print(draw_electrical_circuit(voltage, current, resistance, power))
        
        # Power meter
        power_meter = draw_power_meter(power)
        console.print(f"[bold]Power Meter: {power_meter}[/bold]")
        
        # Verify with different formulas
        power_v2r_calc = power_v2r(voltage, resistance)
        power_i2r_calc = power_i2r(current, resistance)
        
        console.print(f"[dim]Verification: P=V²/R = {power_v2r_calc:.1f}W, P=I²R = {power_i2r_calc:.1f}W[/dim]")
        
        time.sleep(2)

def energy_cost_calculator():
    """Calculate monthly energy costs"""
    console.print(Panel(Text("💰 ENERGY COST CALCULATOR 💰", style="bold bright_green"), 
                       border_style="green"))
    
    appliances = [
        {"name": "💡 LED Bulb", "power": 10, "hours": 5},
        {"name": "📺 TV", "power": 150, "hours": 6},
        {"name": "❄️ Refrigerator", "power": 200, "hours": 24},
        {"name": "🔥 Electric Heater", "power": 1500, "hours": 8},
        {"name": "💻 Computer", "power": 300, "hours": 8},
    ]
    
    cost_per_kwh = 0.12  # $0.12 per kWh
    days_per_month = 30
    
    table = Table(title="Monthly Energy Costs", show_header=True)
    table.add_column("Appliance", style="cyan")
    table.add_column("Power (W)", style="magenta")
    table.add_column("Hours/Day", style="yellow")
    table.add_column("kWh/Month", style="blue")
    table.add_column("Cost/Month", style="green")
    table.add_column("Cost Bar", style="white")
    
    total_cost = 0
    max_cost = 0
    
    # Calculate costs first to get max for visualization
    costs = []
    for appliance in appliances:
        monthly_hours = appliance["hours"] * days_per_month
        monthly_cost = energy_cost(appliance["power"], monthly_hours, cost_per_kwh)
        costs.append(monthly_cost)
        max_cost = max(max_cost, monthly_cost)
    
    # Display results
    for i, appliance in enumerate(appliances):
        monthly_hours = appliance["hours"] * days_per_month
        monthly_kwh = (appliance["power"] * monthly_hours) / 1000
        monthly_cost = costs[i]
        
        # Cost visualization bar
        bar_length = int((monthly_cost / max_cost) * 20)
        cost_bar = "█" * bar_length + "░" * (20 - bar_length)
        
        table.add_row(
            appliance["name"],
            f"{appliance['power']:,}",
            f"{appliance['hours']}",
            f"{monthly_kwh:.1f}",
            f"${monthly_cost:.2f}",
            f"[red]{cost_bar}[/red]"
        )
        
        total_cost += monthly_cost
    
    table.add_row(
        "[bold]TOTAL[/bold]",
        "-",
        "-",
        "-",
        f"[bold]${total_cost:.2f}[/bold]",
        "-"
    )
    
    console.print(table)
    
    # Animated cost accumulation
    console.print("\n[bold blue]📈 Monthly Cost Accumulation:[/bold blue]")
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        console=console
    ) as progress:
        
        task = progress.add_task("Accumulating costs...", total=int(total_cost * 100))
        current_cost = 0
        
        for cost in costs:
            steps = int(cost * 100)
            for _ in range(steps):
                current_cost += 0.01
                progress.update(task, advance=1)
                time.sleep(0.01)
    
    console.print(f"[bold green]💰 Total monthly electricity cost: ${total_cost:.2f}[/bold green]")

# Run demonstrations
power_calculator_demo()
energy_cost_calculator()
