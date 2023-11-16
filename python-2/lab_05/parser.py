import urllib.request

response = urllib.request.urlopen("http://google.com/")
code = response.getcode()
content = response.read().decode("utf-8")

print(code, content)
