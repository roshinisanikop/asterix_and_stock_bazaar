import socket
import json
import random

def sendLookupRequest(host, port):
    """Sends a request to the server"""
    num_requests = 5
    stocks = ["GameStart", "RottenFishCo", "InvalidStock"]  # list of available stocks for part1 implementation
    for i in range(num_requests):
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

host = "172.17.0.2" # ip-address needs to be updated - to server container's IP address 
port = 6169

if __name__ == "__main__":
    sendLookupRequest(host, port)