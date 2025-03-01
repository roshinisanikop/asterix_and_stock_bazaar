import json
import threading

class StockCatalog:
    file_path = "stocks.json"
    lock = threading.Lock()  # initialising locks to ensure thread safety when updating JSON. 

    @classmethod
    def load_stock_data(cls):
        try:
            with open(cls.file_path, "r") as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return {} # an empty list is returned since the file isn't retrivable. 
    
    @classmethod
    def save_to_stocks(cls, stocks):
         with cls.lock:  # lock to prevent race conditions
            with open(cls.file_path, "w") as file:
                json.dump(stocks, file, indent=4)

    @classmethod
    def lookup_stock(cls, stock_name):
        stocks = cls.load_stock_data()
        stock = stocks.get(stock_name, None)

        if stock is None:
            return -1  # if stock isn't found
        if stock["trading_suspended"]:
            return 0  # trading suspended
        return stock["price"]  # return stock price
       
        # if stock is None:  #check if this if loop is required
        #     return {"price": -1, "volume": -1, "max_volume": -1}  # Not found
        # if stock["trading_suspended"]:
        #     return {"price": 0, "volume": stock["volume"], "max_volume": stock["max_volume"]}  # Trading suspended

        # return {
        #     "price": stock["price"],
        #     "volume": stock["volume"],
        #     "max_volume": stock["max_volume"]
        # }
    #check if update also needs to be written here. 

        
    



