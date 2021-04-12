import requests


def get_keys(d_or_l, keys_list):
    if isinstance(d_or_l, dict):
        for k, v in iter(sorted(d_or_l.items())):
            if isinstance(v, list):
                get_keys(v, keys_list)
            elif isinstance(v, dict):
                get_keys(v, keys_list)
            keys_list.append(k)
    elif isinstance(d_or_l, list):
        for i in d_or_l:
            if isinstance(i, list):
                get_keys(i, keys_list)
            elif isinstance(i, dict):
                get_keys(i, keys_list)
    else:
        print("** Skipping item of type: {}".format(type(d_or_l)))
    print(keys_list)
    return keys_list


def get_json_tag(url, body, headers):
    jsonify_page_url = requests.get(url, headers=headers)
    jsonify_page_url = jsonify_page_url.json()
    keys_list = []
    d = jsonify_page_url
    a = get_keys(d, keys_list)
    print(a)
