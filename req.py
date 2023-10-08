import requests
import threading
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Create a lock for printing
print_lock = threading.Lock()

# Function to send GET requests
def send_get_requests(url, request_number):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url  # Automatically add "https://" if not present
        response = requests.get(url)
        if response.status_code == 200:
            time.sleep(0.09)  # Introduce a 0.09-second delay before printing success
            with print_lock:
                print(f"{Fore.GREEN + Style.BRIGHT}SUCCESS {Fore.LIGHTBLACK_EX + Style.BRIGHT}({request_number}{Fore.LIGHTBLACK_EX + Style.BRIGHT})")
        else:
            time.sleep(0.09)  # Introduce a 0.09-second delay before printing failure
            with print_lock:
                print(f"{Fore.RED + Style.BRIGHT}FAILED ({Fore.LIGHTBLACK_EX + Style.BRIGHT}{request_number}{Fore.RED + Style.BRIGHT})")
    except Exception as e:
        with print_lock:
            print(f"{Fore.RED + Style.BRIGHT}An error occurred: {str(e)}")

# Get URL and number of requests from the user
url = input("Enter the URL to send GET requests to: ")
num_requests = int(input("Enter the number of requests to send: "))

threads = []

for i in range(1, num_requests + 1):
    thread = threading.Thread(target=send_get_requests, args=(url, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
