import json
import requests
from src.parser import Parser

if __name__ == '__main__':
    raw = response = requests.get(url)
    data = json.load()
    parser = Parser(data=data)
