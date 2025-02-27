import grpc
from concurrent import futures
import components.models.service.StockTradingService_pb2_grpc as StockTradingService_pb2_grpc;
import components.models.Catalog as Catalog;
import components.models.response as response;


class StockTradingServicer(StockTradingService_pb2_grpc.StockTradingServicer):
    def __init__(self):
        self.catalog = Catalog

    def Lookup(self, request, context):
        stockName = request.stockName

        if stockName not in self.catalog:
            price = -1
            volume = 0
        price = self.catalog[stockName]['price']
        volume = self.catalog[stockName]['volume']

        return response.LookUpResponse_pb2(price = price, volume = volume)
        

    def Trade(self, request, context):
        stockName = request.stockName
        n = request.itemSize
        type = request.type

        if stockName not in self.catalog:
            return response.TradeResponse_pb2(isSuccess = -1)
        
        maxVolume = self.catalog[stockName]['maxVolume']
        volume = self.catalog[stockName]['volume']

        if volume + n > maxVolume:
            return response.TradeResponse_pb2(isSuccess = 0)
        
        self.catalog[stockName]['volume'] = volume + n
        return response.TradeResponse_pb2(isSuccess = 1)

    def Update(self, request, context):
        stockName = request.stockName
        price = request.price

        if stockName not in self.catalog:
            return response.UpdateResponse_pb2(isUpdated = -1)
        
        if price < 0:
            return response.UpdateResponse_pb2(isUpdated = -2)
        
        self.catalog[stockName]['price'] = price
        return response.UpdateResponse_pb2(isUpdated = 1)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    StockTradingService_pb2_grpc.add_StockTradingServicer_to_server(
        StockTradingServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()