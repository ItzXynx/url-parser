import sys
from urllib.parse import urlparse, parse_qs, urlencode

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python main.py <url>")
        sys.exit()
    
    url = sys.argv[1]
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    
    print(f"scheme:   {parsed.scheme}")
    print(f"host:     {parsed.netloc}")
    print(f"path:     {parsed.path}")
    print(f"params:   {params}")
    print(f"fragment: {parsed.fragment or 'none'}")
# updated
