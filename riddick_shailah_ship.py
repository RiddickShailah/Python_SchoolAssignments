class ContainerShip:
    def __init__(self, max_capacity, max_speed, min_draft, max_draft):
        """
        Initializes a ContainerShip object.

        Args:
            max_capacity (int): Maximum cargo capacity in TEUs.
            max_speed (float): Maximum speed in knots with no cargo.
            min_draft (float): Minimum draft in meters with no cargo.
            max_draft (float): Maximum draft in meters with full cargo.
        """
        self.max_capacity = max_capacity
        self.max_speed = max_speed
        self.min_draft = min_draft
        self.max_draft = max_draft
        self.containers = []

    def get_cargo(self):
        """
        Calculates and returns the current cargo in TEUs.

        Returns:
            int: Total cargo in TEUs.
        """
        return sum(container.get_size() for container in self.containers)

    def get_draft(self):
        """
        Calculates and returns the current draft of the ship based on cargo.

        Returns:
            float: Current draft in meters.
        """
        cargo = self.get_cargo()
        draft_range = self.max_draft - self.min_draft
        return self.min_draft + (draft_range * (cargo / self.max_capacity))

    def get_speed(self):
        """
        Calculates and returns the current speed of the ship based on draft.

        Returns:
            float: Current speed in knots.
        """
        draft = self.get_draft()
        speed_reduction = (self.max_speed * 0.5) * ((draft - self.min_draft) / (self.max_draft - self.min_draft))
        return self.max_speed - speed_reduction

    def add_container(self, container):
        """
        Adds a container to the ship if it doesn't exceed maximum capacity.

        Args:
            container (Container): The container to add.

        Raises:
            ValueError: If adding the container exceeds the ship's maximum capacity.
        """
        if self.get_cargo() + container.get_size() <= self.max_capacity:
            self.containers.append(container)
        else:
            raise ValueError("Adding this container exceeds the ship's maximum capacity.")

    def remove_container(self):
        """
        Removes the last container added to the ship.

        Raises:
            ValueError: If there are no containers to remove.
        """
        if self.containers:
            self.containers.pop()
        else:
            raise ValueError("No containers to remove.")

    def print_ship(self):
        """
        Prints the current status of the ship, including cargo, draft, speed, and container composition.
        """
        cargo = self.get_cargo()
        draft = self.get_draft()
        speed = self.get_speed()
        print(f"Cargo: {cargo} TEU")
        print(f"Draft: {draft:.1f} meters")
        print(f"Speed: {speed:.1f} knots")
        print("Composition:")
        for i, container in enumerate(self.containers):
            if i % 4 == 0 and i != 0:
                print()  # New line after every 4 containers
            print(f"[{container.get_cargo_type()}]", end=" ")
        print()
