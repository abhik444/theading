import threading
import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        print(f"{url}: {response.status_code}")
    except requests.RequestException as e:
        print(f"{url}: Error fetching URL")

# List of URLs to check
urls = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.amazon.com"
]

threads = []

for url in urls:
    thread = threading.Thread(target=check_website_status, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
