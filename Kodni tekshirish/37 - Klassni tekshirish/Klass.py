class Car:
    def __init__(self, make, model, year, km = 0, price = None):
        self.make = make
        self.model = model
        self.year = year
        self.__km = km
        self.price = price
    def set_price(self, price):
        self.price = price
    def get_km(self):
        return self.__km
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}"
        info += f" {self.year}-yil, {self.__km} km yurgan"
        if self.price:
            info += f"Narhi: {self.price}"
        return info
    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("Km manfiy bo'lishi mumkin emas")
avto1 = Car('Gm', 'Malibu', 2020)
print(avto1.get_info())
print(avto1.add_km(-500))
    
