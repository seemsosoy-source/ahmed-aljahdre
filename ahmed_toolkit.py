import requests, warnings, datetime
warnings.filterwarnings("ignore")

print("--- Ahmed Toolkit V9 - ETHICAL HACKER ---")
print("For Educational & Authorized Testing Only")
site = input("\nEnter YOUR site: ")

if "127.0.0.1" in site or "localhost" in site:
    if "http" not in site:
        site = "http://" + site
else:
    if "http" not in site:
        site = "https://" + site
    print("WARNING: Make sure you own this site!")

report = []
report.append(f"Ahmed Toolkit V9 Report - {datetime.datetime.now()}")
report.append(f"Target: {site}")
report.append("="*60)

try:
    r = requests.get(site, timeout=10, verify=False)
    h = r.headers
    score = 0
    print("\n[PHASE 1] Header Security Check")
    print(f"Status: {r.status_code}")
    
    checks = ["Content-Security-Policy","X-Frame-Options","Strict-Transport-Security","X-Content-Type-Options","Referrer-Policy","Permissions-Policy","X-XSS-Protection"]
    for ch in checks:
        if ch in h:
            print(f"[PASS] {ch}")
            score+=10
            report.append(f"[PASS] {ch}")
        else:
            print(f"[FAIL] {ch}")
            report.append(f"[FAIL] {ch}")

    if "Server" not in h or "Ahmed" in h.get("Server",""):
        print("[PASS] Server Hidden")
        score+=10
    else:
        print(f"[FAIL] Server: {h.get('Server')}")
    
    if "HttpOnly" in h.get("Set-Cookie","") or "Set-Cookie" not in h:
        print("[PASS] HttpOnly")
        score+=10
    else:
        print("[FAIL] HttpOnly")
    
    if "https" in site or "127.0.0.1" in site or "localhost" in site:
        print("[PASS] HTTPS")
        score+=10
    
    print(f"\nHeader Score: {score}/100")
    report.append(f"Header Score: {score}%")

    print("\n[PHASE 2] XSS Vulnerability Test")
    xss_payload = "<script>alert('XSS')</script>"
    try:
        test_url = f"{site}?q={xss_payload}" if "?" not in site else f"{site}{xss_payload}"
        rx = requests.get(test_url, timeout=10, verify=False)
        if xss_payload in rx.text:
            print("[CRITICAL] XSS VULNERABLE! Input reflected without filtering")
            print("Fix: Use html.escape() in Python")
            report.append("[CRITICAL] XSS VULNERABLE - Reflected")
        else:
            print("[SAFE] XSS Protected - Site filters code")
            report.append("[SAFE] XSS Protected")
    except:
        print("[SAFE] XSS Test Skipped")

    print("\n[PHASE 3] SQL Injection Test")
    sql_payloads = ["'", "' OR '1'='1", "\" OR \"1\"=\"1"]
    vulnerable = False
    sql_errors = ["sql syntax", "mysql", "sqlite", "ORA-", "syntax error"]
    
    for payload in sql_payloads:
        try:
            test_url = f"{site}?id={payload}"
            rs = requests.get(test_url, timeout=10, verify=False)
            text_low = rs.text.lower()
            for err in sql_errors:
                if err in text_low:
                    vulnerable = True
                    break
        except:
            continue
    
    if vulnerable:
        print("[CRITICAL] SQL Injection VULNERABLE! Shows DB errors")
        print("Fix: Use Prepared Statements")
        report.append("[CRITICAL] SQL Injection VULNERABLE")
    else:
        print("[SAFE] SQL Injection Protected - No DB errors")
        report.append("[SAFE] SQL Injection Protected")

    print("\n" + "="*60)
    if score == 100:
        print("FINAL: LEGEND - 100% Headers Secure!")
    print("V9 Scan Complete!")
    
    with open("report_v9.txt","w",encoding="utf-8") as f:
        f.write("\n".join(report))
    print("Saved report_v9.txt")

except Exception as e:
    print(f"[FAIL] {e}")
    print("Make sure secure_site.py is running!")
