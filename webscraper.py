import requests

def scrape(base_url, dict_dir, correct_status_code = 200):
    if base_url[-1] != "/":
        base_url = base_url + "/"

    if not get_status(base_url, "", correct_status_code):
        return
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
    url = url + word + "/"
    resp = requests.get(url)
    if resp.status_code == correct_status_code:
        return url
    return None

if __name__ == "__main__":
    u = scrape("https:\\www.google.com", "rockyou.txt")
    print(u)