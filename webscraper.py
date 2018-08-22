import requests

def scrape(base_url, dict_dir, correct_status_code = 200):
    if not get_status(base_url, "", correct_status_code):
        return None

    if base_url[-1] != "/":
        base_url = base_url + "/"

    with open(dict_dir, "r") as _dict:
        urls = try_url(base_url, _dict, correct_status_code)
    
    return urls

def try_url(base_url, _dict, correct_status_code):
    urls = []
    while True:
        line = _dict.readline().strip()
        if not line:
            break
        url = get_status(base_url, line, correct_status_code)
        if url:
            urls.append(url)
    return urls

def get_status(url, word, correct_status_code):
    if url[-1] != "/":
        url = url + "/"
    url = url + word + "/"
    resp = requests.get(url)
    if resp.status_code == correct_status_code:
        return url
    return None

def scrape_recursive(base_url, dict_dir, correct_status_code = 200, max_depth = 5):
    if not get_status(base_url, "", correct_status_code):
        return None

    if base_url[-1] != "/":
        base_url = base_url + "/"
    
    urls = [base_url]
    tried = []
    for _ in range(0, max_depth):
        for url in urls:
            if url in tried:
                continue
            with open(dict_dir, "r") as _dict:
                _new = try_url(url, _dict, correct_status_code)
                if _new:
                    urls.extend(_new)
                tried.append(url)
    return urls
                    
if __name__ == "__main__":
    u = scrape("https:\\www.google.com", "rockyou.txt")
    print(u)