class Container:
   
    SIZE_1_TEU = 1
    SIZE_2_TEU = 2

    CARGO_TYPES = {
        "FF": "Frozen Food",
        "CG": "Consumer Goods",
        "PG": "Processed Goods",
        "RM": "Raw Materials",
        "IE": "Industrial Equipment",
    }

    def __init__(self, size, cargo_type):
       
        if size not in (Container.SIZE_1_TEU, Container.SIZE_2_TEU):
            raise ValueError("Invalid container size. Must be 1 TEU or 2 TEU.")
        if cargo_type not in Container.CARGO_TYPES:
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
        self._cargo = 0  # Cached cargo value
        self._draft = None  # Cached draft value
        self._speed = None  # Cached speed value

    def get_cargo(self):
        
        if self._cargo is None:
            self._cargo = sum(container.get_size() for container in self.containers)
        return self._cargo

    def get_draft(self):
        
        if self._draft is None:
            cargo_ratio = self.get_cargo() / self.max_capacity
            self._draft = self.min_draft + cargo_ratio * (self.max_draft - self.min_draft)
        return self._draft

    def get_speed(self):
        
        if self._speed is None:
            draft_ratio = (self.get_draft() - self.min_draft) / (self.max_draft - self.min_draft)
            speed_reduction = 1 - draft_ratio / 2  # Minimum speed is 50% at max draft
            self._speed = self.max_speed * speed_reduction
        return self._speed

    def add_container(self, container):
       
        if self.get_cargo() + container.get_size() <= self.max_capacity:
            self.containers.append(container)
            self._cargo = None  # Invalidate cached values
            self._draft = None
            self._speed = None
        else:
            raise ValueError("Container addition exceeds ship capacity.")

    def remove_container(self):
        
        if self.containers:
            self.containers.pop()
            self._cargo = None  # Invalidate cached values
            self._draft = None
            self._speed = None
        else:
            raise ValueError("No containers to remove.")

    def print_ship(self):
        
        cargo = self.get_cargo()
        draft = self.get_draft()
        speed = self.get_speed()

        print(f"Cargo: {cargo} TEU")
        print(f"Draft: {draft:.2f} meters")
        print(f"Speed: {speed:.2f} knots")

        print("\nContainer Composition:")
        for i in range(4):
            row = []
            for j in range(min(len(self.containers), 4 - i)):
                row.append(self.containers[-j - 1].get_cargo_type())
            print(" ".join(row))