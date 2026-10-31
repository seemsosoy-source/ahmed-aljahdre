import requests
import os
from rich import print as rprint

os.system("clear")
rprint("[bold cyan]╔════════════════════════════╗[/bold cyan]")
rprint("[bold cyan]║  SITE CHECKER - Yemen Tool ║[/bold cyan]")
rprint("[bold cyan]╚════════════════════════════╝[/bold cyan]")
print()

site = input("اكتب اسم الموقع (مثلا google.com): ")

if "http" not in site:
    site = "https://" + site

rprint(f"\n[bold yellow]⏳ جاري فحص {site} ...[/bold yellow]\n")

try:
    r = requests.get(site, timeout=8)
    
    if r.status_code == 200:
        rprint(f"[bold green]✔ الموقع شغال 100%![/bold green]")
    else:
        rprint(f"[bold yellow]⚠ الموقع يرد لكن فيه مشكلة: {r.status_code}[/bold yellow]")
    
    rprint(f"[white]🔗 الرابط: {site}[/white]")
    rprint(f"[white]📡 حالة السيرفر: {r.status_code}[/white]")
    rprint(f"[white]⚡ سرعة الرد: {r.elapsed.total_seconds()} ثانية[/white]")
    rprint(f"[white]🛡️ الحماية: {r.headers.get('Server', 'مخفي')}[/white]")
    print()
    rprint(f"[dim]تم الفحص بواسطة Ahmed - عقل اليمن[/dim]")

except:
    rprint(f"[bold red]✘ الموقع مطفي أو الاسم غلط! جرب اسم ثاني[/bold red]")
