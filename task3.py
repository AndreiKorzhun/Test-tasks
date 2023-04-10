import requests
from collections import Counter

path = "http://python.org"
r = requests.get(path)

symbols = Counter(r.text)

with open("readme.md", "w") as file:
    file.write(f"## Symbols found on the site {path}\n\n")
    for symbol, quantity in symbols.items():
        file.write(f"`{symbol}`: `{quantity}`\n\n")
