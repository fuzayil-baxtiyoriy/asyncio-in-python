import time
import requests
import threading
 
 
def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)
 
 
# SYNC FOR I/O bound
# sync_start = time.time()
 
# read_example()
# read_example()
 
# sync_end = time.time()
 
# print(f'Running synchronously took {sync_end - sync_start:.4f} seconds.')

# Threading for I/O bound
thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)
 
thread_start = time.time()
 
thread_1.start()
thread_2.start()
 
print('All threads running!')
 
thread_1.join()
thread_2.join()
 
thread_end = time.time()
 
print(f'Running with threads took {thread_end - thread_start:.4f} seconds.')