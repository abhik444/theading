import threading
import socket
from queue import Queue

# Step 2: Define Target IPs and Ports
ip_range = "192.168.1."
start_ip = 1
end_ip = 10
ports = [22, 80, 443]  # Common ports: SSH, HTTP, HTTPS

# Step 3: Threaded Scan Function
def scan(ip, port, timeout=1):
    socket.setdefaulttimeout(timeout)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        conn = s.connect_ex((ip, port))
        if conn == 0:
            print(f"[+] {ip}:{port} is open")
        else:
            print(f"[-] {ip}:{port} is closed or filtered")

# Step 4: Worker Thread Function
def worker_thread(task_queue):
    while not task_queue.empty():
        ip, port = task_queue.get()
        try:
            scan(ip, port)
        finally:
            task_queue.task_done()

# Step 5: Populate Task Queue and Start Threads
task_queue = Queue()
num_threads = 10  # Adjust based on your concurrency needs and network's tolerance

# Populate the queue with tasks
for ip in range(start_ip, end_ip + 1):
    for port in ports:
        task_queue.put((f"{ip_range}{ip}", port))

# Start worker threads
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=worker_thread, args=(task_queue,))
    t.start()
    threads.append(t)

# Wait for the queue to be empty
task_queue.join()

# Ensuring all threads have completed
for t in threads:
    t.join()

print("Scanning Completed.")
