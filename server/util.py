from urllib.parse import urlparse, parse_qs, unquote

def parseRequest(url_string: str):
    url_string = unquote(url_string)
    # print("Url_string: ", url_string)

    parsed_url = urlparse(url=url_string)
    params = parse_qs(qs=parsed_url.query)
    # print("URL: {}".format(url_string))
    # print("Params: {}".format(params))
    return {
        "path": parsed_url.path,
        "params": params
    }


"""

(\w+=\w+)|(\w+=\{\w+\:\d+,\s*\w+\:\s*\d+\})

"""