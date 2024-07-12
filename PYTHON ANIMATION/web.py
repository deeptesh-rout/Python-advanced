import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia homepage
url = 'https://en.wikipedia.org/wiki/Main_Page'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the headlines (h1, h2, h3) on the page
    headlines = soup.find_all(['h1', 'h2', 'h3'])
    
    # Extract and print the text of each headline
    for headline in headlines:
        print(headline.text.strip())
else:
    print('Failed to retrieve data from the website.')
