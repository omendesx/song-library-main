import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

def write(text, speed, cor="white"):
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
    write("Tive um déjà vu que nós entrava numa grife e assaltava tudo", 0.07)
    write("Eu nunca deixo ela no tédio, alugo um privado e vamos para Búzios", 0.06)
    console.print()
    time.sleep(0.1)
    write("Tem spa e um estúdio", 0.06 )
    write("vamo dominar o mundo", 0.06 )
    console.print()
    time.sleep(0.4)
    write("Avançamos anos luz e a 30 comandando tudo no futuro", 0.05 ) 
    time.sleep(0.3)
    write("Estamos anos luz daquele lugar, nem sei como eu vim parar aqui", 0.07)
    console.print()
    write("Tua lingua eu não entendo, eu só sei que tu é chata e muito gata pra mim", 0.06)
    write("Eu vim de lá", 0.02)
    write("Eu vim de longe, de longe de cá", 0.04)
    write("Eu vim pra te ensinar que quando o beat dropa a gente nunca mais pode parar, tsey", 0.04)
    time.sleep(2)
    clear()
sing()