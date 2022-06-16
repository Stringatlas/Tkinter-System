from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        self.elements = {}
        self.elements_data = {}
        
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)

    def handle_data(self, data):

        if not data.strip():
            return
        print("Encountered some data:", data)


if __name__ == "__main__":
    htmlstring = '''
    <html>
        <head>
           <title>Test</title>
        </head>
        <body>
           <h1>Parse me!</h1>
        </body>
    </html>
    '''
    parser = MyHTMLParser()
    parser.feed(htmlstring)
