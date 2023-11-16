import requests

response = requests.get("https://example.com")

print(response.status_code)
if response.status_code != 200:
    print("Error")
    exit()
    
print(response.text)
