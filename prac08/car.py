class Car:
    """Represent a Car object."""

    def __init__(self, name='', fuel=0):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

        def __str__(self):
            return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)
