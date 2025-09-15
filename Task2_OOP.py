# TASK 2 #

class Appliance:
    # define a base class Appliance
    def __init__(self, brand, power_rating):
        # initialise the appliance with brand name and power rating
        self.brand = brand
        self.power_rating = power_rating

# define the Light_bulb class, which inherits from Appliance
class Light_bulb(Appliance):
    def __init__(self, brand, power_rating, on = False):
        # call the parent class constructor
        super().__init__(brand, power_rating)
        # initialise the light bulb on / off state
        self.on = on

    # switch method toogles the light bulb's state (on / off)
    def switch(self):
        self.on = not self.on

    # use a dunder method to convert object to boolean
    def __bool__(self):
        # returns True if the light bulb is on, if not it's False
        return self.on

# define a Fan class, which inherits from Appliance
class Fan(Appliance):
    def __init__(self, brand, power_rating, speed_levels, current_level = 0):
        # call the parent class constructor
        super().__init__(brand, power_rating)
        # set the speed levels and starting level
        self.speed_levels = speed_levels
        self.current_level = current_level

    # switch method increases the fan's speed level or resets it
    def switch(self):
        if self.current_level < self.speed_levels - 1:
            self.current_level += 1
        else:
            self.current_level = 0

# code usage example
# create / test a light bulb
bulb = Light_bulb('Philips', 60)
print(bool(bulb))
bulb.switch()
print(bool(bulb))

# create / test a fan
fan = Fan('Dyson', 75, speed_levels=3)
print(fan.current_level)
fan.switch()
print(fan.current_level)
fan.switch()
fan.switch()
print(fan.current_level)