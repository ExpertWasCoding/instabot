import threading
import queue
import requests

q = queue.Queue()
working = []

with open("proxy_list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def proxy_checker():
    global q
    global working
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy}, timeout=5)
            if res.status_code == 200:
                working.append(proxy)
        except Exception as e:
            print(f"Error with proxy {proxy}: {str(e)}")
        finally:
            q.task_done()

# Create threads
threads = []
for _ in range(10):
    thread = threading.Thread(target=proxy_checker)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print working proxies
print(working)
