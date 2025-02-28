import threading
import time

# class jobs:
#     def __init__(self, args, function):

#         self.function=function
#         self.args=args

#     def exec(self):
#         self.function(*self.args)

class RequestQueue:
    """
    Synchronisation using semaphores.
    """
    def __init__(self):

        self.requests = [] 
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
        self.request_queue= request_queue

    def execute_job(self):
        while True:
            function, args = self.request_queue.get_requests_from_queue()
            function(*args) #execute task
    
class ThreadPool:
    def __init__(self, N):
        self.request_queue = RequestQueue()
        self.threads= []
        for i in range(N):
            self.threads = WorkerThreads(self.request_queue)

        for each_thread in self.threads:
            each_thread.start()
        
    def submit(self, func, *args):
        """Submits a task to the queue"""
        self.request_queue.add_requests_to_queue(function, args)

