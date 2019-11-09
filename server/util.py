import re
from urllib.parse import urlparse, parse_qs

def parseRequest(url_string: str):
    parsed_url = urlparse(url=url_string)
    params = parse_qs(qs=parsed_url.query)
    print("URL: {}".format(url_string))
    print("Params: {}".format(params))
    return {
        "path": parsed_url.path,
        "params": params
    }