from urllib.parse import urlparse
grid = "http://localhost:4444"
app = "http://localhost:8080/way2python"
print(urlparse(grid).hostname)
print(urlparse(app).hostname)
print(urlparse(grid).port == urlparse(app).port)
