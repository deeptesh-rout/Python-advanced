import requests

# Make a GET request to a webpage

response = requests.get('https://www.google.com')

# Print the status code
print('Status Code:', response.status_code)

# Print the content of the webpage
print('Content:')
print(response.text)
