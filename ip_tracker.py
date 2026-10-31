import requests
from rich import print as rprint
import os

os.system("clear")

rprint("[bold cyan]  ╔════════════════════════════╗[/bold cyan]")
rprint("[bold cyan]  ║   IP TRACKER - Yemen Tool  ║[/bold cyan]")
rprint("[bold cyan]  ╚════════════════════════════╝[/bold cyan]")
print()

ip = input("أدخل الـ IP اللي تبي تتتبعه (أو اضغط Enter لتتبع IP حقك): ")

if ip == "":
    ip = "" # يجيب IP حقك تلقائياً

try:
    url = f"http://ip-api.com/json/{ip}?lang=ar"
    response = requests.get(url, timeout=10)
    data = response.json()

    if data['status'] == 'success':
        rprint(f"[bold green]✔ تم العثور على المعلومات![/bold green]")
        print()
        rprint(f"[bold yellow]🌐 الـ IP: [white]{data['query']}[/white]")
        rprint(f"[bold yellow]🏳️ الدولة: [white]{data['country']} - {data['countryCode']}[/white]")
        rprint(f"[bold yellow]🏙️ المدينة: [white]{data['city']} - {data['regionName']}[/white]")
        rprint(f"[bold yellow]🗺️ الموقع: [white]{data['lat']}, {data['lon']}[/white]")
        rprint(f"[bold yellow]🏢 شركة النت: [white]{data['isp']}[/white]")
        rprint(f"[bold yellow]🏢 المنظمة: [white]{data['org']}[/white]")
        rprint(f"[bold yellow]⏰ المنطقة الزمنية: [white]{data['timezone']}[/white]")
        print()
        rprint(f"[dim]Google Maps: https://www.google.com/maps?q={data['lat']},{data['lon']}[/dim]")
    else:
        rprint(f"[bold red]✘ فشل! IP غلط أو غير موجود[/bold red]")

except Exception as e:
    rprint(f"[bold red]✘ خطأ في النت: {e}[/bold red]")

print()
rprint("[bold cyan]تم بواسطة أحمد - عقل اليمن[/bold cyan]")
