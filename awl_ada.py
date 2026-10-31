import pyfiglet
from rich import print as rprint

print("--- My Tool V4 - FINAL ---")

name = input("Your name: ")
color = input("Choose color (cyan, red, green, yellow): ")
font = input("Choose font (slant, big, block, bubble): ")

if font == "":
    font = "slant"
if color == "":
    color = "cyan"

art = pyfiglet.figlet_format(name, font=font)

rprint(f"[bold {color}]{art}[/bold {color}]")
rprint(f"[yellow]Welcome {name} ![/yellow]")

# حفظ التوقيع
with open("my_banner.txt", "w") as f:
    f.write(art)

rprint(f"[green]تم الحفظ في my_banner.txt ✔[/green]")
