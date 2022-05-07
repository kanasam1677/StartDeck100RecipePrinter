
import requests

targetPageURL="https://www.pokemon-card.com/ex/si/index.html"

r= requests.get(targetPageURL)

print(r.status_code)

print(r.text)
