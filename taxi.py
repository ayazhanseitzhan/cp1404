class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23
    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

        def __str__(self):
            """Return a string like a Car but with current fare distance."""
            return "{}, {}km on current fare, ${}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

        def get_fare(self):
            """Return the price for the taxi trip."""
            return self.price_per_km * self.current_fare_distance