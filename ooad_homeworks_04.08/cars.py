class Car:
    total_cars = 0
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.__class__.total_cars += 1

    def __str__(self):
        return f'Good car {self.model} !!!'
    
    
    @classmethod
    def get_total_cars_count(cls):
        return cls.total_cars



c = Car("Mercedes", 'CLS', 2018)
