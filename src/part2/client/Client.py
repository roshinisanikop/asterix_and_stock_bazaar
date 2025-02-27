import grpc
import random
import components.models.service.StockTradingService_pb2_grpc as StockTradingService_pb2_grpc;
import components.models.request as request
import components.models.response as response


def lookUp(stub,stockName):
    res = stub.Lookup(request.LookupRequest_pb2(stockName = stockName))
    return response.LookUpResponse_pb2(price = res.price, volume = res.volume)


def trade(stub, stockName, n, type):
    res = stub.Trade(request.TradeRequest_pb2(stockName = stockName, itemSize = n, type = type))
    return response.TradeResponse_pb2(isSuccess = res.isSuccess)

def run():
    stockNameList = ['GameStart', 'RottenFishCo', 'BoarCo', 'MenhirCo']
    tradeType = ['buy', 'sell']

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = StockTradingService_pb2_grpc.StockTradingStub(channel)

        numRequests = 10

        for i in range(numRequests):
            stockName = random.choice(stockNameList)
            toss = random.randint(0, 1)
            if toss == 0 :
                lookUp(stub, stockName)
            if toss == 1 :
                n = random.randint(1,500)
                type = random.choice(tradeType)
                trade(stub, stockName, n, type)
            




if __name__ == "__main__":
    run()