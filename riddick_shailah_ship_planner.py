#Shailah Riddick
#a program that can keep track of the composition of a container
#ship and its cargo. 
class Container:
    def __init__(self, size, cargo_type):
        
        if size not in [1, 2]:
            raise ValueError("Size must be 1 TEU or 2 TEU.")
        if cargo_type not in ['FF', 'CG', 'PG', 'RM', 'IE']:
            raise ValueError("Invalid cargo type.")
        
        self.size = size
        self.cargo_type = cargo_type

    def get_size(self):
        return self.size

    def get_cargo_type(self):
        return self.cargo_type


class ContainerShip:
    def __init__(self, max_capacity, max_speed, min_draft, max_draft):
        
        self.max_capacity = max_capacity
        self.max_speed = max_speed
        self.min_draft = min_draft
        self.max_draft = max_draft
        self.containers = []

    def get_cargo(self):
        return sum(container.get_size() for container in self.containers)

    def get_draft(self):
       
        cargo = self.get_cargo()
        draft_range = self.max_draft - self.min_draft
        return self.min_draft + (draft_range * (cargo / self.max_capacity))

    def get_speed(self):
       
        draft = self.get_draft()
        speed_reduction = (self.max_speed * 0.5) * ((draft - self.min_draft) / (self.max_draft - self.min_draft))
        return self.max_speed - speed_reduction

    def add_container(self, container):
        
        if self.get_cargo() + container.get_size() <= self.max_capacity:
            self.containers.append(container)
        else:
            raise ValueError("Adding this container exceeds the ship's maximum capacity.")

    def print_ship(self):
        
        cargo = self.get_cargo()
        draft = self.get_draft()
        speed = self.get_speed()
        print(f"Cargo: {cargo} TEUs")
        print(f"Draft: {draft:.1f} meters")
        print(f"Speed: {speed:.1f} knots")
        for i, container in enumerate(self.containers):
            if i % 4 == 0 and i != 0:
                print()  
            print(f"[{container.get_cargo_type()}]", end=" ")
        print()


ship = ContainerShip(max_capacity=30, max_speed=20.0, min_draft=10.0, max_draft=30.0)

ship.add_container(Container(2, "CG"))
ship.add_container(Container(2, "IE"))
ship.add_container(Container(1, "PG"))
ship.add_container(Container(1, "PG"))
ship.add_container(Container(1, "PG"))
ship.add_container(Container(1, "PG"))
ship.add_container(Container(2, "RM"))
ship.add_container(Container(2, "RM"))
ship.add_container(Container(2, "CG"))
ship.add_container(Container(2, "IE"))
ship.add_container(Container(1, "PG"))
ship.add_container(Container(1, "PG"))
ship.add_container(Container(1, "PG"))
ship.add_container(Container(2, "RM"))
ship.add_container(Container(1, "PG"))
ship.print_ship()