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
git clone https://github.com/pixelrahulnotfound/subdomain-finder
cd subdomain-finder



