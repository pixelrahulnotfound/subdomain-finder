import requests
import time
import re

HEADERS = {"User-Agent": "ReconPipeline/1.0"}

def clean_domain(d: str, domain: str):
    d = d.strip().lower()
    if d.startswith("*."):
        d = d[2:]
    if "@" in d:
        return None
    d = d.rstrip(".")
    if not d.endswith(domain):
        return None
    if not re.match(r"^[a-z0-9.-]+$", d):
        return None
    return d

def get_from_crtsh(domain: str):
    url = f"https://crt.sh/?q=%.{domain}&output=json&dir=asc"

    for attempt in range(3):
        try:
            resp = requests.get(url, timeout=20, headers=HEADERS)
            if resp.status_code == 429:
                time.sleep(3)
                continue
            if resp.status_code != 200:
                return []
            try:
                data = resp.json()
            except:
                return []
            break
        except:
            return []
    else:
        return []

    subs = set()
    for entry in data:
        name = entry.get("name_value", "")
        for n in name.split("\n"):
            cleaned = clean_domain(n, domain)
            if cleaned:
                subs.add(cleaned)
    return list(subs)

def get_from_certspotter(domain: str):
    url = f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names"
    try:
        resp = requests.get(url, timeout=15, headers=HEADERS)
        if resp.status_code != 200:
            return []
        data = resp.json()
    except:
        return []
    subs = set()
    for cert in data:
        for d in cert.get("dns_names", []):
            cleaned = clean_domain(d, domain)
            if cleaned:
                subs.add(cleaned)
    return list(subs)

def get_from_wayback(domain: str):
    url = f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json&fl=original&limit=5000"
    try:
        resp = requests.get(url, timeout=8, headers=HEADERS)
        if resp.status_code != 200:
            return []
        data = resp.json()
    except:
        return []
    subs = set()
    for row in data[1:]:
        url = row[0].lower()
        m = re.search(r"https?://([^/]+)", url)
        if m:
            cleaned = clean_domain(m.group(1), domain)
            if cleaned:
                subs.add(cleaned)
    return list(subs)

def enum_subdomain(domain: str):
    subs = set()
    crt_data = get_from_crtsh(domain)
    subs.update(crt_data)
    cs_data = get_from_certspotter(domain)
    subs.update(cs_data)
    wb_data = get_from_wayback(domain)
    subs.update(wb_data)
    return sorted(subs)
