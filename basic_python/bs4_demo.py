from bs4 import BeautifulSoup
import requests

# Make a request to a website
response = requests.get('https://www.google.com')
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print the title of the page
title = soup.title.string
print(f'Title of the page: {title}')

# Find and print all links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
