from urllib.parse import urlsplit

url = "http://localhost:8080.evil.example/path"
print(url.startswith("http://localhost:8080"))
try:
    print(urlsplit(url).port)
except ValueError:
    print("invalid port")
