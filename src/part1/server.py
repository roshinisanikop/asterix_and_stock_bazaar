import socket
# import json
from threadpool import ThreadPool
# from stock_catalog import StockCatalog # supports json file operations
from Catalog import Catalog # integration 

t_pool = ThreadPool(10)


stock_catalog = Catalog()
def client_requests(clientSocket):
    try:
        stock_name = clientSocket.recv(1024).decode('utf-8').strip()  # read stock name directly

        if not stock_name:
            return 
        print(f"server received request for: {stock_name}")
        # perform lookup in Catalog
        price, volume, maxVolume = stock_catalog.lookUp(stock_name)
        if price == -1:  
            response = f"error: stock {stock_name} - not found in catalog"
        elif price == 0:
            response = f"{stock_name}: trading is suspended due to excessive stock trading"
        else:
            response = f"{stock_name}: price={price}, volume={volume}, maxVolume={maxVolume}"

        clientSocket.send(response.encode())

    except Exception as e:
        clientSocket.send(f"error: {str(e)} - not found in catalog".encode())

    finally:
        clientSocket.close()


def server():
    serverSocket = socket.socket()  
    host = "172.17.0.2" # ip-address needs to be updated - to server container's IP address 
    port = 6169
    serverSocket.bind((host, port))  
    serverSocket.listen(5)
    print(f"Server is listening on {host}:{port}...")
    while True:
        clientSocket, addr = serverSocket.accept()
        print(f"Connection accepted from {addr}")

        # dispatch threads to the thread pool 
        t_pool.submit(client_requests, clientSocket)


if __name__ == "__main__":
    server()











