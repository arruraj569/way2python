from html.parser import HTMLParser
class Reader(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a": print(dict(attrs).get("href"))

Reader().feed('<a href="/guide?a=1&amp;b=2">Guide</a>')
