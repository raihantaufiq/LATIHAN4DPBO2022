from Vehicle import Vehicle

class Ship(Vehicle):

    def __init__(self, vehicle, age, type, countryOfmanufacture):
    #konstruktor
        self.setFuelType(vehicle.getFuelType())
        self.setMaxPassengers(vehicle.getMaxPassengers())
        self.setDriver(vehicle.getDriver())
        self.__age = age
        self.__type = type
        self.__countryOfManufacture = countryOfmanufacture

    #set
    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setCountryOfmanufacture(self, countryOfmanufacture):
        self.__countryOfManufacture = countryOfmanufacture

    #get
    def getAge(self):
        return self.__age

    def getType(self):
        return self.__type

    def getCountryOfmanufacture(self):
        return self.__countryOfManufacture

    #methods
    def Move(self):
        print("ship is sailing...")

    def showDetail(self):
        print("fuelType : " + self.getFuelType())
        print("maxPassengers : " + str(self.getMaxPassengers()))
        print("Age : " + str(self.getAge()))
        print("Type : " + self.getType())
        print("Country Of Manufacture : " + self.getCountryOfmanufacture())
        print("----- Driver Info -----")
        pengendara = self.getDriver()
        pengendara.showDetail()
