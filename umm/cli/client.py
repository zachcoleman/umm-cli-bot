import requests

from umm.utils.config import parse_config


def umm_request(tags):
    config = parse_config()
    params = {t: "" for t in tags}
    resp = requests.get(f"http://0.0.0.0:{config.port}/umm", params=params)
    return resp.json()


def confirm_request(id):
    config = parse_config()
    params = dict(id=id)
    resp = requests.get(f"http://0.0.0.0:{config.port}/confirm", params=params)
    return resp.json()
