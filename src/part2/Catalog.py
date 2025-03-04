import threading


class Catalog:
    def __init__(self):
        # Using Lock to ensure synchronization in the catalog
        self.lock = threading.Lock()
        # Stock catalog
        self.catalog = {
            "GameStart": {
                'price': 100,
                'volume': 20,
                'maxVolume': 100
            },
            "RottenFishCo": {
                'price': 50,
                'volume': 15,
                'maxVolume': 100            
            },
            "BoarCo": {
                'price': 25,
                'volume': 0,
                'maxVolume': 100           
            },
            "MenhirCo": {
                'price': 70,
                'volume': 10,
                'maxVolume': 100
            }
        }

    # Lookup function logic
    def lookUp(self, stockName):

        with self.lock:
            
            # Invalid stock name
            if stockName not in self.catalog:
                price = -1
                volume = 0
                return price, volume

            price = self.catalog[stockName]['price']
            volume = self.catalog[stockName]['volume']

            # Print catalog
            print(self.catalog) 
            return price, volume
        
    # Trade function logic
    def trade(self, stockName, itemSize, tradeType):
        with self.lock:
            # Invalid stock name
            if stockName not in self.catalog:
                return -1
            
            maxVolume = self.catalog[stockName]['maxVolume']
            volume = self.catalog[stockName]['volume']

            # Stock trading blocked
            if volume + itemSize > maxVolume:
                return 0
            
            # Update the catalog after trade
            self.catalog[stockName]['volume'] = volume + itemSize
            # Print updated atalog
            print(self.catalog)
            return 1

    # Update function logic
    def update(self, stockName, newPrice):
        with self.lock:
            # Invalid stock name
            if stockName not in self.catalog:
                return -1
            # Invalid price
            if newPrice < 0:
                return -2
            # Update the catalog
            self.catalog[stockName]['price'] = newPrice
            # Print updated catalog
            print(self.catalog)
            return 1
        