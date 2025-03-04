import socket
import random
import time
import os
import threading

latency_file = "latency_results.txt"

lock = threading.Lock() 
if os.path.exists(latency_file):
    open(latency_file, "w").close()

def sendLookupRequest(host, port):
    """Sends a request to the server"""
    num_requests = 5
    stocks = ["GameStart", "RottenFishCo", "InvalidStock"]  # list of available stocks for part1 implementation
    totalLookupTime = 0
    for i in range(num_requests):
        startLookup = time.time()
        stock_name = random.choice(stocks) 

        try:
            clientSocket = socket.socket()
            clientSocket.connect((host, port))
            clientSocket.send(stock_name.encode())
            response = clientSocket.recv(1024).decode('utf-8')
            print(f"response: {response}")

        except socket.error as e:
            print(f"socket error: {e}")
        except Exception as e:
            print(f"unexpected error: {e}")
        finally:
            clientSocket.close() 
        endLookUp = time.time()
        latencyLookUp = endLookUp - startLookup
        totalLookupTime += latencyLookUp
    
    avgLatencyLookup = totalLookupTime / num_requests
    print(f"Avg Latency for Lookup: {avgLatencyLookup : .4f} seconds") 
    
    with lock:
        with open(latency_file, "a") as f:
            f.write(f"{avgLatencyLookup:.4f}\n")
    


host = "172.17.0.2" # ip-address needs to be updated - to server container's IP address 
port = 6169

if __name__ == "__main__":
    sendLookupRequest(host, port)