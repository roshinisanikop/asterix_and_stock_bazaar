import grpc
from concurrent import futures
import StockTrading_pb2_grpc 
import StockTrading_pb2
import Catalog


class StockTradingServicer(StockTrading_pb2_grpc.StockTradingServicer):
    def __init__(self):
        # Stock Catalog
        self.catalog = Catalog.Catalog()

    # Lookup Function
    def Lookup(self, request, context):
        stockName = request.stockName
        price, volume = self.catalog.lookUp(stockName)
        return StockTrading_pb2.LookupResponse(price = price, volume = volume)
        
    # Trade Function
    def Trade(self, request, context):
        stockName = request.stockName
        n = request.itemSize
        type = request.type
        response = self.catalog.trade(stockName,n,type)
        return StockTrading_pb2.TradeResponse(isSuccess = response)
    
    # Update Function
    def Update(self, request, context):
        stockName = request.stockName
        price = request.price
        response = self.catalog.update(stockName,price)
        return StockTrading_pb2.UpdateResponse(isUpdated = response)
        
# Starting GRPC Server 
def serve():
    # set max worker threads to 10
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5)) 
    StockTrading_pb2_grpc.add_StockTradingServicer_to_server(
        StockTradingServicer(), server
    )
    # Connect to the server port
    ip = "172.17.0.2:12949"
    server.add_insecure_port(ip)
    server.start()
    print(f"Server started on {ip} !")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()