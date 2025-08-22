import requests

response = requests.get('https://www.example.com') # I/O-bound web request
items = response.headers.items()

headers = [f'{key}: {header}' for key, header in items] # CPU-bound response processing

formatted_headers = '\n'.join(headers)  # CPU-bound string concatenation

with open('headers.txt', 'w') as file: # I/O-bound write to disk
    file.write(formatted_headers)
