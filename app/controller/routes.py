from app.engine.parser import JsonParsing
from app.fetcher.simple import ReadPage


def crawling_divar(url, headers):
    parse = JsonParsing()
    read = ReadPage()
    keys_list = []
    jsonify_page_url = read.get_simple_page_without_login(url, headers)
    keys = parse.get_keys(jsonify_page_url, keys_list)
    print(keys)
