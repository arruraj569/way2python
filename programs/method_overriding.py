class Reporter:
    def format(self, name):
        return f"Result: {name}"
class HtmlReporter(Reporter):
    def format(self, name):
        return f"<p>{super().format(name)}</p>"

print(HtmlReporter().format("login"))
