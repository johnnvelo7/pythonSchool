class Car:
    def __init__(self, fuel_efficiency):
        self.fuel_efficiency = fuel_efficiency
        self.fuel_level = 0

    def drive(self, distance):
        fuel_consumed = distance / self.fuel_efficiency
        self.fuel_level -= fuel_consumed

    def getGasLevel(self):
        return self.fuel_level

    def addGas(self, amount):
        self.fuel_level += amount

myHybrid = Car (50) # 50 miles per gallon
myHybrid.addGas (20) # Tank 20 gallons
myHybrid.drive (100) # Drive 100 miles
print (myHybrid.getGasLevel ()) # Print fuel remaining
