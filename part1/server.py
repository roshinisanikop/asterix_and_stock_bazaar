import socket
import json
from threadpool_library.threadpool import ThreadPool
from stock_catalog import StockCatalog

t_pool = ThreadPool(5)

def client_requests(clientSocket):
    try:
        data = clientSocket.recv(1024).decode()
        if not data:
            return 
        
        request = json.loads(data)
        method = request.get("method")
        stock_name = request.get("stock_name")

        if method == "Lookup":
            result = StockCatalog.lookup_stock(stock_name)
            response = json.dumps(result)  # Return full stock info
        else:
            response = json.dumps({"error": "Invalid request"})

        clientSocket.send(response.encode())

    except Exception as e:
        clientSocket.send(json.dumps({"error": str(e)}).encode())

    finally:
        clientSocket.close()

def server():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # for me - check if params are necessary
    host = "0.0.0.0" # ip-address needs to be updated - to server container's IP address 
    port = 2312
    serverSocket.bind((host, port))  
    # serverSocket.bind("0.0.0.0", 2312)  # ip-address needs to be updated - to server container's IP address 
    serverSocket.listen(5)
    while True:
        clientSocket, addr = serverSocket.accept()
        print(f"Connection accepted from {addr}")

        #dispatch threads to the thread pool 
        ThreadPool.submit(client_requests, clientSocket)

if __name__ == "__main__":
    server()











