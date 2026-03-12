class Computer:
    def __init__(self, manufacturer, model, processor, ram, display_size):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.display_size = display_size

    def print_info(self):
        print("Manufacturer: {}".format(self.manufacturer), "Model: {}".format(self.model),
              "Processor: {}".format(self.processor), "RAM: {}".format(self.ram),
              "Display Size: {}".format(self.display_size),end='')


class Laptop(Computer):
    def __init__(self, manufacturer, model, processor, ram, display_size, weight, it):
        super().__init__(manufacturer, model, processor, ram, display_size)
        self.it = it
        self.weight = weight

    def print_info(self):
        #super().print_info()
        print(super().print_info(),'Weight: {}'.format(self.weight), "Touch-Screen: {}".format(self.it))


class Desktop(Computer):
    def __init__(self, manufacturer, model, processor, ram, display_size, type):
        super().__init__(manufacturer, model, processor, ram, display_size)
        self.type = type

    def print_info(self):
        print(super().print_info(), 'Type: {}'.format(self.type))


computer1 = Laptop('Apple', 'MacBook Air', 'Apple M1', '16GB', '13.3"', '2.7 lbs', False)
computer2 = Laptop('HP', 'Envy', 'core i5', '8GB', '15.6"', '4lbs', True)
computer3 = Desktop('Dell', 'Inspiron', 'core i7', '32GB', '27"', 'All-in-One')
computer1.print_info()
computer2.print_info()
computer3.print_info()
