import threading
import time


class RequestQueue:
    # synchronisation using semaphores
    def __init__(self):
        self.requests = [] #queue - add jobs to this queue
        self.request_available = threading.Semaphore(0)   #controls the workers waiting
        self.lock = threading.Semaphore(1)  

    def add_requests_to_queue(self, function, args):
        self.lock.acquire()
        self.requests.append((function, args)) 
        self.lock.release()  
        self.request_available.release()  #notifies worker threads that there's a task available

    def get_requests_from_queue(self):
        self.request_available.acquire()
        self.lock.acquire()
        oldest_request= self.requests.pop(0)
        self.lock.release()
        return oldest_request     


class WorkerThreads(threading.Thread):
    #to process incoming requests acquired through semaphore synchronisation
    def __init__(self, request_queue):
        super().__init__(daemon=True) #runs in background
        self.request_queue = request_queue

    def run(self):
        while True:
            function, args = self.request_queue.get_requests_from_queue()
            function(*args) # execute task
    
class ThreadPool:
    def __init__(self, N):
        self.request_queue = RequestQueue()

        self.threads= []
        for i in range(N):
            thread = WorkerThreads(self.request_queue)
            self.threads.append(thread)
            print(thread)
            thread.start() #calls run from workerthread
        
    def submit(self, func, *args):
        # submits a task to the request queue
        self.request_queue.add_requests_to_queue(func, args)

