import json
import threading

class StockCatalog:
    filePath = "/home/cs677-user/lab1/src/part1/stocks.json"
    lock = threading.Lock()  # initialising locks to ensure thread safety when updating JSON. 

    @classmethod
    def loadStockData(cls):
        try:
            with open(cls.filePath, "r") as file:
                data = json.load(file)
                print(f" Loaded stock data: {data}")
                return data
            
        except(FileNotFoundError, json.JSONDecodeError):         
            print("Error: stocks.json is missing or corrupted!")  # Debugging output
            return {}  # # an empty list is returned since the file isn't retrivable. 
    
    @classmethod
    def saveToStocks(cls, stocks):
         with cls.lock:  # lock to prevent race conditions
            with open(cls.filePath, "w") as file:
                json.dump(stocks, file, indent=4)


    @classmethod
    def lookupStock(cls, stock_name):
        stocks = cls.loadStockData()  # Ensure this method exists
        stock = stocks.get(stock_name, None)

        if stock is None:
            return {
                "stock_name": stock_name,
                "price": -1,
                "volume": -1,
                "maxVolume": -1
            }  # Stock not found
        
        return {  # Return stock details along with the stock name
            "stock_name": stock_name,
            "price": stock["price"],
            "volume": stock["volume"],
            "maxVolume": stock["maxVolume"]
        }
    


