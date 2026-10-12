from html.parser import HTMLParser
class LinkReader(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            link = dict(attrs).get("href")
            if link:
                print(link)

LinkReader().feed('<a href="/guide">Guide</a>')
