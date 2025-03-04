import grpc
import random
import time
import StockTrading_pb2_grpc   
import StockTrading_pb2 
import os
import threading


# # Update function
# latency_file = "latency_results.txt"

# lock = threading.Lock() 
# if os.path.exists(latency_file):
#     open(latency_file, "w").close()

def update(stub,stockName, price):
    req = StockTrading_pb2.UpdateRequest(stockName = stockName, price = price)
    res = stub.Update(req)
    return StockTrading_pb2.UpdateResponse(isUpdated = res.isUpdated)


def run():
    # Stock name list
    stockNameList = ['GameStart', 'RottenFishCo', 'BoarCo', 'MenhirCo', 'InvalidStock']

    # Connect to server ip
    with grpc.insecure_channel("172.17.0.2:12949") as channel:
        stub = StockTrading_pb2_grpc.StockTradingStub(channel)

        numUpdates = 5
        totalUpdateTime = 0

        for i in range(numUpdates):
            # print("-----------------------------------------------------------------------")
            startUpdate = time.time()
            stockName = random.choice(stockNameList)
            price = random.randint(0,500)
            print(f"Update Request for stockname {stockName}, price {price}")

            response = update(stub, stockName, price)
            endUpdate = time.time()
            latencyUpdate = endUpdate - startUpdate
            totalUpdateTime += latencyUpdate
            if response.isUpdated == 1:
                print(f"Update Response: Catalog price update is successful for {stockName}. New price is {price}! ")
            elif response.isUpdated == -1:
                print(f"Update Response: {stockName} is an invalid stock!")
            elif response.isUpdated == -2:
                print(f"Update Response: {price} is an invalid!")
            
            # print(f"Latency for Update: {latencyUpdate}")
            # Sleep - for periodic updates to the stock prices
            time.sleep(random.randint(1,5))
            
        avgLatencyUpdate = totalUpdateTime / numUpdates
        print(f"Avg Latency for Update: {avgLatencyUpdate : .4f} seconds") 
        # with lock:
        #     with open(latency_file, "a") as f:
        #         f.write(f"{avgLatencyUpdate:.4f}\n")

            


if __name__ == "__main__":
    run()
