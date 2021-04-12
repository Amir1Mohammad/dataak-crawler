# Created on 2021-04-12 07:34:21
from app.controller.routes import crawling_divar
from app.constants.divar import first_url, header


def read_config():
    return {}


def load_kafka():
    return {}


def main():
    crawling_divar(first_url, header)
    return {}


if __name__ == '__main__':
    main()
