from Driver import Driver

class Vehicle:

    def __init__(self, fuelType, maxPassengers, driver):
    #konstruktor
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers
        self.__driver = driver

    #set
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    def setDriver(self, driver):
        self.__driver = driver

    #get
    def getFuelType(self):
        return self.__fuelType

    def getMaxPassengers(self):
        return self.__maxPassengers

    def getDriver(self):
        return self.__driver

    #methods
    def Move(self):
        print("vehicle is moving...")

    def showDetail(self):
        print("fuelType : " + self.getFuelType())
        print("maxPassengers : " + str(self.getMaxPassengers()))
        print("----- Driver Info -----")
        self.__driver.showDetail()

