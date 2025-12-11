from subdomains import enum_subdomain

if __name__=="__main__":
    domain=input("enter the target domain:").strip()
    subs=enum_subdomain(domain)
    print(f"found {len(subs)} subdomains for the domain: {domain}")
    for i in subs:
        print(i)
