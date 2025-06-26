# Task-3
# Web Scraper for News Headlines.
# Author: Bineesha K P
# Date: 26-06-2025
import requests
from bs4 import BeautifulSoup

# fetch HTML
url = "https://www.indiatoday.in/"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch page.")
    exit()

#  parse <h2> or <title> tags
soup = BeautifulSoup(response.content, 'html.parser')

# Extract <title> tag
headlines = []
title_tag = soup.find('title')
if title_tag:
    headlines.append(title_tag.get_text(strip=True))

# Extract all <h2> tags
h2_tags = soup.find_all('h2')
for tag in h2_tags:
    text = tag.get_text(strip=True)
    if text:
        headlines.append(text)

# Save the titles in text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines, 1):
        file.write(f"{i}. {headline}\n")

print(" Headlines saved successfully!.✅")
