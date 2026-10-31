import requests

url = "https://example.com"
r = requests.get(url)
print(r.status_code)
print(r.text[:200])
