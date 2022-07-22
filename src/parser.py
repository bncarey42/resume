class Parser:
    def __init__(self, data):
        pass

    def __parse_md(self):
        pass

    def __parse_html(self):
        pass

    def parse(self, md=True):
        return self.__parse_md() if md else self.__parse_html()
