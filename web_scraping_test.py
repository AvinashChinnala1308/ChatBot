import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://docs.github.com/en"


response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Scraping content from the GitHub Docs home page...")
for section in soup.find_all("section")[:5]:  
    print(section.get_text(strip=True))
