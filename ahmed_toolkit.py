import os, requests, random, string
from pyfiglet import Figlet
from rich import print as rprint

def banner():
    os.system("clear")
    f = Figlet(font='slant')
    name = input("اكتب الاسم للبنر: ")
    if name == "": name = "Ahmed"
    rprint(f"[bold cyan]{f.renderText(name)}[/bold cyan]")
    rprint(f"[bold white]Made by {name} - Yemen Hacker[/bold white]")
    input("\nاضغط Enter للرجوع...")

def ip_tracker():
    os.system("clear")
    rprint("[bold cyan]--- IP TRACKER ---[/bold cyan]")
    ip = input("ادخل IP (Enter لتتبع نفسك): ")
    try:
        url = f"http://ip-api.com/json/{ip}"
        d = requests.get(url, timeout=10).json()
        if d['status'] == 'success':
            rprint(f"[green]IP: {d['query']}\nCountry: {d['country']} - {d['city']}\nISP: {d['isp']}\nMap: https://maps.google.com/?q={d['lat']},{d['lon']}[/green]")
        else:
            rprint("[red]IP غلط[/red]")
    except:
        rprint("[red]خطأ في النت[/red]")
    input("\nاضغط Enter للرجوع...")

def site_checker():
    os.system("clear")
    rprint("[bold cyan]--- SITE CHECKER ---[/bold cyan]")
    site = input("ادخل الموقع (google.com): ")
    if "http" not in site: site = "https://" + site
    rprint(f"[yellow]فحص {site}...[/yellow]")
    try:
        r = requests.get(site, timeout=8)
        rprint(f"[green]شغال! Code: {r.status_code} - Time: {r.elapsed.total_seconds()}s - Server: {r.headers.get('Server','hidden')}[/green]")
    except:
        rprint("[red]الموقع مطفي او غلط[/red]")
    input("\nاضغط Enter للرجوع...")

def password_gen():
    os.system("clear")
    rprint("[bold magenta]--- PASSWORD GENERATOR ---[/bold magenta]")
    try:
        length = int(input("كم طول الباسورد تبي؟ (مثلا 12): "))
    except:
        length = 12
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    
    rprint(f"\n[bold yellow]باسوردك القوي هو:[/bold yellow]")
    rprint(f"[bold green on black]  {password}  [/bold green on black]")
    print()
    
    # فحص قوة الباسورد
    if length < 8:
        rprint("[bold red]⚠ ضعيف! خله اطول من 8[/bold red]")
    elif length < 12:
        rprint("[bold yellow]⚡ متوسط[/bold yellow]")
    else:
        rprint("[bold green]✔ قوي جداً! مستحيل الاختراق[/bold green]")
    
    input("\nاضغط Enter للرجوع...")

while True:
    os.system("clear")
    f = Figlet(font='small')
    rprint(f"[bold magenta]{f.renderText('Ahmed Tool')}[/bold magenta]")
    rprint("[bold white]1 - Banner Maker\n2 - IP Tracker\n3 - Site Checker\n4 - Password Generator\n0 - Exit[/bold white]")
    choice = input("\nاختر رقم: ")
    if choice == "1": banner()
    elif choice == "2": ip_tracker()
    elif choice == "3": site_checker()
    elif choice == "4": password_gen()
    elif choice == "0":
        rprint("[bold green]مع السلامة يا أسطورة اليمن![/bold green]")
        break
