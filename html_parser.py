from html.parser import HTMLParser


class TkHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.elements = {}
        self.temp_tags = []

    def handle_starttag(self, tag, attrs):
        self.temp_tags.append(tag)
        print(self.temp_tags)
        self.create_path(self.temp_tags)
        print(self.elements)
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        tag_occurances = [i for i, start_tag in enumerate(self.temp_tags) if tag == start_tag]
        del self.temp_tags[-1]

        print(self.temp_tags)
        print("Encountered an end tag:", tag)

    def handle_data(self, data):
        if not data.strip():
            return
        self.post_data(self.temp_tags, data)
        print(self.elements)
        print("Encountered some data:", data)

    def post_data(self, path, content):
        if not path:
            if "extra_content" not in self.elements:
                self.elements["extra_content"] = [content]
            else:
                self.elements["extra_content"].append(content)

            return

        current_dict = self.elements
        for tag in path[0:-1]:
            current_dict = current_dict[tag]

        current_dict[path[-1]] = content

    def create_path(self, path):
        if not path:
            return

        current_dict = self.elements
        for tag in path:
            if tag not in current_dict.keys():
                current_dict[tag] = {}

            current_dict = current_dict[tag]

if __name__ == "__main__":
    # try using html code with bugs
    htmlstring = '''
    <html>
        <head>
           <title>TesTWEt</title>
        </head>
        <body>
           <h1>Parse me!</h1>
        </body>
    </html>
    '''
    parser = TkHTMLParser()
    parser.feed(htmlstring)
