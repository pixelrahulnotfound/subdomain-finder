# Subdomain Finder

A lightweight Python tool for discovering subdomains using publicly available SSL Certificate Transparency (CT) logs.  
It queries certificate datasets for a given domain, extracts related subdomains, removes duplicates and noise, and prints a clean list of results.

---

## Features

- Uses public CT logs (like crt.sh) to gather subdomains  
- Simple, minimal, and dependency-light  
- Filters and deduplicates discovered domains  
- Designed as a beginner-friendly recon utility

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pixelnotfound/subdomain-finder
cd subdomain-finder
```



## Usage

Run the tool by passing a domain:

```bash
python3 subdomains.py --domain example.com
```



When executed, the tool will:

1. Query Certificate Transparency logs  
2. Extract subdomains related to the given domain  
3. Remove duplicates and invalid entries  
4. Print a clean list of results

---

## Example Output

```
api.example.com
blog.example.com
cdn.example.com
shop.example.com
```

---






