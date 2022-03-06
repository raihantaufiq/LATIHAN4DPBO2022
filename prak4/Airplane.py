from Vehicle import Vehicle

class Airplane(Vehicle):

    def __init__(self, vehicle, type, age, wingsLength):
    #konstruktor
        self.setFuelType(vehicle.getFuelType())
        self.setMaxPassengers(vehicle.getMaxPassengers())
        self.setDriver(vehicle.getDriver())
        self.__type = type
        self.__age = age
        self.__wingsLength = wingsLength

    #set
    def setType(self, type):
        self.__type = type

    def setAge(self, age):
        self.__age = age

    def setwingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    #get
    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

    def getWingsLength(self):
        return self.__wingsLength

    #methods
    def Move(self):
        print("airplane is flying...")

    def showDetail(self):
        print("fuelType : " + self.getFuelType())
        print("maxPassengers : " + str(self.getMaxPassengers()))
        print("Type : " + self.getType())
        print("Age : " + str(self.getAge()))
        print("Wings Length : " + self.getWingsLength())
        print("----- Driver Info -----")
        pengendara = self.getDriver()
        pengendara.showDetail()
