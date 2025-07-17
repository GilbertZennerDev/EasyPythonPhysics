# Enhanced Ohm's Law Calculator with colorful circuit visualization
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
import time

console = Console()

def calculate_voltage(current, resistance):
    """V = I × R"""
    return current * resistance

def calculate_current(voltage, resistance):
    """I = V / R"""
    return voltage / resistance

def calculate_resistance(voltage, current):
    """R = V / I"""
    return voltage / current

def draw_circuit(voltage, current, resistance):
    """Draw ASCII circuit diagram"""
    circuit = f"""
    [yellow]┌─────────────────────┐[/yellow]
    [yellow]│[/yellow]     [red]V = {voltage}V[/red]      [yellow]│[/yellow]
    [yellow]│[/yellow]                     [yellow]│[/yellow]
    [yellow]│[/yellow]   [cyan]I = {current}A[/cyan]       [yellow]│[/yellow]
    [yellow]│[/yellow]        ↓         [yellow]│[/yellow]
    [yellow]│[/yellow]   [green]R = {resistance}Ω[/green]      [yellow]│[/yellow]
    [yellow]│[/yellow]                     [yellow]│[/yellow]
    [yellow]└─────────────────────┘[/yellow]
    """
    return circuit

def ohms_law_demo():
    """Interactive Ohm's Law demonstration"""
    console.print(Panel(Text("⚡ OHM'S LAW CALCULATOR ⚡", style="bold bright_yellow"), 
                       border_style="yellow"))
    
    # Test cases
    test_cases = [
        {"V": 12, "I": 2, "R": None, "name": "Find Resistance"},
        {"V": None, "I": 3, "R": 4, "name": "Find Voltage"},
        {"V": 24, "I": None, "R": 8, "name": "Find Current"},
    ]
    
    for case in test_cases:
        console.print(f"\n[bold blue]🔍 {case['name']}[/bold blue]")
        
        if case["R"] is None:
            # Calculate resistance
            resistance = calculate_resistance(case["V"], case["I"])
            voltage, current = case["V"], case["I"]
            console.print(f"[green]✓ Resistance = {resistance:.2f} Ω[/green]")
        elif case["V"] is None:
            # Calculate voltage
            voltage = calculate_voltage(case["I"], case["R"])
            current, resistance = case["I"], case["R"]
            console.print(f"[green]✓ Voltage = {voltage:.2f} V[/green]")
        else:
            # Calculate current
            current = calculate_current(case["V"], case["R"])
            voltage, resistance = case["V"], case["R"]
            console.print(f"[green]✓ Current = {current:.2f} A[/green]")
        
        # Draw circuit
        console.print(draw_circuit(voltage, current, resistance))
        
        # Power calculation
        power = voltage * current
        console.print(f"[bold magenta]⚡ Power = {power:.2f} W[/bold magenta]")
        
        time.sleep(1.5)

ohms_law_demo()
