import json
from src.parser import Parser

if __name__ == '__main__':
    with open('./resume.json') as fr:
        data = json.load(fr)
        print(data)
    parser = Parser(data=data)
    parser.parse()
