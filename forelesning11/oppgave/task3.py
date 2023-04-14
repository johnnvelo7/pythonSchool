class MyCar:
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

myHybrid = MyCar(70)
myHybrid.addGas(20)
myHybrid.drive(100)
print(myHybrid.getGasLevel())

