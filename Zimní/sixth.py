import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            raise ValueError(f"Chyba: URL {url} vrátilo status code {response.status_code}")
        
        content = response.content.decode('utf-8', errors='ignore')
        
        hrefs = re.findall(r'<a\s+href=["\'](https?://[^"\']+)["\']', content)
        
        return hrefs
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Chyba při přístupu na URL {url}: {e}")

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        for href in hrefs:
            print(href)
    except Exception as e:
        print(f"Program skončil chybou: {e}")
