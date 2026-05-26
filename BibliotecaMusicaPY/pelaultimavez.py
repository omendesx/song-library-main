import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def Write(text, speed, cor="white"):
    linha = ""

    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for letra in text:
            linha += letra
            live.update(f"[{cor}]{linha}[/]")
            time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")
    time.sleep(0.6)

def sing():
    clear()
    Write("Só pedi um ultimo favor", 0.06)
    time.sleep(0.8)
    console.print()
    Write("Pela ultima vez, vem dar beijão de lingua na minha boca", 0.07 )
    Write("Vem me encontrar de pouca roupa", 0.06)
    Write("Faz aquele amor de outro planeta",0.07)
    Write("Depois cê me bloqueia, pela ultima vez", 0.05) 
    Write("Vem dar beijão de lingua na minha boca", 0.07 )
    console.print()
    Write("Vem me encontrar de pouca roupa", 0.06)
    Write("Faz aquele amor de outro planeta",0.07)
    Write("Depois cê me bloqueia", 0.06) 
    time.sleep(2)
    clear() 
sing()