import grpc
import random
import time
import components.models.service.StockTradingService_pb2_grpc as StockTradingService_pb2_grpc;
import components.models.request as request
import components.models.response as response


def update(stub,stockName, price):
    res = stub.Update(request.UpdateRequest_pb2(stockName = stockName, price = price))
    return response.UpdateResponse_pb2(isUpdated = res.isUpdated)


def run():
    stockNameList = ['GameStart', 'RottenFishCo', 'BoarCo', 'MenhirCo']

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = StockTradingService_pb2_grpc.StockTradingStub(channel)

        numUpdates = 10

        for i in range(numUpdates):
            stockName = random.choice(stockNameList)
            price = random.randint(0,500)
            update(stub, stockName, price)
            time.sleep(random.randint(1,5))


if __name__ == "__main__":
    run()