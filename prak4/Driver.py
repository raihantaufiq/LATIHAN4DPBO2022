from Person import Person

class Driver(Person):

    def __init__(self, person, lisenceID, activeUntil, vehicleType):
    #konstruktor
        self.setNIK(person.getNIK())
        self.setName(person.getName())
        self.setGender(person.getGender())
        self.setJob(person.getJob())
        self.__lisenceID = lisenceID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType
        

    #set
    def setLisenceID(self, lisenceID):
        self.__lisenceID = lisenceID

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    #get
    def getLisenceID(self):
        return self.__lisenceID

    def getActiveUntil(self):
        return self.__activeUntil

    def getVehicleType(self):
        return self.__vehicleType

    #methods
    def showDetail(self):
        print("NIK : " + self.getNIK())
        print("Name : " + self.getName())
        if self.getGender():#TRUE=Male, False=Female
            print("Gender : Male")
        else:
            print("Gender : Female")
        job = self.getJob()
        print("NIP : " + job.getNIP())
        print("Company Name : " + job.getCompanyName())
        print("Position : " + job.getPosition())
        print("LisenceID : " + self.getLisenceID())
        print("Active Until : " + self.getActiveUntil())
        print("Vehicle Type : " + self.getVehicleType())
