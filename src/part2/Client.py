import grpc
import random
import StockTrading_pb2_grpc   
import StockTrading_pb2 

# Lookup function
def lookUp(stub,stockName):
    req = StockTrading_pb2.LookupRequest(stockName = stockName)
    res = stub.Lookup(req)
    return StockTrading_pb2.LookupResponse(price = res.price, volume = res.volume)

# Trade function
def trade(stub, stockName, n, type):
    req = StockTrading_pb2.TradeRequest(stockName = stockName, itemSize = n, type = type)
    res = stub.Trade(req)
    return StockTrading_pb2.TradeResponse(isSuccess = res.isSuccess)

def run():
    # Stock name list
    stockNameList = ['GameStart', 'RottenFishCo', 'BoarCo', 'MenhirCo']
    # Trade type
    tradeType = ['buy', 'sell']

    # Connect to server ip
    with grpc.insecure_channel("172.17.0.2:12949") as channel:
        stub = StockTrading_pb2_grpc.StockTradingStub(channel)

        # numRequests = 6

        # for i in range(numRequests):

        # value of toss determines whether trade function will be called or lookup
        toss = random.randint(0, 1)
    
        if toss == 0 :
            # print("-----------------------------------------------------------------------")
            stockName = random.choice(stockNameList)
            print(f"Lookup Request for stockname {stockName}")

            response = lookUp(stub, stockName)

            if response.price == -1:
                print(f"Lookup Response: {stockName} is an invalid stock!")
            else:
                print(f"Lookup Response: Lookup is successful for {stockName} -  Price: {response.price}, Volume: {response.volume}")
        if toss == 1 :
            # print("-----------------------------------------------------------------------")
            stockName = random.choice(stockNameList)
            n = random.randint(1,50)
            type = random.choice(tradeType)
            print(f"Trade Request for stockname {stockName}, number of items {n} and trade type {type}")

            response = trade(stub, stockName, n, type)

            if response.isSuccess == 1:
                print(f"Trade Response: Trade is successful for {stockName} - {type} {n} stocks!")
            elif response.isSuccess == 0:
                print(f"Trade Response: Trade is suspended for {stockName}")
            elif response.isSuccess == -1:
                print(f"Trade Response: {stockName} is an invalid stock!")
            


if __name__ == "__main__":
    run()