url = 'https://api.divar.ir/v5/posts/'
first_url = url + 'AY0pYjhR'

body = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
        "params": [[["place2", 0, ["1"]], ["cat1", 0, [143]]], 0]}

header = {'Content-type': 'application/json', 'Accept': 'text/plain'}

header_with_token = {
    'Authorization': ''
}
