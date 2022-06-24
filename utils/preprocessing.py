from typing import List
from loguru import logger


def load_csic_2010_txt(fname: str) -> List[str]:
    requests = []
    request = None
    with open(fname, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            if "GET" in line or "POST" in line:
                if request:
                    requests.append(request)
                request = line
            elif line.strip():
                request += f" {line}"
    return requests


def extract_url(request: str) -> str:

    split_request = request.split()
    method = split_request[0]
    url = split_request[1]

    # Preprocessing  -> All data has "http://localhost:8080" , "/tienda1"
    for dup in ["http://localhost:8080", "/tienda1"]:
        url = url.replace(dup, "")

    # POST has query in body -> concatenate query to uri
    if method == "POST":
        url += f"?{split_request[-1]}"
        return method + " " + url

    return method + " " + url
