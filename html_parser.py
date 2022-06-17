from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        self.elements = {}
        self.elements_data = {}
        self.temp_tags = []

    def handle_starttag(self, tag, attrs):
        self.temp_tags += tag
        print(self.temp_tags)
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        tag_occurances = [i for i, start_tag in enumerate(self.temp_tags) if tag == start_tag]
        del self.temp_tags[tag_occurances[len(tag_occurances)]]

        print(self.temp_tags)
        print("Encountered an end tag:", tag)

    def handle_data(self, data):

        if not data.strip():
            return
        print("Encountered some data:", data)


if __name__ == "__main__":
    htmlstring = '''    # try using html code with bugs,
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
