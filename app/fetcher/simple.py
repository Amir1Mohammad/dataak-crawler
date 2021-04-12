import requests


class ReadPage:
    def __init__(self):
        pass

    def get_simple_page_without_login(self, url, headers):
        jsonify_page_url = requests.get(url, headers=headers)
        jsonify_page_url = jsonify_page_url.json()
        return jsonify_page_url
