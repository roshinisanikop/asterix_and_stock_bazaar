import grpc
import random
import time
import StockTrading_pb2_grpc   
import StockTrading_pb2 

# Update function
def update(stub,stockName, price):
    req = StockTrading_pb2.UpdateRequest(stockName = stockName, price = price)
    res = stub.Update(req)
    return StockTrading_pb2.UpdateResponse(isUpdated = res.isUpdated)


def run():
    # Stock name list
    stockNameList = ['GameStart', 'RottenFishCo', 'BoarCo', 'MenhirCo']

    # Connect to server ip
    with grpc.insecure_channel("172.17.0.2:12949") as channel:
        stub = StockTrading_pb2_grpc.StockTradingStub(channel)

        # numUpdates = 10

        # for i in range(numUpdates):
        # print("-----------------------------------------------------------------------")
        stockName = random.choice(stockNameList)
        price = random.randint(0,500)
        print(f"Update Request for stockname {stockName}, price {price}")

        response = update(stub, stockName, price)

        if response.isUpdated == 1:
            print(f"Update Response: Catalog price update is successful for {stockName}. New price is {price}! ")
        elif response.isUpdated == -1:
            print(f"Update Response: {stockName} is an invalid stock!")
        elif response.isUpdated == -2:
            print(f"Update Response: {price} is an invalid!")
        
        # Sleep - for periodic updates to the stock prices
        time.sleep(random.randint(1,5))


if __name__ == "__main__":
    run()
